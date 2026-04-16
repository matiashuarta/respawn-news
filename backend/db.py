"""
db.py — SQLite database setup and query helpers
"""
import sqlite3
import hashlib
import secrets
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "respawn.db")


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


def init_db():
    conn = get_conn()
    c = conn.cursor()

    # Users table
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT    NOT NULL UNIQUE,
            email    TEXT    NOT NULL UNIQUE,
            password TEXT    NOT NULL,
            role     TEXT    NOT NULL DEFAULT 'user',
            created  TEXT    DEFAULT (datetime('now'))
        )
    """)

    # Sessions table
    c.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            token    TEXT PRIMARY KEY,
            user_id  INTEGER NOT NULL,
            created  TEXT DEFAULT (datetime('now')),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    # Articles table
    c.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            category  TEXT    NOT NULL,
            tag       TEXT    NOT NULL,
            tag_class TEXT    NOT NULL,
            headline  TEXT    NOT NULL,
            summary   TEXT    NOT NULL,
            author    TEXT    NOT NULL,
            date      TEXT    NOT NULL,
            score     REAL,
            image     TEXT    NOT NULL,
            featured  INTEGER NOT NULL DEFAULT 0
        )
    """)

    # ── Migrations ─────────────────────────────────────────────────────────────

    # Add body column to articles if missing
    existing_cols = [row[1] for row in conn.execute("PRAGMA table_info(articles)").fetchall()]
    if "body" not in existing_cols:
        conn.execute("ALTER TABLE articles ADD COLUMN body TEXT NOT NULL DEFAULT ''")
        conn.commit()
        print("[DB] Migrated: added body column to articles")

    # Add image_position column to articles if missing
    existing_cols = [row[1] for row in conn.execute("PRAGMA table_info(articles)").fetchall()]
    if "image_position" not in existing_cols:
        conn.execute("ALTER TABLE articles ADD COLUMN image_position TEXT NOT NULL DEFAULT 'center center'")
        conn.commit()
        print("[DB] Migrated: added image_position column to articles")

    # Add avatar column to users if missing
    user_cols = [row[1] for row in conn.execute("PRAGMA table_info(users)").fetchall()]
    if "avatar" not in user_cols:
        conn.execute("ALTER TABLE users ADD COLUMN avatar TEXT NOT NULL DEFAULT ''")
        conn.commit()
        print("[DB] Migrated: added avatar column to users")

    # Comments table
    c.execute("""
        CREATE TABLE IF NOT EXISTS comments (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            article_id INTEGER NOT NULL,
            user_id    INTEGER NOT NULL,
            username   TEXT    NOT NULL,
            body       TEXT    NOT NULL,
            parent_id  INTEGER DEFAULT NULL,
            created    TEXT    DEFAULT (datetime('now')),
            FOREIGN KEY (article_id) REFERENCES articles(id) ON DELETE CASCADE,
            FOREIGN KEY (user_id)    REFERENCES users(id),
            FOREIGN KEY (parent_id)  REFERENCES comments(id) ON DELETE CASCADE
        )
    """)

    # Comment votes table
    c.execute("""
        CREATE TABLE IF NOT EXISTS comment_votes (
            comment_id INTEGER NOT NULL,
            user_id    INTEGER NOT NULL,
            vote       INTEGER NOT NULL CHECK(vote IN (1, -1)),
            PRIMARY KEY (comment_id, user_id),
            FOREIGN KEY (comment_id) REFERENCES comments(id) ON DELETE CASCADE,
            FOREIGN KEY (user_id)    REFERENCES users(id)
        )
    """)

    # ── Migration: add parent_id to existing comments table if missing ─────────
    comment_cols = [row[1] for row in conn.execute("PRAGMA table_info(comments)").fetchall()]
    if "parent_id" not in comment_cols:
        conn.execute("ALTER TABLE comments ADD COLUMN parent_id INTEGER DEFAULT NULL")
        conn.commit()
        print("[DB] Migrated: added parent_id column to comments")

    conn.commit()

    # ── Seed admin user ────────────────────────────────────────────────────────
    admin = conn.execute(
        "SELECT id FROM users WHERE email = 'admin@respawn.gg'"
    ).fetchone()
    if not admin:
        pw_hash = hash_password("admin123")
        conn.execute(
            "INSERT INTO users (username, email, password, role) VALUES (?, ?, ?, ?)",
            ("admin", "admin@respawn.gg", pw_hash, "admin"),
        )
        conn.commit()
        print("[DB] Admin user created — email: admin@respawn.gg  password: admin123")

    # ── Seed articles if empty ─────────────────────────────────────────────────
    count = conn.execute("SELECT COUNT(*) FROM articles").fetchone()[0]
    if count == 0:
        import news_data
        for a in news_data.ARTICLES:
            conn.execute(
                """INSERT INTO articles
                   (category, tag, tag_class, headline, summary, author, date, score, image, image_position, featured, body)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    a["category"], a["tag"], a["tag_class"],
                    a["headline"], a["summary"], a["author"],
                    a["date"], a.get("score"), a["image"],
                    a.get("image_position", "50% 50%"),
                    1 if a.get("featured") else 0,
                    a.get("body", ""),
                ),
            )
        conn.commit()
        print(f"[DB] Seeded {len(news_data.ARTICLES)} articles")
    else:
        # ── Patch existing articles: sync images, body, and image_position ─────
        import news_data
        patched = 0
        inserted = 0
        for a in news_data.ARTICLES:
            row = conn.execute(
                "SELECT image, body, image_position FROM articles WHERE id = ?", (a["id"],)
            ).fetchone()
            if not row:
                # New article added to seed data — insert it
                conn.execute(
                    """INSERT INTO articles
                       (id, category, tag, tag_class, headline, summary, author, date, score, image, image_position, featured, body)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (
                        a["id"], a["category"], a["tag"], a["tag_class"],
                        a["headline"], a["summary"], a["author"],
                        a["date"], a.get("score"), a["image"],
                        a.get("image_position", "50% 50%"),
                        1 if a.get("featured") else 0,
                        a.get("body", ""),
                    ),
                )
                inserted += 1
                continue
            new_image    = a["image"]
            new_body     = a.get("body", "")
            new_img_pos  = a.get("image_position", "50% 50%")
            old_image    = row["image"]
            old_body     = row["body"] or ""
            old_img_pos  = row["image_position"] or "50% 50%"
            needs_update = (old_image != new_image) or (not old_body and new_body) or (old_img_pos != new_img_pos)
            if needs_update:
                conn.execute(
                    "UPDATE articles SET image = ?, body = ?, image_position = ? WHERE id = ?",
                    (new_image, new_body if not old_body else old_body, new_img_pos, a["id"]),
                )
                patched += 1
        if inserted:
            conn.commit()
            print(f"[DB] Inserted {inserted} new seed articles")
        if patched:
            conn.commit()
            print(f"[DB] Patched {patched} articles (images/body)")

    # ── Forum tables ───────────────────────────────────────────────────────────
    c.execute("""
        CREATE TABLE IF NOT EXISTS forum_categories (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT    NOT NULL,
            slug        TEXT    NOT NULL UNIQUE,
            description TEXT    NOT NULL,
            icon        TEXT    NOT NULL DEFAULT '💬',
            color       TEXT    NOT NULL DEFAULT '#7c3aed',
            sort_order  INTEGER NOT NULL DEFAULT 0
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS forum_topics (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            category_id  INTEGER NOT NULL,
            title        TEXT    NOT NULL,
            user_id      INTEGER NOT NULL,
            username     TEXT    NOT NULL,
            created      TEXT    DEFAULT (datetime('now')),
            last_post_at TEXT    DEFAULT (datetime('now')),
            post_count   INTEGER NOT NULL DEFAULT 0,
            view_count   INTEGER NOT NULL DEFAULT 0,
            pinned       INTEGER NOT NULL DEFAULT 0,
            locked       INTEGER NOT NULL DEFAULT 0,
            FOREIGN KEY (category_id) REFERENCES forum_categories(id),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS forum_posts (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id INTEGER NOT NULL,
            user_id  INTEGER NOT NULL,
            username TEXT    NOT NULL,
            body     TEXT    NOT NULL,
            created  TEXT    DEFAULT (datetime('now')),
            likes    INTEGER NOT NULL DEFAULT 0,
            FOREIGN KEY (topic_id) REFERENCES forum_topics(id) ON DELETE CASCADE,
            FOREIGN KEY (user_id)  REFERENCES users(id)
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS forum_post_likes (
            post_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            PRIMARY KEY (post_id, user_id),
            FOREIGN KEY (post_id) REFERENCES forum_posts(id) ON DELETE CASCADE,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)
    conn.commit()

    # ── Seed forum categories (upsert by slug so new ones are added safely) ──────
    ALL_CATS = [
        ("General Discussion", "general",      "Talk about anything gaming-related.",                       "💬", "#7c3aed",  1),
        ("PlayStation",        "playstation",   "PS5, PS4, PSVR, and everything Sony.",                     "🎮", "#003087",  2),
        ("Xbox",               "xbox",          "Xbox Series X/S, Game Pass, and Microsoft gaming.",        "🟩", "#107c10",  3),
        ("Nintendo",           "nintendo",      "Switch, Zelda, Mario, and Nintendo exclusives.",           "🔴", "#e4000f",  4),
        ("PC Gaming",          "pc",            "Hardware, Steam, mods, and all things PC.",                "💻", "#1a73e8",  5),
        ("eSports",            "esports",       "Tournaments, teams, and competitive gaming.",              "🏆", "#f59e0b",  6),
        ("Mobile Gaming",      "mobile",        "iOS, Android, and handheld gaming.",                       "📱", "#10b981",  7),
        ("VR / AR",            "vr-ar",         "Virtual reality, augmented reality, and mixed reality.",   "🥽", "#8b5cf6",  8),
        ("Retro Gaming",       "retro",         "Classic consoles, emulation, and gaming history.",         "👾", "#a16207",  9),
        ("Game Development",   "gamedev",       "Indie dev, engines, tutorials, and game design talk.",     "⚙️", "#0891b2", 10),
        ("Tech & Hardware",    "tech",          "GPUs, CPUs, monitors, peripherals, and PC building.",      "🖥️", "#475569", 11),
        ("Deals & Sales",      "deals",         "Game deals, sales, bundles, and free-to-play finds.",      "🛒", "#059669", 12),
        ("Looking for Group",  "lfg",           "Find teammates, guilds, clans, and co-op partners.",       "🤝", "#d97706", 13),
        ("Sports",             "sports",        "Football, basketball, F1, FIFA, and all real-world sport.", "⚽", "#16a34a", 14),
        ("Movies & TV",        "movies-tv",     "Films, series, trailers, reviews, and streaming.",         "🎬", "#dc2626", 15),
        ("Music",              "music",         "Game soundtracks, artists, albums, and concerts.",         "🎵", "#7c3aed", 16),
        ("Anime & Manga",      "anime",         "Anime series, manga, light novels, and Japanese culture.", "🌸", "#ec4899", 17),
        ("Off-Topic",          "off-topic",     "Anything else — memes, life, random chatter.",             "🌐", "#6b7280", 18),
    ]
    for name, slug, desc, icon, color, sort in ALL_CATS:
        conn.execute(
            """INSERT OR IGNORE INTO forum_categories (name, slug, description, icon, color, sort_order)
               VALUES (?,?,?,?,?,?)""",
            (name, slug, desc, icon, color, sort)
        )
    conn.commit()
    print("[DB] Forum categories synced")

    # ── Seed forum topics & posts ──────────────────────────────────────────────
    # ── Seed forum topics (INSERT OR IGNORE by title so re-runs are safe) ─────────
    admin_id = conn.execute("SELECT id FROM users WHERE role='admin'").fetchone()
    if admin_id:
        aid = admin_id["id"]
        ALL_TOPICS = [
            # (cat_slug, title, body, pinned, locked)
            ("general", "Forum Rules — Please Read Before Posting",
             "Welcome to the RESPAWN News Forum!\n\nThese rules exist to keep this community fun, safe, and valuable for everyone. Please read them before posting.\n\nRule 1 — Be Respectful\nTreat every member with respect. No personal attacks, insults, harassment, or hate speech of any kind. Disagreements are fine; abuse is not.\n\nRule 2 — Stay On Topic\nPost in the right category. A PC gaming question belongs in PC Gaming, not General. Off-topic posts will be moved or removed.\n\nRule 3 — No Spam or Self-Promotion\nDo not post the same topic multiple times. Unsolicited ads, referral links, or promotional content will be removed.\n\nRule 4 — Tag Spoilers\nWrap story spoilers in [SPOILER][/SPOILER] tags. Respect that not everyone finishes games at the same pace.\n\nRule 5 — No Piracy or Illegal Content\nLinks to ROMs, cracked games, warez, or any illegal content will result in an immediate ban. No exceptions.\n\nRule 6 — English in Main Categories\nPlease post in English in all categories except Off-Topic. This helps moderators keep the community safe and readable.\n\nRule 7 — Don't Feed Trolls\nIf someone is breaking the rules, use the report button — don't engage. Responding to trolls escalates situations.\n\nRule 8 — No Account Sharing\nEach account represents one person. Shared accounts may be banned if suspicious activity is detected.\n\nPunishments range from a warning for first-time minor offences to a permanent ban for serious or repeated violations.\n\nThank you for being part of RESPAWN. Game on!", 1, 1),

            ("general", "Welcome to the RESPAWN Forum! Introduce yourself",
             "Hey RESPAWN community! Drop a reply and introduce yourself.\n\nTell us:\n- What platforms do you game on?\n- What's your all-time favourite game?\n- What are you playing right now?\n\nI'll start: Admin here — been gaming since the NES days. Currently hooked on Half-Life 3 and DK Bananza. Welcome aboard everyone!", 1, 0),

            ("general", "What game has the BEST story of all time?",
             "I've been thinking about this a lot lately. For me it has to be The Last of Us Part I. The emotional weight of that game is unmatched.\n\nBut plenty of people swear by Red Dead Redemption 2, or the entire Mass Effect trilogy. Some say Disco Elysium. What do you think — what game has the best story ever written?", 0, 0),

            ("general", "Your current gaming setup — share pics and specs!",
             "Always love seeing how people set up their battle stations. Share your current setup!\n\nMine: RTX 4060, 32GB RAM, 4K 144Hz monitor, DualSense Edge on the couch setup. Recently added LED strips behind the desk and it looks amazing at night.", 0, 0),

            ("general", "Most disappointing game of 2026 so far?",
             "We've had some great releases but also some seriously disappointing ones. What let you down the most this year?\n\nI was hyped for Avowed and while it was good it felt too short and too safe. Didn't blow me away the way I hoped it would.", 0, 0),

            ("playstation", "Stellar Blade 2 — better than the original?",
             "Just finished Stellar Blade 2 and the combat is so much tighter than the first game. The boss fights are genuinely some of the best I've played this generation.\n\nDoes anyone else think it surpasses the original? I think it does — by a good margin.", 0, 0),

            ("playstation", "PS5 Pro — worth upgrading from the base PS5?",
             "I have a launch PS5 and I'm seriously debating the Pro upgrade. The performance mode improvements are supposed to be incredible but the price tag is steep.\n\nHas anyone made the jump? Is it worth it for someone who games 2–3 hours a day? Would love some real-world impressions.", 0, 0),

            ("xbox", "Game Pass — still the best value in gaming?",
             "With Fable launching on Game Pass day one I genuinely think it's the best deal in gaming right now. Hundreds of games for the price of a single AAA title per month.\n\nHas Game Pass completely changed how you approach buying games? I haven't bought a full-price Xbox game in over a year.", 0, 0),

            ("nintendo", "Mario Kart World — which track is your favourite?",
             "Just unlocked all the cups in Mario Kart World and Nintendo absolutely delivered. Some of these tracks are the most creative in the entire series history.\n\nFavourite track so far? Mine is the Cybercity circuit at night — the lighting and music are incredible.", 0, 0),

            ("pc", "Half-Life 3 — living up to 18 years of hype?",
             "I finished Half-Life 3 in one sitting yesterday. 14 hours straight. No regrets whatsoever.\n\nValve absolutely delivered. The ending left me completely stunned. I genuinely think it might be the greatest FPS ever made.\n\nNo spoilers please — just want to know: who else has finished it and what do you think?", 0, 0),

            ("pc", "Best gaming mice in 2026 — what are you using?",
             "Looking to upgrade. My old Logitech G502 is finally giving up after years of faithful service.\n\nWhat are you all using? I mainly play competitive FPS so precision and low weight are key. Budget around $80–100. Any recommendations appreciated!", 0, 0),

            ("esports", "T1 three-peat — greatest dynasty in LoL history?",
             "After Worlds 2026 I genuinely believe T1 is the greatest dynasty in competitive League of Legends history. Three consecutive World Championships is something no one thought possible.\n\nFaker is the GOAT, full stop. Is there any argument against this at this point?", 0, 0),

            ("mobile", "Pokemon TCG Pocket Season 2 — new cards are broken",
             "The new Scarlet/Violet set in TCG Pocket Season 2 is completely broken. Some of these new ex cards are destroying ladder left and right.\n\nFavourite new card? The new Charizard ex art is gorgeous but the Mewtwo reprint feels way too powerful for the format.", 0, 0),

            ("vr-ar", "Is VR finally going mainstream in 2026?",
             "With PSVR3 announced and Apple Vision Pro 2 shipping, 2026 might be the year VR actually crosses into the mainstream.\n\nI've been a VR skeptic for years but after trying a PSVR3 demo last week I'm genuinely impressed. The resolution and comfort are on another level compared to earlier headsets.\n\nWhat do you think — is this finally VR's moment?", 0, 0),

            ("retro", "What's your most nostalgic game and why?",
             "Retro gaming is having a massive renaissance right now and I'm here for it.\n\nFor me it's Banjo-Kazooie on the N64. The music, the worlds, the humour — it holds up perfectly even today.\n\nWhat game instantly takes you back? Doesn't have to be ancient — even PS3/360 era counts as retro to some people now!", 0, 0),

            ("gamedev", "What engine are you building your game in?",
             "Whether you're a hobbyist or working on a commercial project, engine choice matters a lot.\n\nI'm building a 2D metroidvania in Godot 4 and loving it. The GDScript workflow is incredibly fast and the 2D tools are excellent.\n\nWhat engine are you using and what type of game are you making? Share your projects!", 0, 0),

            ("tech", "RTX 5090 vs RTX 6090 — is it worth waiting?",
             "If you're building a new PC right now the RTX 5090 is obviously the king — but the RTX 6090 Ti leaks look absolutely insane. Rumoured to double the 5090's performance at 4K.\n\nIs it worth waiting 6–12 months for the 6090 Ti or just build now with the 5090? What would you do?", 0, 0),

            ("deals", "Best gaming deals this week — post them here!",
             "This thread is for sharing the best gaming deals you find. Anything goes — Steam sales, console store discounts, physical game deals, hardware bundles, Game Pass offers, whatever.\n\nI'll start: Hollow Knight is currently 50% off on Steam. If you haven't played it yet, there is no excuse at this price.", 0, 0),

            ("lfg", "Looking for ranked teammates — post your game and rank here",
             "This is the official LFG (Looking for Group) thread. Post your game, your rank/skill level, your timezone, and what you're looking for.\n\nFormat:\nGame: [game name]\nRank: [rank or skill level]\nTimezone: [timezone]\nLooking for: [what type of player/team]\n\nI'll start:\nGame: Valorant\nRank: Platinum 2\nTimezone: EST\nLooking for: Chill duo/trio for ranked grind, 18+", 0, 0),

            ("sports", "Champions League 2026 — who wins it?",
             "The Champions League is down to the last 8 and the bracket is absolutely stacked this year.\n\nMy prediction: Real Madrid vs Manchester City in the final again — but this time City finally win it with their new striker partnership.\n\nWho do you have winning it? And who's been the biggest surprise of the tournament so far?", 0, 0),

            ("movies-tv", "Most anticipated movie of the rest of 2026?",
             "We're halfway through 2026 and the back half of the year looks stacked for cinema.\n\nI'm most excited for the new Nolan film — the trailer looked absolutely incredible and the practical effects look insane.\n\nWhat film are you most looking forward to for the rest of the year? Can be anything — blockbuster, indie, horror, whatever.", 0, 0),

            ("music", "Best video game soundtrack of all time?",
             "Game soundtracks don't get enough credit as proper musical art. Some of the most creative composition of the last 30 years has been in games.\n\nMy pick: Nier: Automata by Keiichi Okabe. The way the music reacts to gameplay and the choral work is unlike anything else.\n\nWhat's your pick for the greatest video game soundtrack ever made?", 0, 0),

            ("anime", "Best anime of 2026 so far?",
             "2026 has been a fantastic year for anime. We've had some incredible new seasons and some surprise new IPs that came out of nowhere.\n\nFor me the standout so far is the new Dungeon Meshi season — the production quality is through the roof and the story just keeps getting better.\n\nWhat's been your favourite watch of the year so far? New seasons or new series both count.", 0, 0),

            ("off-topic", "What are you watching on Netflix/streaming right now?",
             "Taking a short break from gaming to catch up on TV. Just finished Dune: Prophecy Season 2 and it was phenomenal.\n\nWhat are you watching? Doesn't matter what platform — Netflix, Disney+, HBO, whatever. Any genre. Always looking for recommendations!", 0, 0),

            # ── Additional topics (2 per category) ─────────────────────────────
            ("general", "Games you regret NOT playing sooner",
             "We all have that one game everyone was raving about for years that we finally played and kicked ourselves for waiting so long.\n\nMine was Hollow Knight. Bought it in a sale, sat in my library for 2 years. Played it. Finished it in a week. Immediately regretted not playing it sooner.\n\nWhat's your 'why did I wait so long?' game?", 0, 0),

            ("general", "Hot take thread — unpopular gaming opinions welcome",
             "No judgement here. Share your hottest gaming takes.\n\nI'll start: escort missions get too much hate. Some of the best tension in gaming comes from protecting someone. The RE4 Ashley sections are great and I will die on this hill.", 0, 0),

            ("playstation", "PSVR3 — first impressions and must-play titles",
             "Finally got my hands on a PSVR3 this week. The leap in clarity over PSVR2 is massive — text is actually readable now.\n\nBeat Saber still slaps. But the killer app for me is the new Astro Bot VR experience. Absolutely mind-blowing in full VR.\n\nWho else has one? What are you playing?", 0, 0),

            ("playstation", "PlayStation exclusives ranked — best to worst this gen",
             "After 5+ years of PS5, let's rank the exclusives properly.\n\nMy tier list:\nS: Demon's Souls, Returnal, Spider-Man 2, Stellar Blade\nA: Ratchet & Clank: Rift Apart, Ghost of Tsushima Director's Cut\nB: Sackboy, Miles Morales\nC: Destruction AllStars\n\nFight me in the replies.", 0, 0),

            ("xbox", "Xbox exclusives — where did it all go wrong?",
             "I'm an Xbox fan but I have to be honest — the exclusive lineup has been underwhelming since Halo Infinite.\n\nFable looks promising and The Outer Worlds 2 has me hyped. But compared to PlayStation exclusives, Microsoft has fallen way behind.\n\nAm I being too harsh? What Xbox exclusives are you actually excited about?", 0, 0),

            ("xbox", "Game Pass vs PlayStation Plus — which is genuinely better value in 2026?",
             "Both subscription services have matured a lot. Game Pass Ultimate now includes EA Play and day-one first-party titles. PS Plus Extra has a massive back-catalogue.\n\nCrunching the numbers and the value per game — which one wins? I've had both and I keep coming back to Game Pass just for the day-one titles.", 0, 0),

            ("nintendo", "Nintendo Switch 2 hidden gems — what are you sleeping on?",
             "Everyone knows the big titles but what Switch 2 games are underrated or overlooked?\n\nI'm putting forward Baten Kaitos Remastered and also Penny's Big Breakaway. Both criminally ignored.\n\nWhat Switch 2 games do you wish more people were talking about?", 0, 0),

            ("nintendo", "The Legend of Zelda — ranking every mainline game",
             "With Echoes of Wisdom fresh in memory and the Tears of the Kingdom hype still going, it's time for a definitive Zelda ranking thread.\n\nMy top 3: Majora's Mask, Breath of the Wild, Link to the Past — in that order.\n\nWhere does Tears of the Kingdom land in your rankings?", 0, 0),

            ("pc", "PC Gaming in 2026 — is the cost still worth it?",
             "Building a PC has never been more expensive. A mid-range 1440p build now costs around $1,500. Consoles look better value than ever on paper.\n\nBut then you have modding, backward compatibility, mouse + keyboard precision, and the freedom to upgrade piece by piece.\n\nIs PC gaming still worth the premium in 2026?", 0, 0),

            ("pc", "Recommend me a good single-player RPG on PC — no open world fatigue",
             "I love RPGs but I'm burnt out on 100+ hour open worlds. Looking for something focused — maybe 25–40 hours, strong story, no filler.\n\nAlready played: Disco Elysium, Planescape Torment, Baldur's Gate 3, Mass Effect trilogy.\n\nWhat do you recommend?", 0, 0),

            ("esports", "Best esports player of all time — who gets your vote?",
             "Faker for League. s1mple for CS. Serral for StarCraft. Daigo for FGC. N0tail for Dota.\n\nEvery game has its GOAT but who is THE greatest esports player ever across all disciplines?\n\nArgue for your pick in the replies — skill ceiling, longevity, and impact on the scene all count.", 0, 0),

            ("esports", "Esports salaries in 2026 — are players being paid fairly?",
             "Top tier esports players are now earning comparable to traditional athletes. Faker's estimated earnings are north of $10M/year when including endorsements.\n\nBut mid-tier players in smaller orgs are still making less than minimum wage in some cases.\n\nHow do you think esports handles player compensation? Is the ecosystem sustainable?", 0, 0),

            ("mobile", "Best free-to-play mobile games that aren't pay-to-win",
             "The mobile market is flooded with predatory monetisation but there are genuine gems if you know where to look.\n\nMy picks: Brawl Stars (generous F2P), Legends of Kingdom Rush, and Vampire Survivors Mobile.\n\nWhat F2P mobile games do you actually enjoy without spending money?", 0, 0),

            ("mobile", "Mobile vs handheld — Switch 2 vs playing on your phone",
             "With Switch 2 out there and phones getting more powerful every year, the handheld market feels like it's at a crossroads.\n\nDo you prefer dedicated handheld gaming or is your phone enough? I switched from carrying a Switch to just using my phone with a Razer Kishi and honestly — it works.", 0, 0),

            ("vr-ar", "Best VR games to show sceptics — what converts people instantly",
             "Every time I put a friend in a VR headset for the first time I want to pick the perfect game to blow their mind.\n\nBeat Saber always works. Half-Life: Alyx gets gasps. Walking on a plank in a skyscraper in Richie's Plank Experience terrifies everyone.\n\nWhat's your go-to demo game to convert VR sceptics?", 0, 0),

            ("retro", "Emulation in 2026 — is it preservation or piracy?",
             "The legal grey area around emulation keeps getting murkier. Nintendo's ongoing war against emulators. The Internet Archive's legal battles. Preservation vs profit.\n\nI believe strongly that emulation of orphaned software is digital preservation. Games that can't be bought legally shouldn't be locked away forever.\n\nWhere do you stand?", 0, 0),

            ("gamedev", "Show off your in-progress game — screenshots and WIPs welcome",
             "This is the thread for RESPAWN's indie developers and hobbyists to share what they're working on.\n\nScreenshots, concept art, playable demos, design questions — all welcome. We're a supportive community here.\n\nI'll start: working on a procedurally generated dungeon crawler in Godot 4. Finally got the room-connection algorithm working properly after three weeks of wrestling with it.", 0, 0),

            ("tech", "Monitor buying guide 2026 — 1440p vs 4K vs OLED",
             "Picked up a new monitor last month and the choices are overwhelming right now. 1440p 240Hz, 4K 144Hz, 4K OLED, ultrawide — all at different price points.\n\nFor gaming, I ended up going 1440p 240Hz and I have zero regrets. The high refresh rate matters more to me than the extra resolution.\n\nWhat setup are you running and what would you recommend?", 0, 0),

            ("deals", "Free games right now — Epic, PS Plus, Game Pass, Prime Gaming",
             "Let's keep this thread updated with all the free games available right now across platforms.\n\nThis week:\n- Epic: Control Ultimate Edition (free until Sunday)\n- PS Plus Monthly: Sifu and Rollerdrome\n- Game Pass new additions: Fable and Avowed\n- Prime Gaming: Rogue Legacy 2\n\nAdd what you find in the replies!", 0, 0),

            ("lfg", "Minecraft server looking for builders and survival players",
             "We have a small but active RESPAWN community Minecraft server running a custom modpack. Mostly survival with some light RPG mods.\n\nLooking for 5–10 more active players who want to build something great together. Server runs 24/7, no PvP unless consented, friendly community.\n\nDrop your Discord below if you're interested and I'll send you the invite.", 0, 0),

            ("sports", "Formula 1 2026 — new engine rules changing everything?",
             "The new F1 engine regulations coming in 2026 are the biggest rule change in a decade. More electrical power, different fuel mix, new turbo architecture.\n\nWith Red Bull's dominance finally cracking, could this level the field? I'm genuinely excited. A proper title fight between 4 or 5 teams would be incredible after years of one-team domination.", 0, 0),

            ("movies-tv", "Best video game adaptations ever made — ranked",
             "The Fallout show set a new standard. The Last of Us Season 2 delivered. Even the Sonic movies are somehow good.\n\nWe're in a golden age of gaming adaptations. But what's the best one ever made?\n\nMy ranking: Fallout S1 > Last of Us S1 > Arcane > Detective Pikachu > Castlevania.\n\nWhat's your order?", 0, 0),

            ("music", "Artists you discovered through gaming",
             "Games have introduced me to so much music I'd never have found otherwise.\n\nRed Dead Redemption 2 got me into bluegrass. Persona series got me into Japanese pop and jazz fusion. Tony Hawk's Pro Skater basically wrote my teenage soundtrack.\n\nWhat artists or genres did you first hear through a video game?", 0, 0),

            ("anime", "Manga you wish had a proper anime adaptation",
             "So many incredible manga have never gotten a proper anime — or got a rushed, low-budget version that didn't do them justice.\n\nTop of my list: Berserk needs a proper modern adaptation that covers the entire arc. The 1997 anime was great but it barely scratches the surface.\n\nWhat manga are you waiting for someone to adapt properly?", 0, 0),

            ("off-topic", "What's everyone's job outside of gaming?",
             "Curious about who's behind the usernames here. What do you do for work?\n\nI'm a secondary school PE teacher by day, aspiring indie dev by night. Gaming and teaching kids sport oddly share a lot of the same design principles when you think about it.\n\nDrop what you do in the replies — no need to be specific if you'd rather keep it vague!", 0, 0),
        ]
        inserted_topics = 0
        for cat_slug, title, body, pinned, locked in ALL_TOPICS:
            cat_row = conn.execute("SELECT id FROM forum_categories WHERE slug=?", (cat_slug,)).fetchone()
            if not cat_row:
                continue
            cat_id = cat_row["id"]
            # Only insert if a topic with this exact title doesn't already exist in this category
            exists = conn.execute(
                "SELECT id FROM forum_topics WHERE category_id=? AND title=?", (cat_id, title)
            ).fetchone()
            if exists:
                continue
            cur2 = conn.execute(
                """INSERT INTO forum_topics (category_id, title, user_id, username, post_count, pinned, locked)
                   VALUES (?,?,?,?,1,?,?)""",
                (cat_id, title, aid, "admin", pinned, locked)
            )
            topic_id = cur2.lastrowid
            conn.execute(
                "INSERT INTO forum_posts (topic_id, user_id, username, body) VALUES (?,?,?,?)",
                (topic_id, aid, "admin", body)
            )
            inserted_topics += 1
        if inserted_topics:
            conn.commit()
            print(f"[DB] Seeded {inserted_topics} new forum topics")

    conn.close()
    print(f"[DB] Initialized at {DB_PATH}")


# ── Password helpers ──────────────────────────────────────────────────────────

def hash_password(password: str) -> str:
    salt = secrets.token_hex(16)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 200_000)
    return f"{salt}${dk.hex()}"


def verify_password(password: str, stored: str) -> bool:
    try:
        salt, dk_hex = stored.split("$")
        dk = hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 200_000)
        return secrets.compare_digest(dk.hex(), dk_hex)
    except Exception:
        return False


# ── Auth queries ──────────────────────────────────────────────────────────────

def register_user(username: str, email: str, password: str):
    """Returns (user_dict, error_str)."""
    conn = get_conn()
    try:
        pw_hash = hash_password(password)
        conn.execute(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            (username.strip(), email.strip().lower(), pw_hash),
        )
        conn.commit()
        row = conn.execute(
            "SELECT id, username, email, role FROM users WHERE email = ?",
            (email.strip().lower(),),
        ).fetchone()
        return dict(row), None
    except sqlite3.IntegrityError as e:
        msg = str(e)
        if "username" in msg:
            return None, "Username already taken"
        if "email" in msg:
            return None, "Email already registered"
        return None, "Registration failed"
    finally:
        conn.close()


def login_user(email: str, password: str):
    """Returns (token, user_dict, error_str)."""
    conn = get_conn()
    try:
        row = conn.execute(
            "SELECT * FROM users WHERE email = ?",
            (email.strip().lower(),),
        ).fetchone()
        if not row:
            return None, None, "Invalid email or password"
        if not verify_password(password, row["password"]):
            return None, None, "Invalid email or password"

        token = secrets.token_hex(32)
        conn.execute(
            "INSERT INTO sessions (token, user_id) VALUES (?, ?)",
            (token, row["id"]),
        )
        conn.commit()
        user = {
            "id":       row["id"],
            "username": row["username"],
            "email":    row["email"],
            "role":     row["role"],
            "avatar":   row["avatar"] if "avatar" in row.keys() else "",
        }
        return token, user, None
    finally:
        conn.close()


def get_user_by_token(token: str):
    """Returns user dict or None."""
    if not token:
        return None
    conn = get_conn()
    try:
        row = conn.execute(
            """SELECT u.id, u.username, u.email, u.role, u.avatar
               FROM sessions s JOIN users u ON s.user_id = u.id
               WHERE s.token = ?""",
            (token,),
        ).fetchone()
        return dict(row) if row else None
    finally:
        conn.close()


def update_user_profile(user_id: int, data: dict):
    """Update email, avatar, and optionally password. Returns (user_dict, error_str)."""
    conn = get_conn()
    try:
        existing = conn.execute(
            "SELECT * FROM users WHERE id = ?", (user_id,)
        ).fetchone()
        if not existing:
            return None, "User not found"
        ex = dict(existing)

        new_email  = (data.get("email") or ex["email"]).strip().lower()
        new_avatar = data.get("avatar", ex.get("avatar", ""))
        new_pw     = data.get("new_password", "").strip()
        cur_pw     = data.get("current_password", "").strip()

        # Validate email format
        if "@" not in new_email:
            return None, "Invalid email address"

        # Check email uniqueness if changed
        if new_email != ex["email"]:
            clash = conn.execute(
                "SELECT id FROM users WHERE email = ? AND id != ?", (new_email, user_id)
            ).fetchone()
            if clash:
                return None, "Email already in use"

        # Password change
        if new_pw:
            if len(new_pw) < 6:
                return None, "New password must be at least 6 characters"
            if not cur_pw:
                return None, "Current password is required to set a new one"
            if not verify_password(cur_pw, ex["password"]):
                return None, "Current password is incorrect"
            pw_hash = hash_password(new_pw)
        else:
            pw_hash = ex["password"]

        conn.execute(
            "UPDATE users SET email = ?, avatar = ?, password = ? WHERE id = ?",
            (new_email, new_avatar, pw_hash, user_id),
        )
        conn.commit()

        row = conn.execute(
            "SELECT id, username, email, role, avatar FROM users WHERE id = ?", (user_id,)
        ).fetchone()
        return dict(row), None
    except sqlite3.IntegrityError:
        return None, "Email already in use"
    except Exception as e:
        return None, str(e)
    finally:
        conn.close()


def logout_user(token: str):
    conn = get_conn()
    try:
        conn.execute("DELETE FROM sessions WHERE token = ?", (token,))
        conn.commit()
    finally:
        conn.close()


# ── Article helpers ───────────────────────────────────────────────────────────

def _row_to_article(row) -> dict:
    d = dict(row)
    d["featured"] = bool(d["featured"])
    d.setdefault("body", "")
    d.setdefault("image_position", "center center")
    return d


# ── Article queries ───────────────────────────────────────────────────────────

def get_all_articles(limit: int = None, offset: int = 0):
    conn = get_conn()
    try:
        total = conn.execute("SELECT COUNT(*) FROM articles").fetchone()[0]
        if limit is not None:
            rows = conn.execute(
                "SELECT * FROM articles ORDER BY id DESC LIMIT ? OFFSET ?",
                (limit, offset),
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT * FROM articles ORDER BY id DESC"
            ).fetchall()
        return [_row_to_article(r) for r in rows], total
    finally:
        conn.close()


def get_articles_by_category(category: str, limit: int = None, offset: int = 0):
    conn = get_conn()
    try:
        total = conn.execute(
            "SELECT COUNT(*) FROM articles WHERE lower(category) = lower(?)",
            (category,),
        ).fetchone()[0]
        if limit is not None:
            rows = conn.execute(
                "SELECT * FROM articles WHERE lower(category) = lower(?) ORDER BY id DESC LIMIT ? OFFSET ?",
                (category, limit, offset),
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT * FROM articles WHERE lower(category) = lower(?) ORDER BY id DESC",
                (category,),
            ).fetchall()
        return [_row_to_article(r) for r in rows], total
    finally:
        conn.close()


def get_featured_articles():
    conn = get_conn()
    try:
        rows = conn.execute(
            "SELECT * FROM articles WHERE featured = 1 ORDER BY id DESC"
        ).fetchall()
        return [_row_to_article(r) for r in rows]
    finally:
        conn.close()


def get_article_by_id(article_id: int):
    conn = get_conn()
    try:
        row = conn.execute(
            "SELECT * FROM articles WHERE id = ?", (article_id,)
        ).fetchone()
        return _row_to_article(row) if row else None
    finally:
        conn.close()


def create_article(data: dict):
    """Returns (article_dict, error_str)."""
    conn = get_conn()
    try:
        cur = conn.execute(
            """INSERT INTO articles
               (category, tag, tag_class, headline, summary, author, date, score, image, featured, body, image_position)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                data.get("category", ""),
                data.get("tag", ""),
                data.get("tag_class", "tag-pc"),
                data.get("headline", ""),
                data.get("summary", ""),
                data.get("author", ""),
                data.get("date", ""),
                data.get("score"),
                data.get("image", ""),
                1 if data.get("featured") else 0,
                data.get("body", ""),
                data.get("image_position", "center center"),
            ),
        )
        conn.commit()
        row = conn.execute(
            "SELECT * FROM articles WHERE id = ?", (cur.lastrowid,)
        ).fetchone()
        return _row_to_article(row), None
    except Exception as e:
        return None, str(e)
    finally:
        conn.close()


