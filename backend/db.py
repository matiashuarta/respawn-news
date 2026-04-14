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
                   (category, tag, tag_class, headline, summary, author, date, score, image, featured, body)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (
                    a["category"], a["tag"], a["tag_class"],
                    a["headline"], a["summary"], a["author"],
                    a["date"], a.get("score"), a["image"],
                    1 if a.get("featured") else 0,
                    a.get("body", ""),
                ),
            )
        conn.commit()
        print(f"[DB] Seeded {len(news_data.ARTICLES)} articles")
    else:
        # ── Patch existing articles: fix Nintendo images & fill body text ──────
        import news_data
        patched = 0
        inserted = 0
        for a in news_data.ARTICLES:
            row = conn.execute(
                "SELECT image, body FROM articles WHERE id = ?", (a["id"],)
            ).fetchone()
            if not row:
                # New article added to seed data — insert it
                conn.execute(
                    """INSERT INTO articles
                       (id, category, tag, tag_class, headline, summary, author, date, score, image, featured, body)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (
                        a["id"], a["category"], a["tag"], a["tag_class"],
                        a["headline"], a["summary"], a["author"],
                        a["date"], a.get("score"), a["image"],
                        1 if a.get("featured") else 0,
                        a.get("body", ""),
                    ),
                )
                inserted += 1
                continue
            new_image = a["image"]
            new_body  = a.get("body", "")
            old_image = row["image"]
            old_body  = row["body"] or ""
            needs_update = (old_image != new_image) or (not old_body and new_body)
            if needs_update:
                conn.execute(
                    "UPDATE articles SET image = ?, body = ? WHERE id = ?",
                    (new_image, new_body if not old_body else old_body, a["id"]),
                )
                patched += 1
        if inserted:
            conn.commit()
            print(f"[DB] Inserted {inserted} new seed articles")
        if patched:
            conn.commit()
            print(f"[DB] Patched {patched} articles (images/body)")

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
    return d


# ── Article queries ───────────────────────────────────────────────────────────

def get_all_articles():
    conn = get_conn()
    try:
        rows = conn.execute(
            "SELECT * FROM articles ORDER BY id DESC"
        ).fetchall()
        return [_row_to_article(r) for r in rows]
    finally:
        conn.close()


def get_articles_by_category(category: str):
    conn = get_conn()
    try:
        rows = conn.execute(
            "SELECT * FROM articles WHERE lower(category) = lower(?) ORDER BY id DESC",
            (category,),
        ).fetchall()
        return [_row_to_article(r) for r in rows]
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
               (category, tag, tag_class, headline, summary, author, date, score, image, featured, body)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
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
                   author=?, date=?, score=?, image=?, featured=?, body=?
               WHERE id=?""",
            (
                data.get("category",  ex["category"]),
                data.get("tag",       ex["tag"]),
                data.get("tag_class", ex["tag_class"]),
                data.get("headline",  ex["headline"]),
                data.get("summary",   ex["summary"]),
                data.get("author",    ex["author"]),
                data.get("date",      ex["date"]),
                data.get("score",     ex["score"]),
                data.get("image",     ex["image"]),
                1 if data.get("featured", ex["featured"]) else 0,
                data.get("body",      ex.get("body", "")),
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