def update_article(article_id: int, data: dict):
    """Returns (article_dict, error_str)."""
    conn = get_conn()
    try:
        existing = conn.execute(
            "SELECT * FROM articles WHERE id = ?", (article_id,)
        ).fetchone()
        if not existing:
            return None, "Article not found"
        ex = dict(existing)
        conn.execute(
            """UPDATE articles
               SET category=?, tag=?, tag_class=?, headline=?, summary=?,
                   author=?, date=?, score=?, image=?, featured=?, body=?, image_position=?
               WHERE id=?""",
            (
                data.get("category",       ex["category"]),
                data.get("tag",            ex["tag"]),
                data.get("tag_class",      ex["tag_class"]),
                data.get("headline",       ex["headline"]),
                data.get("summary",        ex["summary"]),
                data.get("author",         ex["author"]),
                data.get("date",           ex["date"]),
                data.get("score",          ex["score"]),
                data.get("image",          ex["image"]),
                1 if data.get("featured", ex["featured"]) else 0,
                data.get("body",           ex.get("body", "")),
                data.get("image_position", ex.get("image_position", "center center")),
                article_id,
            ),
        )
        conn.commit()
        row = conn.execute(
            "SELECT * FROM articles WHERE id = ?", (article_id,)
        ).fetchone()
        return _row_to_article(row), None
    except Exception as e:
        return None, str(e)
    finally:
        conn.close()


def delete_article(article_id: int):
    """Returns (success_bool, error_str)."""
    conn = get_conn()
    try:
        result = conn.execute(
            "DELETE FROM articles WHERE id = ?", (article_id,)
        )
        conn.commit()
        if result.rowcount == 0:
            return False, "Article not found"
        return True, None
    except Exception as e:
        return False, str(e)
    finally:
        conn.close()


# ── Comment queries ───────────────────────────────────────────────────────────

def delete_comment(comment_id: int):
    """Admin delete — removes comment and its replies. Returns (success_bool, error_str)."""
    conn = get_conn()
    try:
        result = conn.execute(
            "DELETE FROM comments WHERE id = ?", (comment_id,)
        )
        conn.commit()
        if result.rowcount == 0:
            return False, "Comment not found"
        return True, None
    except Exception as e:
        return False, str(e)
    finally:
        conn.close()


def delete_comment_by_user(comment_id: int, user_id: int, is_admin: bool):
    """Owner or admin delete. Returns (success_bool, error_str)."""
    conn = get_conn()
    try:
        row = conn.execute("SELECT user_id FROM comments WHERE id = ?", (comment_id,)).fetchone()
        if not row:
            return False, "Comment not found"
        if not is_admin and row["user_id"] != user_id:
            return False, "You can only delete your own comments"
        conn.execute("DELETE FROM comments WHERE id = ?", (comment_id,))
        conn.commit()
        return True, None
    except Exception as e:
        return False, str(e)
    finally:
        conn.close()


def edit_comment(comment_id: int, user_id: int, new_body: str):
    """Owner edit. Returns (comment_dict, error_str)."""
    conn = get_conn()
    try:
        row = conn.execute("SELECT * FROM comments WHERE id = ?", (comment_id,)).fetchone()
        if not row:
            return None, "Comment not found"
        if row["user_id"] != user_id:
            return None, "You can only edit your own comments"
        conn.execute("UPDATE comments SET body = ? WHERE id = ?", (new_body, comment_id))
        conn.commit()
        updated = conn.execute(
            """SELECT c.*, u.avatar,
                      COALESCE(SUM(CASE WHEN v.vote=1  THEN 1 ELSE 0 END),0) AS likes,
                      COALESCE(SUM(CASE WHEN v.vote=-1 THEN 1 ELSE 0 END),0) AS dislikes
               FROM comments c
               LEFT JOIN users u         ON c.user_id   = u.id
               LEFT JOIN comment_votes v ON c.id        = v.comment_id
               WHERE c.id = ?
               GROUP BY c.id""",
            (comment_id,),
        ).fetchone()
        return dict(updated), None
    except Exception as e:
        return None, str(e)
    finally:
        conn.close()


# ── Vote helpers ──────────────────────────────────────────────────────────────

def vote_comment(comment_id: int, user_id: int, vote: int):
    """
    vote: 1 = like, -1 = dislike, 0 = remove vote.
    Returns (likes, dislikes, user_vote, error_str).
    """
    conn = get_conn()
    try:
        # Verify comment exists
        row = conn.execute("SELECT id FROM comments WHERE id = ?", (comment_id,)).fetchone()
        if not row:
            return None, None, None, "Comment not found"

        if vote == 0:
            conn.execute(
                "DELETE FROM comment_votes WHERE comment_id = ? AND user_id = ?",
                (comment_id, user_id),
            )
        else:
            conn.execute(
                """INSERT INTO comment_votes (comment_id, user_id, vote)
                   VALUES (?, ?, ?)
                   ON CONFLICT(comment_id, user_id) DO UPDATE SET vote = excluded.vote""",
                (comment_id, user_id, vote),
            )
        conn.commit()

        counts = conn.execute(
            """SELECT
                 SUM(CASE WHEN vote = 1  THEN 1 ELSE 0 END) AS likes,
                 SUM(CASE WHEN vote = -1 THEN 1 ELSE 0 END) AS dislikes
               FROM comment_votes WHERE comment_id = ?""",
            (comment_id,),
        ).fetchone()
        likes    = counts["likes"]    or 0
        dislikes = counts["dislikes"] or 0

        uv = conn.execute(
            "SELECT vote FROM comment_votes WHERE comment_id = ? AND user_id = ?",
            (comment_id, user_id),
        ).fetchone()
        user_vote = uv["vote"] if uv else 0

        return likes, dislikes, user_vote, None
    except Exception as e:
        return None, None, None, str(e)
    finally:
        conn.close()


def get_comments(article_id: int) -> list:
    """Returns top-level comments with nested replies, each with vote counts."""
    conn = get_conn()
    try:
        rows = conn.execute(
            """SELECT c.id, c.article_id, c.user_id, c.username, c.body,
                      c.parent_id, c.created, u.avatar,
                      COALESCE(SUM(CASE WHEN v.vote = 1  THEN 1 ELSE 0 END), 0) AS likes,
                      COALESCE(SUM(CASE WHEN v.vote = -1 THEN 1 ELSE 0 END), 0) AS dislikes
               FROM comments c
               LEFT JOIN users u          ON c.user_id    = u.id
               LEFT JOIN comment_votes v  ON c.id         = v.comment_id
               WHERE c.article_id = ?
               GROUP BY c.id
               ORDER BY c.created ASC""",
            (article_id,),
        ).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def get_user_votes(article_id: int, user_id: int) -> dict:
    """Returns {comment_id: vote} for all comments the user voted on in this article."""
    conn = get_conn()
    try:
        rows = conn.execute(
            """SELECT cv.comment_id, cv.vote
               FROM comment_votes cv
               JOIN comments c ON cv.comment_id = c.id
               WHERE c.article_id = ? AND cv.user_id = ?""",
            (article_id, user_id),
        ).fetchall()
        return {row["comment_id"]: row["vote"] for row in rows}
    finally:
        conn.close()


def add_comment(article_id: int, user_id: int, username: str, body: str, parent_id=None):
    """Returns (comment_dict, error_str)."""
    conn = get_conn()
    try:
        cur = conn.execute(
            """INSERT INTO comments (article_id, user_id, username, body, parent_id)
               VALUES (?, ?, ?, ?, ?)""",
            (article_id, user_id, username, body.strip(), parent_id),
        )
        conn.commit()
        row = conn.execute(
            """SELECT c.*, u.avatar,
                      0 AS likes, 0 AS dislikes
               FROM comments c
               LEFT JOIN users u ON c.user_id = u.id
               WHERE c.id = ?""",
            (cur.lastrowid,),
        ).fetchone()
        return dict(row), None
    except Exception as e:
        return None, str(e)
    finally:
        conn.close()


# ── Forum queries ─────────────────────────────────────────────────────────────

def get_forum_categories():
    conn = get_conn()
    try:
        rows = conn.execute(
            """SELECT fc.*, COUNT(ft.id) AS topic_count
               FROM forum_categories fc
               LEFT JOIN forum_topics ft ON ft.category_id = fc.id
               GROUP BY fc.id ORDER BY fc.sort_order"""
        ).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def get_forum_topics(category_slug=None, page=1, per_page=20):
    conn = get_conn()
    offset = (page - 1) * per_page
    try:
        if category_slug:
            cat = conn.execute(
                "SELECT id FROM forum_categories WHERE slug=?", (category_slug,)
            ).fetchone()
            if not cat:
                return [], 0
            rows = conn.execute(
                """SELECT ft.*, u.avatar
                   FROM forum_topics ft
                   LEFT JOIN users u ON ft.user_id = u.id
                   WHERE ft.category_id=?
                   ORDER BY ft.pinned DESC, ft.last_post_at DESC
                   LIMIT ? OFFSET ?""",
                (cat["id"], per_page, offset)
            ).fetchall()
            total = conn.execute(
                "SELECT COUNT(*) FROM forum_topics WHERE category_id=?", (cat["id"],)
            ).fetchone()[0]
        else:
            rows = conn.execute(
                """SELECT ft.*, u.avatar
                   FROM forum_topics ft
                   LEFT JOIN users u ON ft.user_id = u.id
                   ORDER BY ft.pinned DESC, ft.last_post_at DESC
                   LIMIT ? OFFSET ?""",
                (per_page, offset)
            ).fetchall()
            total = conn.execute("SELECT COUNT(*) FROM forum_topics").fetchone()[0]
        return [dict(r) for r in rows], total
    finally:
        conn.close()


def get_forum_topic(topic_id: int):
    conn = get_conn()
    try:
        topic = conn.execute(
            """SELECT ft.*, fc.name AS category_name, fc.slug AS category_slug,
                      fc.icon AS category_icon, u.avatar
               FROM forum_topics ft
               JOIN forum_categories fc ON ft.category_id = fc.id
               LEFT JOIN users u ON ft.user_id = u.id
               WHERE ft.id=?""",
            (topic_id,)
        ).fetchone()
        if not topic:
            return None, []
        conn.execute("UPDATE forum_topics SET view_count = view_count + 1 WHERE id=?", (topic_id,))
        conn.commit()
        posts = conn.execute(
            """SELECT fp.*, u.avatar,
                      (SELECT COUNT(*) FROM forum_posts fp2 WHERE fp2.user_id = fp.user_id) AS user_post_count
               FROM forum_posts fp
               LEFT JOIN users u ON fp.user_id = u.id
               WHERE fp.topic_id=?
               ORDER BY fp.created ASC""",
            (topic_id,)
        ).fetchall()
        return dict(topic), [dict(p) for p in posts]
    finally:
        conn.close()


def create_forum_topic(category_slug: str, title: str, body: str, user_id: int, username: str):
    conn = get_conn()
    try:
        cat = conn.execute(
            "SELECT id FROM forum_categories WHERE slug=?", (category_slug,)
        ).fetchone()
        if not cat:
            return None, "Category not found"
        cur = conn.execute(
            """INSERT INTO forum_topics (category_id, title, user_id, username, post_count)
               VALUES (?,?,?,?,1)""",
            (cat["id"], title.strip(), user_id, username)
        )
        topic_id = cur.lastrowid
        conn.execute(
            "INSERT INTO forum_posts (topic_id, user_id, username, body) VALUES (?,?,?,?)",
            (topic_id, user_id, username, body.strip())
        )
        conn.commit()
        topic = conn.execute("SELECT * FROM forum_topics WHERE id=?", (topic_id,)).fetchone()
        return dict(topic), None
    except Exception as e:
        return None, str(e)
    finally:
        conn.close()


def create_forum_post(topic_id: int, body: str, user_id: int, username: str):
    conn = get_conn()
    try:
        topic = conn.execute(
            "SELECT id, locked FROM forum_topics WHERE id=?", (topic_id,)
        ).fetchone()
        if not topic:
            return None, "Topic not found"
        if topic["locked"]:
            return None, "This topic is locked"
        conn.execute(
            "INSERT INTO forum_posts (topic_id, user_id, username, body) VALUES (?,?,?,?)",
            (topic_id, user_id, username, body.strip())
        )
        conn.execute(
            """UPDATE forum_topics SET post_count=post_count+1,
               last_post_at=datetime('now') WHERE id=?""",
            (topic_id,)
        )
        conn.commit()
        row = conn.execute(
            """SELECT fp.*, u.avatar FROM forum_posts fp
               LEFT JOIN users u ON fp.user_id=u.id
               WHERE fp.rowid=last_insert_rowid()"""
        ).fetchone()
        return dict(row), None
    except Exception as e:
        return None, str(e)
    finally:
        conn.close()


def toggle_forum_post_like(post_id: int, user_id: int):
    conn = get_conn()
    try:
        existing = conn.execute(
            "SELECT 1 FROM forum_post_likes WHERE post_id=? AND user_id=?",
            (post_id, user_id)
        ).fetchone()
        if existing:
            conn.execute(
                "DELETE FROM forum_post_likes WHERE post_id=? AND user_id=?",
                (post_id, user_id)
            )
            conn.execute(
                "UPDATE forum_posts SET likes=likes-1 WHERE id=?", (post_id,)
            )
            liked = False
        else:
            conn.execute(
                "INSERT INTO forum_post_likes (post_id, user_id) VALUES (?,?)",
                (post_id, user_id)
            )
            conn.execute(
                "UPDATE forum_posts SET likes=likes+1 WHERE id=?", (post_id,)
            )
            liked = True
        conn.commit()
        likes = conn.execute(
            "SELECT likes FROM forum_posts WHERE id=?", (post_id,)
        ).fetchone()["likes"]
        return {"liked": liked, "likes": likes}, None
    except Exception as e:
        return None, str(e)
    finally:
        conn.close()


def delete_forum_post(post_id: int, user_id: int, is_admin: bool):
    conn = get_conn()
    try:
        post = conn.execute(
            "SELECT user_id, topic_id FROM forum_posts WHERE id=?", (post_id,)
        ).fetchone()
        if not post:
            return "Post not found"
        if not is_admin and post["user_id"] != user_id:
            return "Forbidden"
        topic_id = post["topic_id"]
        conn.execute("DELETE FROM forum_posts WHERE id=?", (post_id,))
        conn.execute(
            "UPDATE forum_topics SET post_count=MAX(0,post_count-1) WHERE id=?",
            (topic_id,)
        )
        conn.commit()
        return None
    except Exception as e:
        return str(e)
    finally:
        conn.close()


def get_forum_stats():
    conn = get_conn()
    try:
        topics = conn.execute("SELECT COUNT(*) FROM forum_topics").fetchone()[0]
        posts  = conn.execute("SELECT COUNT(*) FROM forum_posts").fetchone()[0]
        users  = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
        return {"topics": topics, "posts": posts, "members": users}
    finally:
        conn.close()


def get_user_forum_post_count(user_id: int) -> int:
    conn = get_conn()
    try:
        return conn.execute(
            "SELECT COUNT(*) FROM forum_posts WHERE user_id=?", (user_id,)
        ).fetchone()[0]
    finally:
        conn.close()


def get_hot_forum_topics(limit: int = 5) -> list:
    """Score = post_count*5 + view_count + recency_bonus. Excludes pinned topics."""
    conn = get_conn()
    try:
        rows = conn.execute(
            """SELECT ft.*,
                      fc.name  AS category_name,
                      fc.icon  AS category_icon,
                      fc.slug  AS category_slug,
                      (ft.post_count * 5 + ft.view_count +
                       CASE
                         WHEN ft.last_post_at >= datetime('now', '-3 days')  THEN 100
                         WHEN ft.last_post_at >= datetime('now', '-7 days')  THEN 60
                         WHEN ft.last_post_at >= datetime('now', '-30 days') THEN 20
                         ELSE 0
                       END) AS hot_score
               FROM forum_topics ft
               JOIN forum_categories fc ON ft.category_id = fc.id
               WHERE ft.pinned = 0
               ORDER BY hot_score DESC, ft.post_count DESC
               LIMIT ?""",
            (limit,)
        ).fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def get_forum_rules_topic_id() -> int | None:
    """Returns the ID of the pinned locked rules topic."""
    conn = get_conn()
    try:
        row = conn.execute(
            "SELECT id FROM forum_topics WHERE pinned=1 AND locked=1 ORDER BY id LIMIT 1"
        ).fetchone()
        return row["id"] if row else None
    finally:
        conn.close()
