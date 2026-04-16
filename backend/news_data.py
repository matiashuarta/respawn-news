"""
news_data.py — Seed articles for RESPAWN News.
Auto-managed: run  python backend/sync_seed.py  after changing images or
content via the admin panel, then commit the result to keep the repo in sync.
"""

ARTICLES = [

    {
        "id": 1, "category": """PlayStation""",
        "tag": """PS5""", "tag_class": """tag-ps""",
        "headline": """Ghost of Yōtei — First Gameplay Revealed at State of Play""",
        "summary": """Sucker Punch Productions unveiled 12 minutes of open-world gameplay set in 1603 Hokkaido. The sequel doubles down on exploration and introduces Atsu, a revenge-driven female protagonist navigating feudal Japan.""",
        "author": """Camila Reyes""", "date": """Apr 12, 2026""",
        "score": None,
        "image": """https://www.screenhub.com.au/wp-content/uploads/sites/4/2025/09/ghost-of-yotei-game-review.jpg""",
        "image_position": """50% 19%""",
        "featured": True,
        "body": """Sucker Punch Productions took center stage at Sony's April State of Play, delivering a stunning 12-minute gameplay showcase for Ghost of Yōtei, the long-anticipated follow-up to Ghost of Tsushima. Set in 1603 Hokkaido against the backdrop of the Edo period's turbulent dawn, the game introduces Atsu — a ronin driven by vengeance after her clan is slaughtered by a ruthless warlord. The demo showcased the vast, snow-dusted plains of Hokkaido, dense cedar forests, and a fishing village rife with political tension.

Combat feels distinctly evolved from its predecessor. Atsu wields a curved tachi with fluid precision, and the new "Phantom Stance" mechanic lets her exploit an enemy's emotional state — fear, rage, grief — to unlock devastating finishing moves. Dual-wielding short blades returns as an option mid-fight, and for the first time players can command a small band of allied ronin in scripted ambushes.

The open world itself appears considerably larger than Tsushima, with a full day-night cycle influencing NPC behaviour and patrol patterns. Sucker Punch confirmed a robust side-quest system built around Hokkaido's Ainu indigenous culture, promising authentic consultation with historians and cultural advisors throughout development. Ghost of Yōtei is confirmed for PS5 and PC, with a release window of Q4 2026.""",
    },
    {
        "id": 2, "category": """PlayStation""",
        "tag": """Review""", "tag_class": """tag-ps""",
        "headline": """Death Stranding 2 Review — 9.2 / 10""",
        "summary": """Kojima's magnum opus returns with richer traversal, a bolder narrative, and a seamless online world. The strand genre finally feels fully realized in this breathtaking sequel.""",
        "author": """Lena Park""", "date": """Apr 10, 2026""",
        "score": 9.2,
        "image": """https://cdn.mos.cms.futurecdn.net/jxiEQwnU3namcMBAguRYCW.jpg""",
        "image_position": """52% 44%""",
        "featured": False,
        "body": """Death Stranding 2: On the Beach is the rare sequel that does the impossible — it makes you question why the original ever felt incomplete. Hideo Kojima has returned with a game that is simultaneously more accessible and more daring, trimming the repetitive early trudge of its predecessor while expanding the strand-based online ecosystem into something genuinely moving. Sam Bridges is back, haunted and hardwired, delivering cargo across a world still stitched together by invisible threads of human connection.

The traversal systems have been overhauled significantly. Vehicles feel heavier and more purposeful; rope mechanics now allow vertical traversal across cliffsides and flooded ruins; and the BT encounters have been reimagined as full-scale set pieces rather than tense tip-toeing. The narrative — wild, ambitious, occasionally impenetrable — lands its emotional punches far more consistently this time, anchored by career-best performances from Norman Reedus and a scene-stealing new cast member we'll leave nameless.

What elevates Death Stranding 2 above the pack is its online world. Seeing a stranger's bridge still standing from months ago, or a ladder left precisely where you needed one — it creates a form of empathy rarely found in games. This is Kojima's magnum opus, and it demands to be experienced.""",
    },
    {
        "id": 3, "category": """PlayStation""",
        "tag": """PS5 Pro""", "tag_class": """tag-ps""",
        "headline": """PS5 Pro Slim Announced — Smaller, Cheaper, Same Power""",
        "summary": """Sony confirms a redesigned PS5 Pro Slim model launching this November at $449. It drops the optical drive but adds 2 TB of internal storage and a new neural rendering chip.""",
        "author": """Marco Vidal""", "date": """Apr 8, 2026""",
        "score": None,
        "image": """https://images.unsplash.com/photo-1607853202273-797f1c22a38e?w=900&q=80""",
        "image_position": """center center""",
        "featured": False,
        "body": """Sony has officially unveiled the PS5 Pro Slim, a redesigned mid-generation console targeting players who want Pro-tier performance at a more approachable price point. Announced at $449 — $50 less than the standard PS5 Pro at launch — the Slim model is roughly 30% smaller in volume and ships without an optical drive, following the same disc-free strategy that proved popular with the PS5 Slim. The trade-off is negligible for most players, Sony argues, given the PlayStation Store's maturity.

The headline addition is the new Neural Rendering Accelerator (NRA) chip co-developed with TSMC, which Sony claims can double frame-rate stability in demanding ray-traced titles by intelligently predicting and reconstructing frames. Early tech demos shown to press reportedly demonstrated Demon's Souls running at a locked 120fps with full RT reflections enabled — a feat the standard PS5 Pro manages only inconsistently. Internal storage jumps to 2 TB SSD, addressing one of the most common complaints about the existing hardware.

Sony also confirmed a revised DualSense controller bundled with the unit: the DualSense Edge Slim, featuring replaceable stick modules as standard — previously an Edge-exclusive feature. The PS5 Pro Slim launches November 14, 2026, and will be available in Midnight Black and Cosmic White colourways.""",
    },
    {
        "id": 4, "category": """PlayStation""",
        "tag": """Exclusive""", "tag_class": """tag-ps""",
        "headline": """Naughty Dog's 'Project Sable' — Sci-Fi RPG Leaked""",
        "summary": """Internal documents suggest Naughty Dog is deep in production on a science-fiction RPG codenamed Project Sable. Insiders describe it as Naughty Dog's most ambitious title, with a fully simulated alien ecosystem.""",
        "author": """Camila Reyes""", "date": """Apr 5, 2026""",
        "score": None,
        "image": """https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=900&q=80""",
        "image_position": """center center""",
        "featured": False,
        "body": """A series of leaked internal documents circulating through verified industry sources paint a fascinating picture of Naughty Dog's next project — codenamed Project Sable — a departure from the cinematic action-adventure formula the studio built its reputation on. According to the materials, Sable is a third-person science-fiction RPG set on an uncharted exoplanet teeming with procedurally simulated alien life. The documents describe a "living ecosystem engine" where predators hunt prey in real-time, weather patterns shift habitats, and player actions create cascading consequences across the world.

The protagonist is described as a xenobiologist stranded after a colonial ship crash, forced to form alliances with indigenous alien species to survive and eventually uncover the truth behind the mission's sabotage. Branching dialogue, skill trees tied to specific alien communication methods, and non-lethal stealth mechanics all feature prominently. Notably, the documents suggest a strong influence from Disco Elysium's dialogue philosophy — morally ambiguous, deeply researched, written with literary ambition.

Naughty Dog has declined to comment. PlayStation Studios boss Hermen Hulst, when pressed at a recent investor call, said only that the studio is "working on something we're incredibly proud of." Given the scope described in the leak, a reveal before end of 2026 seems unlikely — but anticipation is sky-high.""",
    },
    {
        "id": 5, "category": """PlayStation""",
        "tag": """Spider-Man""", "tag_class": """tag-ps""",
        "headline": """Marvel's Spider-Man 2 — 'Black Suit' DLC Drops This Summer""",
        "summary": """Insomniac Games announced a 6-hour story expansion featuring Peter Parker's symbiote arc as a standalone narrative, launching July 18 exclusively on PS5.""",
        "author": """Lena Park""", "date": """Apr 3, 2026""",
        "score": None,
        "image": """https://media.es.wired.com/photos/6532dfa71f09c12d4e468444/master/pass/8-Tips-to-Get-Started-with-Marvel's-Spider-Man-2-Culture.jpg""",
        "image_position": """59% 21%""",
        "featured": False,
        "body": """Insomniac Games has announced a substantial paid story expansion for Marvel's Spider-Man 2 titled Black Suit, arriving July 18 exclusively on PS5. The DLC focuses entirely on Peter Parker during the period immediately after the Venom defeat — specifically the psychological aftermath of symbiote bonding, exploring the residual corruption left in Peter's psyche. Insomniac describes it as a "self-contained narrative" lasting approximately six hours, roughly the length of a standalone film.

The expansion introduces two new districts of New York built for the DLC, a revamped combat system for the Black Suit incorporating rage-fuelled abilities distinct from the base game's symbiote moveset, and a new villain not featured in the original release. Insomniac has been tight-lipped on villain identity, though a pre-release teaser image showing a cracked white mask has sent the community into speculation overdrive.

Existing Marvel's Spider-Man 2 owners will receive the expansion at $24.99, while a new Complete Edition bundling the base game and DLC will launch simultaneously at $79.99. Insomniac also confirmed that a free update accompanying the DLC will add New Game Plus and the Photo Mode enhancements long requested by the community. Pre-orders open April 15.""",
    },
    {
        "id": 6, "category": """PlayStation""",
        "tag": """God of War""", "tag_class": """tag-ps""",
        "headline": """God of War: Valhalla 2 Confirmed — Norse Saga Continues""",
        "summary": """Santa Monica Studio officially confirms a sequel to the free Valhalla expansion, this time branching into Egyptian mythology. Kratos and a new companion embark on an intercultural pantheon odyssey.""",
        "author": """Marco Vidal""", "date": """Mar 30, 2026""",
        "score": None,
        "image": """https://ca-times.brightspotcdn.com/dims4/default/d4fb01a/2147483647/strip/true/crop/3840x2160+0+0/resize/1200x675!/quality/75/?url=https%3A%2F%2Fcalifornia-times-brightspot.s3.amazonaws.com%2F89%2F0e%2F83ba54707c1db5b1bc744d6efd05%2F03198d04bd6d41aaa2d7767427270e96""",
        "image_position": """54% 31%""",
        "featured": False,
        "body": """Santa Monica Studio has officially confirmed God of War: Valhalla 2, the follow-up to 2023's beloved free roguelite expansion. Unlike its predecessor, Valhalla 2 is a full premium release — a standalone title within the God of War universe that serves as a bridge between the Norse and Egyptian mythological arcs. The announcement was accompanied by a cinematic trailer showing Kratos and a new companion, Naret — a disgraced Egyptian emissary of Ra — navigating a liminal realm where Norse and Egyptian afterlives converge in violent collision.

The game takes direct inspiration from Egyptian mythology's concept of the Duat, the underworld through which Ra's sun barque travels each night. Santa Monica has committed to the same cultural rigour that distinguished the Norse trilogy: full consultation with Egyptologists, collaboration with Egyptian creative consultants, and authentic integration of hieroglyphic scripture into environmental storytelling. Combat previews shown at GDC 2026 hint at a completely new weapon — the Khopesh of Osiris — alongside Kratos's Blades of Chaos.

Valhalla 2 is confirmed as a PS5 and PC simultaneous release, with no cross-generation support — Santa Monica wants to build exclusively for current-gen hardware. A release window of Spring 2027 has been mentioned in passing by studio director Cory Barlog, though nothing official has been committed.""",
    },
    {
        "id": 7, "category": """PlayStation""",
        "tag": """PSVR3""", "tag_class": """tag-ps""",
        "headline": """PSVR3 Officially Teased — Wireless, Eye-Tracked, $349""",
        "summary": """Sony's next-gen VR headset is officially in the pipeline. A short teaser shows a sleek wireless design with foveated rendering powered by eye-tracking — targeting a Q1 2027 launch at $349.""",
        "author": """Camila Reyes""", "date": """Mar 27, 2026""",
        "score": None,
        "image": """https://images.unsplash.com/photo-1593508512255-86ab42a8e620?w=900&q=80""",
        "image_position": """center center""",
        "featured": False,
        "body": """Sony has broken its silence on the next generation of PlayStation VR with an official teaser for PSVR3, confirming the headset is real, wireless, and coming in Q1 2027 at a $349 launch price. The 40-second teaser revealed a dramatically slimmer profile than PSVR2 — closer in silhouette to a pair of oversized ski goggles than a traditional VR headset — and highlighted two headline features: full eye-tracking and foveated rendering.

Foveated rendering, which renders only the area directly in focus at full resolution while downscaling peripheral vision, is the critical enabler here. Sony's documentation accompanying the teaser claims PSVR3 can render its display at an effective 8K equivalent resolution by concentrating pixel density exactly where the eye is looking at any given moment. This dramatically reduces the GPU load on PS5, making wireless operation viable without sacrificing visual fidelity.

The controller situation remains unclear — the teaser showed no peripherals — though Sony filed patents earlier this year for a glove-style haptic input device. Pricing at $349 undercuts Meta Quest 3 at launch and positions PSVR3 as the most accessible dedicated console VR headset to date. A full reveal event is expected at PlayStation's summer showcase.""",
    },
    {
        "id": 8, "category": """PlayStation""",
        "tag": """Review""", "tag_class": """tag-ps""",
        "headline": """Gran Turismo 8 Review — 9.0 / 10""",
        "summary": """Polyphony Digital delivers the definitive racing simulator. Gran Turismo 8 stuns with ray-traced reflections at 60fps, a revised physics engine, and 500 meticulously crafted cars at launch.""",
        "author": """Marco Vidal""", "date": """Mar 22, 2026""",
        "score": 9.0,
        "image": """https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=900&q=80""",
        "image_position": """center center""",
        "featured": False,
        "body": """Gran Turismo 8 is Polyphony Digital's most complete entry in the franchise's 28-year history, and in many respects it is the simulator that GT7 promised but couldn't quite deliver. Five hundred cars at launch — each modelled with forensic attention, down to correct tyre deformation under lateral load — racing across 47 circuits, with a track-building editor that surpasses anything in the genre. The headline achievement is sustained 60fps with full ray-traced reflections enabled on PS5 Pro hardware; standard PS5 runs at a rock-solid 60fps in rasterised mode.

The revised physics engine is the real story. Polyphony has worked directly with tyre manufacturers to simulate compound behaviour under temperature change, meaning cold tyres genuinely behave differently from warm ones. Brake fade is modelled at the disc level. Kerb geometry can unsettle a car's balance mid-corner in ways that feel authentic rather than punitive. It is demanding, but the new extensive Driving School mode makes mastery feel achievable for newcomers.

Career mode remains Gran Turismo's weakest link — it's a structured but soulless march through licences and manufacturer cups — but the online Sport Mode, now featuring a fully fledged live-service calendar with weekly manufacturer challenges, is where Gran Turismo 8 truly lives. This is the benchmark for racing simulation on console.""",
    },
    {
        "id": 9, "category": """Xbox""",
        "tag": """Xbox Series X""", "tag_class": """tag-xbox""",
        "headline": """Fable — Release Date Set for October 14, 2026""",
        "summary": """Microsoft finally locks in October 14 for the long-awaited Fable reboot. Playground Games promises a comedic open-world RPG with 60+ hours of content, dynamic hero reputation, and the most colorful version of Albion ever seen.""",
        "author": """James O'Brien""", "date": """Apr 11, 2026""",
        "score": None,
        "image": """https://static0.dualshockersimages.com/wordpress/wp-content/uploads/2026/01/fable-finally-launching-this-fall-along-with-a-new-complex-morality-system.png""",
        "image_position": """50% 79%""",
        "featured": True,
        "body": """After nearly a decade of anticipation, Microsoft has confirmed that Fable arrives on Xbox Series X|S, PC, and Game Pass on October 14, 2026. Playground Games — the studio behind Forza Horizon's vibrant open worlds — is making its RPG debut with what it describes as a "love letter and a reimagining" of Peter Molyneux's beloved franchise. The announcement was accompanied by an extended gameplay showcase lasting 20 minutes, revealing the world of Albion in extraordinary, painterly detail.

The new Albion is an island nation in a vaguely industrial-era Britain, soaked in warm colour and populated by characters who seem to have stepped directly out of a Terry Pratchett novel. The tone is comedic but with genuine stakes — Playground has spoken extensively about wanting to balance the whimsy of the originals with a story that actually resonates emotionally. Hero reputation returns in evolved form: your choices ripple not just through how NPCs react to you, but through the physical landscape of towns and wilderness over time.

Combat blends melee, ranged, and spellcasting in an action-RPG style closer to Dragon's Dogma than the original Fable's deliberate pacing. A "Renown" system tracks legendary status across three distinct in-world cultures, unlocking unique questlines and cosmetic rewards. Fable will be one of the largest games Playground has ever shipped, with Forza Horizon's open-world DNA unmistakably present in every corner of Albion.""",
    },
    {
        "id": 10, "category": """Xbox""",
        "tag": """Game Pass""", "tag_class": """tag-xbox""",
        "headline": """Game Pass Ultimate Gets 14 New Day-One Titles in Q2 2026""",
        "summary": """Microsoft's subscription lineup grows again, with 14 first- and third-party games launching directly into Game Pass Ultimate this quarter, including Fable, Contraband, and Perfect Dark.""",
        "author": """Sarah Thompson""", "date": """Apr 9, 2026""",
        "score": None,
        "image": """https://images.unsplash.com/photo-1621259182978-fbf93132d53d?w=900&q=80""",
        "image_position": """center center""",
        "featured": False,
        "body": """Microsoft has revealed the Q2 2026 Game Pass Ultimate content calendar, and it represents the subscription service's most stacked quarter to date. Fourteen titles are confirmed as day-one additions across April, May, and June — eight of which are Xbox Game Studios first-party releases. Headlining the quarter is, of course, Fable in October, but the earlier months carry serious weight too. Contraband from Avalanche Studios launches in May directly into Game Pass, ending years of near-silence from the open-world co-op heist game. Perfect Dark from The Initiative — after its turbulent multi-year development — is confirmed for June.

Third-party highlights include a major JRPG from NamcoBandai, two AA indie titles from ID@Xbox partners, and a surprise addition of a remastered classic from a major Japanese publisher. Microsoft has also expanded the Game Pass library with backwards compatibility improvements, adding 23 Xbox 360 titles with updated resolution and HDR.

For console subscribers, the PC Game Pass parity update — long requested — means all 14 day-one titles will be simultaneously available on Windows. Microsoft's CFO confirmed in a recent earnings call that Game Pass now exceeds 45 million subscribers globally, with Ultimate tier growth outpacing the base tier three-to-one. The value proposition continues to be unmatched in the subscription gaming space.""",
    },
    {
        "id": 11, "category": """Xbox""",
        "tag": """Review""", "tag_class": """tag-xbox""",
        "headline": """Avowed Review — 8.4 / 10""",
        "summary": """Obsidian's first-person RPG delivers a tight story, exceptional world-building, and meaningful choices — even if the combat feels a touch shallow late-game. Fans of Pillars of Eternity will find it irresistible.""",
        "author": """David Kim""", "date": """Apr 6, 2026""",
        "score": 8.4,
        "image": """https://sm.ign.com/ign_es/gallery/a/avowed-gam/avowed-gamescom-2024-screenshots_jduc.jpg""",
        "image_position": """51% 100%""",
        "featured": False,
        "body": """Obsidian Entertainment's Avowed is a first-person RPG set in the Living Lands — a volatile island region on the fringe of the Pillars of Eternity world — and it is, without qualification, the best game Obsidian has made since The Outer Worlds. That's not faint praise: Avowed is a confident, beautifully realised RPG that puts writing and worldbuilding first, and largely succeeds in making the Living Lands feel like a place with history, contradictions, and a soul.

The story casts you as an envoy from the Aedyran Empire investigating a mysterious plague consuming the island's population. The five-act structure is economical and satisfying, and crucially, your choices meaningfully alter the political landscape by the credits — not in the Bioware checkbox fashion but in ways that emerge organically from the factions you cultivate. Companion writing is exceptional; every party member earns both your trust and your scepticism at some point.

Where Avowed stumbles is in its combat, particularly in the back half. The dual-wield and magic systems feel electric early on, but enemies scale awkwardly and the encounter design grows repetitive across longer play sessions. A more varied bestiary and smarter enemy AI would have elevated this from great to unmissable. As it stands, Avowed is a must-play for Pillars fans and a compelling showcase of what Obsidian can achieve with full Xbox Game Studios backing.""",
    },
    {
        "id": 12, "category": """Xbox""",
        "tag": """Hardware""", "tag_class": """tag-xbox""",
        "headline": """Xbox Series X 2 — Specs Leak Points to Massive GPU Leap""",
        "summary": """An internal Microsoft document allegedly reveals the next Xbox will feature AMD's RDNA 5 GPU targeting native 8K at 60fps for first-party titles, plus a unified memory architecture with 32 GB GDDR7.""",
        "author": """James O'Brien""", "date": """Apr 3, 2026""",
        "score": None,
        "image": """https://i.extremetech.com/imagery/content-types/017bzo4irDqcCFc33nVjdhN/hero-image.fit_lim.v1678673290.jpg""",
        "image_position": """50% 50%""",
        "featured": False,
        "body": """A document purportedly originating from Microsoft's Xbox hardware division has been circulating among verified hardware journalists, and if authentic, it paints an extraordinary picture of the next Xbox console — internally referred to as "Project Aries." The headline specification is an AMD RDNA 5 GPU rated at approximately 24 teraflops, more than double the Xbox Series X's 12 TF, designed to target native 8K at 60fps for first-party optimised titles and 4K at 120fps for third-party games.

Perhaps more significant than raw GPU power is the memory architecture. The document describes 32 GB of unified GDDR7 memory — shared between CPU and GPU — with a bandwidth figure that would represent a generational leap over current unified memory solutions. This would allow substantially larger game worlds to exist entirely in memory, reducing load times to near-zero and eliminating the texture streaming hitches that still plague current-gen open-world games.

The document also references a new custom SSD controller achieving read speeds above 10 GB/s, compared to the Series X's already-fast 2.4 GB/s. Microsoft has not commented on the leak. Analysts note that the specifications align with manufacturing timelines for a late-2027 or 2028 announcement, with a 2029 launch being the most plausible window given TSMC's current production roadmap for RDNA 5.""",
    },
    {
        "id": 13, "category": """Xbox""",
        "tag": """Halo""", "tag_class": """tag-xbox""",
        "headline": """Halo: The Endless War — 343 Industries Teases New Entry""",
        "summary": """343 Industries dropped a cryptic 90-second teaser showing the Master Chief descending into an alien structure unlike anything from previous Halo entries. A full reveal is slated for Xbox Showcase 2026.""",
        "author": """Sarah Thompson""", "date": """Mar 31, 2026""",
        "score": None,
        "image": """https://static0.gamerantimages.com/wordpress/wp-content/uploads/2021/12/halo-infinite-fan-proposes-infected-armor-core-based-on-the-flood.jpg?q=49&fit=contain&w=750&h=422&dpr=2""",
        "image_position": """57% 22%""",
        "featured": False,
        "body": """343 Industries has posted a 90-second teaser for what appears to be the next mainline Halo title — subtitled The Endless War — on the franchise's official social channels, breaking two years of near-complete silence from the studio. The teaser is atmospheric and deliberately cryptic: the Master Chief descends alone through a structure that bends geometric logic, its architecture bearing no resemblance to Forerunner, Covenant, or Banished design language. The closing seconds reveal a brief glimpse of what fans are already calling "the Endless home world" — a churning, purple-black void latticed with incomprehensible machinery.

The tease arrives as 343 Industries completes an extensive internal restructuring following Halo Infinite's troubled live-service period. New studio head Pierre Hintze has spoken publicly about recentring the franchise on premium single-player experiences, with a full campaign-focused reveal planned for the Xbox Games Showcase in June 2026. Multiplayer is reportedly still part of the package, but the marketing emphasis is firmly on Master Chief's solo story for the first time since Halo 5.

Lore implications are significant. The Endless — introduced in Halo Infinite's campaign as ancient beings immune to the Halo rings' effect — have been a source of intense fan speculation since 2021. The Endless War title implies a direct confrontation with this faction at civilisation scale. Engine footage shown internally to press reportedly runs on a new build of Slipspace, rebuilt substantially from the ground up.""",
    },
    {
        "id": 14, "category": """Xbox""",
        "tag": """Forza""", "tag_class": """tag-xbox""",
        "headline": """Forza Motorsport Update 9 — Weather Overhaul & 20 New Cars""",
        "summary": """Turn 10's latest update brings a full dynamic weather system, puddle simulation, and 20 new cars including several vintage Le Mans racers, all free for current owners.""",
        "author": """David Kim""", "date": """Mar 28, 2026""",
        "score": None,
        "image": """https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/2440510/page_bg_raw.jpg?t=1747073895""",
        "image_position": """51% 85%""",
        "featured": False,
        "body": """Turn 10 Studios has shipped Forza Motorsport Update 9, the game's most substantial post-launch content drop since launch, and it transforms the racing sim in ways that should have been present from day one. The headline addition is a fully dynamic weather system: rain accumulates on track surfaces in real-time, puddles form based on circuit topography and drainage modelling, spray from competitors affects visibility at speed, and drying lines emerge over several laps as tyres clear the standing water. It is, by a considerable margin, the most technically impressive weather system in a console racing title.

Twenty new cars arrive free with the update, spread across eras and categories. The vintage Le Mans contingent is the standout addition — six endurance racers from the 1960s through 1980s, including two cars never before seen in any Forza title, each rebuilt from factory blueprints sourced directly from manufacturer archives. These vintage machines require a fundamentally different approach to racing: pre-downforce aerodynamics, mechanical drum brakes, and period-correct tyre compounds that punish modern driving lines.

Turn 10 has also addressed several longstanding community requests in the same update: the Career mode has been expanded with a dedicated Historic Racing series, the Drivatars AI has received a tuning pass to reduce the aggressive ramming behaviour, and a full photo mode overhaul adds volumetric lighting controls and a custom backdrop system.""",
    },
    {
        "id": 15, "category": """Xbox""",
        "tag": """Indiana Jones""", "tag_class": """tag-xbox""",
        "headline": """Indiana Jones — 'The Order of Giants' DLC Revealed""",
        "summary": """MachineGames announces a massive expansion to Indiana Jones and the Great Circle, sending Indy on a new adventure through ancient Mayan ruins with a new whip combat system and two original companions.""",
        "author": """James O'Brien""", "date": """Mar 24, 2026""",
        "score": None,
        "image": """https://media.wired.com/photos/67646f02464b15abf2f2eab6/master/w_2560%2Cc_limit/Indianba-Jones-Review-Game-Culture.jpg""",
        "image_position": """58% 0%""",
        "featured": False,
        "body": """MachineGames has announced The Order of Giants, a premium story expansion for Indiana Jones and the Great Circle that sends Dr. Jones to the jungles of the Yucatán Peninsula in pursuit of a stolen Olmec artefact with catastrophic implications. The expansion was announced via a cinematic trailer that immediately drew comparisons to the tone of Raiders of the Lost Ark — tense, humorous, and genuinely adventurous rather than the more po-faced delivery of some recent franchise entries.

New to the expansion is a rebuilt whip combat system. In the base game, the whip functioned primarily as a traversal and puzzle tool; in The Order of Giants, it has been expanded into a full combat instrument. Players can now disarm enemies with precision strikes, bind multiple opponents simultaneously, and execute environmental takedowns by wrapping the whip around structural elements mid-fight. MachineGames describes it as bringing "the whip to the foreground in a way that feels true to the films."

Two original companion characters accompany Indy through the campaign: Xóchitl, a Mayan archaeologist with deep ties to the artefact, and Sergeant Kowalski, a wisecracking veteran mercenary. Both characters are voiced by original actors recorded for the DLC, and their interactions with Indy form the emotional core of the story. The Order of Giants launches May 22, priced at $29.99, with Game Pass Ultimate access included.""",
    },
    {
        "id": 16, "category": """Xbox""",
        "tag": """Review""", "tag_class": """tag-xbox""",
        "headline": """Minecraft Legends 2 Review — 7.8 / 10""",
        "summary": """The follow-up expands on the strategy-action formula with a proper campaign editor, cross-play co-op for 8 players, and a much deeper biome ecosystem. A solid sequel that learns from its predecessor's missteps.""",
        "author": """Sarah Thompson""", "date": """Mar 20, 2026""",
        "score": 7.8,
        "image": """https://www.minecraft.net/content/dam/minecraftnet/games/badger/screenshots/TU2-Update_Screenshots_Frog_Hero_1920x1080.jpg""",
        "image_position": """50% 50%""",
        "featured": False,
        "body": """Minecraft Legends 2 does something genuinely difficult: it takes an awkward first attempt at a new genre and builds something coherent and enjoyable from the wreckage. The original Minecraft Legends was a curious hybrid of action-RTS and Minecraft aesthetics that never quite committed to either identity. The sequel commits. It is leaner, more confident, and considerably more replayable.

The 12-hour campaign is the franchise's strongest narrative effort by some margin — a story of ancient grudges between three distinct civilisations, told through environmental storytelling and some genuinely affecting set pieces. The campaign editor is the sequel's standout feature: a fully featured toolset that allows players to build and share custom campaigns with scripted events, custom enemy placements, and authored dialogue. The Minecraft community's track record with creation tools suggests this will have a shelf life far beyond the game's own campaign.

Cross-play eight-player co-op in campaign and versus modes works reliably, and the biome ecosystem — with seven distinct environments each producing unique resources, factions, and tactical challenges — gives the multiplayer serious strategic depth. Where Legends 2 still trails the genre's best is in real-time combat readability; large-scale battles can collapse into visual chaos that makes tactical decision-making feel like guesswork. A respectable sequel, and a solid foundation for a potential third entry.""",
    },
    {
        "id": 17, "category": """Nintendo""",
        "tag": """Switch 2""", "tag_class": """tag-nin""",
        "headline": """Nintendo Switch 2 — Full Launch Lineup Confirmed""",
        "summary": """Nintendo announces 22 launch titles for Switch 2, headlined by Mario Kart World, a new 3D Donkey Kong adventure, and Metroid Prime 4 arriving day one. The hybrid console launches June 5 at $449.""",
        "author": """Yuki Tanaka""", "date": """Apr 12, 2026""",
        "score": None,
        "image": """https://static.fnac-static.com/multimedia/Images/ES/Comete/30961/CCP_IMG_ORIGINAL/433424.jpg""",
        "image_position": """53% 55%""",
        "featured": True,
        "body": """Nintendo has confirmed the complete launch lineup for Switch 2, and it is, by any measure, the strongest day-one software slate the company has ever shipped with a new console. Twenty-two titles will be available from June 5 — the hardware's launch date — including three major first-party games that would each independently constitute a system seller. Mario Kart World, the first open-world entry in the franchise's history, arrives day one alongside Metroid Prime 4 and a brand-new 3D platformer starring Donkey Kong in his first fully 3D adventure since the Nintendo 64 era.

Switch 2 itself represents a significant hardware leap. The larger 7.9-inch LCD display runs at 1080p docked and 720p handheld, with DLSS upscaling enabled on supported titles pushing output to 4K on a modern TV. The new Joy-Con 2 controllers feature magnetic attachment, revised analogue sticks with Hall effect sensors (addressing the Joy-Con drift that plagued the original), and a new "C Button" designed as a shortcut to the Switch 2's expanded online ecosystem.

Battery life sits at five to seven hours in handheld mode depending on title, and the system's charging architecture now supports USB-C PD at 45W, halving recharge time compared to the original Switch. At $449, Nintendo has priced Switch 2 at a premium, though a confirmed hardware bundle including Mario Kart World at $499 is already drawing significant pre-order interest.""",
    },
    {
        "id": 18, "category": """Nintendo""",
        "tag": """Review""", "tag_class": """tag-nin""",
        "headline": """Metroid Prime 4 Review — 9.7 / 10""",
        "summary": """Worth the wait. Retro Studios delivers the definitive first-person adventure: stunning alien environments, a haunting orchestral score, and some of the best boss encounters in Nintendo history.""",
        "author": """Yuki Tanaka""", "date": """Apr 9, 2026""",
        "score": 9.7,
        "image": """https://gaming-cdn.com/images/news/articles/14406/cover/1000x563/metroid-prime-4-beyond-ya-ha-sido-clasificado-en-estados-unidos-cover68a6d782a7cfb.jpg""",
        "image_position": """65% 58%""",
        "featured": False,
        "body": """Metroid Prime 4 has been in development for nine years. It has changed studios, changed engines, changed creative directors, and survived every form of development hell that a major Nintendo title can endure. The remarkable thing — the almost unreasonable thing — is that none of that shows. Metroid Prime 4 is seamless, confident, and absolutely stunning: a game that feels like it was made by a studio at the peak of its craft, with precisely the time it needed to breathe.

Retro Studios has rebuilt the Metroid Prime formula from the ground up for Switch 2, and every system has been reconsidered with fresh eyes. The scanning mechanic, so central to Prime's identity, has been expanded into a full environmental analysis tool: Samus can now detect residual thermal signatures, biological contamination trails, and structural weaknesses in ways that feed directly into exploration and combat. Visor switching has been made genuinely fluid, cycling between modes mid-combat without breaking pace. The result is a game that rewards curiosity at every turn.

The planet Ados IV — a dying gas giant whose upper atmosphere harbours a civilisation of crystalline beings — is the single most beautiful environment Retro has ever built. Across roughly 22 hours for a first playthrough, not one environment repeats a visual motif. Boss encounters are masterclasses in design: challenging, readable, and mythologically coherent with the world's lore. A score from the late Kenji Yamamoto's team haunts every corridor. Metroid Prime 4 is a genuine masterpiece.""",
    },
    {
        "id": 19, "category": """Nintendo""",
        "tag": """Mario Kart""", "tag_class": """tag-nin""",
        "headline": """Mario Kart World Hands-On — 32 Courses, Wild New Items""",
        "summary": """We went hands-on with Mario Kart World for 3 hours. The open-overworld exploration between races is a revelation, and new items like the Boo Balloon and Chain Chomp Chain completely shake up strategy.""",
        "author": """Mia Chen""", "date": """Apr 7, 2026""",
        "score": None,
        "image": """https://www.digitallydownloaded.net/wp-content/uploads/2025/06/Mario-Kart-World-Review-5.webp""",
        "image_position": """55% 63%""",
        "featured": False,
        "body": """Mario Kart World is the series' most ambitious redesign in its 33-year history, and three hours with it suggests Nintendo may have pulled off the impossible: making Mario Kart feel genuinely new without sacrificing the approachable chaos that makes it one of gaming's great social experiences. The structural change is radical — between races, players exist in an open world spanning seven themed kingdoms, each with their own atmospheric identity, hidden shortcuts, collectable Koopa Coins, and spontaneous mini-races triggered by encountering AI drivers on the road.

The 32 courses are stunningly designed. The open-world DNA bleeds into track architecture: routes now branch mid-race, with risk-reward shortcuts that swing outcomes in ways that feel fair rather than arbitrary. Anti-gravity surfaces return from Mario Kart 8 and have been expanded to include full 360-degree tunnel sections that invert the spatial logic of racing in delightful ways. Courses feel longer and more narratively structured, with environmental storytelling woven into the landscapes that players race through.

New items are where Mario Kart World gets genuinely wild. The Boo Balloon inflates your kart for five seconds, making you immune to projectiles and briefly massive — terrifying for drivers behind you. The Chain Chomp Chain, deployed from behind, latches onto the nearest competitor and drags them with you for three seconds of frantic, screaming chaos. Both feel instantly iconic. With 12-player local support and confirmed 24-player online, Mario Kart World is already shaping up to be the Switch 2's defining multiplayer title.""",
    },
    {
        "id": 20, "category": """Nintendo""",
        "tag": """Zelda""", "tag_class": """tag-nin""",
        "headline": """The Legend of Zelda: Echoes of Eternity — Fall 2026""",
        "summary": """Nintendo reveals a brand-new Zelda title for Switch 2, set in a parallel Hyrule where time flows in reverse. The game uses a new 'Echo Weaving' mechanic letting Link copy and replay any ability or environment element.""",
        "author": """Yuki Tanaka""", "date": """Apr 4, 2026""",
        "score": None,
        "image": """https://sm.mashable.com/t/mashable_sea/review/t/the-legend/the-legend-of-zelda-echoes-of-wisdom-review-princess-zelda-s_tvcg.1248.jpg""",
        "image_position": """50% 49%""",
        "featured": False,
        "body": """Nintendo has officially unveiled The Legend of Zelda: Echoes of Eternity, a brand-new Zelda title exclusive to Switch 2 targeting a Fall 2026 release. The announcement trailer is conceptually striking: a Hyrule rendered in lush, painterly strokes — reminiscent of an animated film — where the environment physically flows backwards, waterfalls ascending, crumbled ruins reassembling, autumn leaves returning to branches. Link navigates this reality in reverse, and the game's central mechanic — Echo Weaving — emerges from this premise.

Echo Weaving allows Link to observe any ability, enemy behaviour, or environmental interaction, then "echo" it: a perfect replay of that action, stored and deployable at will. An enemy charges; Link captures the charge as an Echo and uses it to break a distant barrier. A waterfall flows upward; Link echoes it to create a temporary water column for vertical traversal. The system appears to have near-infinite combinatorial potential, and Nintendo's demonstration showed solutions to puzzles that the developers themselves hadn't anticipated during playtesting.

The art direction marks the biggest visual departure for a mainline Zelda since the cel-shaded Wind Waker. Hyrule's architecture blends familiar landmarks — Death Mountain, Lake Hylia, Gerudo Canyon — with surrealist geometry that reflects the time-reversal premise. A new antagonist has not been named, though the trailer's final seconds suggest a familiar silhouette transformed in deeply unsettling ways. Echoes of Eternity is targeting a November 2026 launch.""",
    },
    {
        "id": 21, "category": """Nintendo""",
        "tag": """Pokémon""", "tag_class": """tag-nin""",
        "headline": """Pokémon Legends: Z-A — Lumiose City Reimagined in 3D""",
        "summary": """Game Freak's latest Legends entry sets the action in a fully 3D Lumiose City undergoing urban redevelopment. Players can freely roam districts, influence city planning decisions, and encounter Mega Evolutions in the wild.""",
        "author": """Mia Chen""", "date": """Apr 1, 2026""",
        "score": None,
        "image": """https://www.nintendo.com/eu/media/images/08_content_images/games_6/nintendo_switch_7/nswitch_pokemonlegendsza_1/CI_NSwitch_Pokemon_Legends_ZA_NS1_Illustration_Day.jpg""",
        "image_position": """54% 15%""",
        "featured": False,
        "body": """Pokémon Legends: Z-A is Game Freak's most technically ambitious Pokémon title to date and a significant step forward from Legends: Arceus in virtually every measurable dimension. Set in a future version of Lumiose City from Pokémon X & Y — now undergoing a massive urban redevelopment project — the game abandons the open wilderness of its predecessor in favour of a dense, vertical urban environment filled with layered districts, underground sewer ecosystems, rooftop gardens, and a sprawling central park where wild Pokémon roam freely.

The city-planning mechanic is genuinely novel for the franchise. Players accumulate influence with Lumiose's three competing development factions, each with a different vision for the city's future: an industrial conglomerate, an ecological preservation group, and a heritage society protecting historical districts. Your choices — which construction projects to support, which to sabotage, which Pokémon to capture or release — physically reshape the city over the course of the game. Districts literally look different depending on your decisions.

Mega Evolution returns as a central mechanic, discovered wild in Lumiose's deep infrastructure layers. Rather than a battle-only transformation, Mega Pokémon now roam as apex predators of their urban ecosystems — a Mega Gengar dominating the neon-lit entertainment quarter, a Mega Aerodactyl nesting in the unfinished upper scaffolding of the central tower. The shift to Switch 2 hardware is immediately visible: character models, lighting, and environment density are a generation beyond Scarlet and Violet.""",
    },
    {
        "id": 22, "category": """Nintendo""",
        "tag": """Donkey Kong""", "tag_class": """tag-nin""",
        "headline": """Donkey Kong Odyssey — DK Gets His Own 3D Adventure""",
        "summary": """Nintendo finally gives Donkey Kong his own 3D platformer. DK Odyssey features lush jungle worlds, rhythmic gameplay tied to a dynamic soundtrack, and a deep crafting system using materials from defeated enemies.""",
        "author": """Mia Chen""", "date": """Mar 28, 2026""",
        "score": None,
        "image": """https://i0.wp.com/levelup.buscafs.com/2025/07/Donkey-Kong.webp?fit=2560,1440&quality=75&strip=all""",
        "image_position": """53% 56%""",
        "featured": True,
        "body": """Donkey Kong has not starred in his own fully 3D platformer since Donkey Kong 64 in 1999 — a 27-year drought that Nintendo has finally ended with Donkey Kong Odyssey. Developed by Nintendo EPD in collaboration with Retro Studios, Odyssey does not attempt to mimic the 2D rhythm-platformer DNA of the Tropical Freeze series. Instead, it builds something entirely its own: a lush, kinetic 3D platformer structured around music as a core gameplay element.

Every world in Donkey Kong Odyssey has a living soundtrack that responds directly to DK's movement and combat. Defeating enemies in sequence builds a "Groove Meter" that, when full, temporarily transforms the environment — platforms emerge from rhythm, hazards freeze in time, collectables multiply across the stage. The crafting system built from defeated enemy materials is deeper than it first appears: DK can construct traversal tools, improvisational musical instruments that affect world state, and protective gear suited to each world's distinct environmental challenges.

The seven worlds across the game's roughly 15-hour main campaign are visually extraordinary — dense, hand-crafted jungle environments far beyond what the Switch 1 could have rendered. A Jurassic-era Primal Jungle, an Art Deco Banana Metropolis, and an Arctic Archipelago of glacial ice formations are particular standouts. Two-player co-op lets a second player control Diddy Kong with his own distinct ability set. Donkey Kong Odyssey is a confident, joyful game that proves DK can anchor a 3D platformer every bit as well as Mario.""",
    },
    {
        "id": 23, "category": """Nintendo""",
        "tag": """Mario Bros""", "tag_class": """tag-nin""",
        "headline": """Super Mario Bros. Wonder 2 — 2D Returns with Gravity Twist""",
        "summary": """Nintendo's follow-up to the acclaimed Wonder flips the script with gravity-based stages. Up to 4 players navigate worlds that rotate, flip, and collapse in real time, with 12 new Wonder Flower effects never seen before.""",
        "author": """Yuki Tanaka""", "date": """Mar 24, 2026""",
        "score": None,
        "image": """https://media.gq.com.mx/photos/69deb796e33a2e519feafd85/master/w_1600%2Cc_limit/Super_Mario_Bros_Wonder_Nintendo_Switch_2_Koopalines.jpg""",
        "image_position": """65% 5%""",
        "featured": False,
        "body": """Super Mario Bros. Wonder 2 follows its acclaimed predecessor with a central mechanic that is, if anything, even more conceptually wild: gravity manipulation. Where the original Wonder introduced the Wonder Flower as a catalyst for unexpected transformations, Wonder 2 builds its entire stage design philosophy around surfaces, ceilings, and walls becoming interchangeable. World 1-1 establishes the premise immediately — a stage that begins conventionally, then tilts 90 degrees mid-play, walls becoming floors as the entire platforming vocabulary is reshuffled.

The physics engine has been rebuilt to support this, and the result is 2D platforming that consistently wrong-foots even experienced Mario players in the best possible way. Up to four players in local co-op means gravity shifts become collaborative puzzles: one player holding a gravity anchor while another launches upward; a third carried inadvertently into a new section by a rotating platform. The emergent comedy of four-player Wonder 2 in gravity chaos stages is some of the best co-op gaming Nintendo has produced.

Twelve new Wonder Flower effects accompany the gravity system, each appearing only once per stage: a fan-favourite involves reversing only the player's personal gravity while the world remains anchored, creating a first-person experience of everything falling "up." Badge integration returns from the original, with new gravity-specific badges adding entirely new movement options. Wonder 2's six worlds across roughly 12 hours of content are dense, inventive, and — critically — never repetitive.""",
    },
    {
        "id": 24, "category": """Nintendo""",
        "tag": """Animal Crossing""", "tag_class": """tag-nin""",
        "headline": """Animal Crossing: New Horizons 2 — Switch 2 Reveal Incoming""",
        "summary": """Nintendo's financial report hints at a new Animal Crossing title in final development for Switch 2. Leakers describe it as a 'living world' with real-time seasonal weather, NPC storylines, and multiplayer islands for 16 players.""",
        "author": """Mia Chen""", "date": """Mar 20, 2026""",
        "score": None,
        "image": """https://media.wired.com/photos/5fa5be20daa25f804cdbd2d9/16:9/w_1615,h_908,c_limit/games_culture_anch-fall.jpg""",
        "image_position": """54% 33%""",
        "featured": False,
        "body": """Nintendo's Q4 2025 financial report buried a disclosure that sent the Animal Crossing community into a frenzy: a line item referencing "unannounced simulation title in final QA" within the Nintendo EPD Group 2 pipeline — the team historically responsible for Animal Crossing. Multiple reliable Nintendo leakers have since corroborated that the title is indeed the Switch 2 follow-up to New Horizons, internally codenamed "Orchid," and that a reveal is planned for Nintendo's summer Direct.

According to leaker accounts, Animal Crossing: New Horizons 2 represents the most significant evolution of the series since its inception. The "living world" designation refers to a simulated ecosystem running on Switch 2 hardware 24/7: real-time seasonal weather that changes weekly rather than monthly, NPC villagers with autonomous storylines that advance even while the player is offline, and an economy that fluctuates based on aggregate player activity across the global online network.

The headline multiplayer feature allows up to 16 players to inhabit a single island simultaneously — up from eight in New Horizons — with dedicated zones for collaborative construction projects. Leakers describe a new "town services" system where players collectively vote on island infrastructure improvements, community events, and seasonal festivals. Nintendo's silence on all fronts has been total, but given the financial disclosure and the Switch 2's launch momentum, an announcement before the end of summer seems inevitable.""",
    },
    {
        "id": 26, "category": """PC""",
        "tag": """Hardware""", "tag_class": """tag-pc""",
        "headline": """NVIDIA RTX 6090 Ti Benchmarked — Doubles RTX 5090 Performance""",
        "summary": """Early benchmark results from a verified source show the RTX 6090 Ti achieving 2× rasterization and 3× ray-tracing performance over the RTX 5090, with DLSS 5 delivering frame-perfect 8K gaming at a rumored $1,599 MSRP.""",
        "author": """Tom Bradley""", "date": """Apr 10, 2026""",
        "score": None,
        "image": """https://www.nvidia.com/content/dam/en-zz/Solutions/geforce/graphic-cards/50-series/rtx-5090/geforce-rtx-5090-learn-more-og-1200x630.jpg""",
        "image_position": """45% 100%""",
        "featured": False,
        "body": """The RTX 6090 Ti benchmark leak comes from a source with a near-perfect track record on GPU performance figures, and the numbers are staggering. In synthetic rasterisation workloads, the 6090 Ti scores approximately 2.1× the RTX 5090 — itself the fastest consumer GPU ever tested at its launch. Ray-tracing performance improvement is even more dramatic, at roughly 3.2× in full path-traced scenarios, enabled by a third generation of dedicated RT cores that Blackwell++ architecture introduces.

DLSS 5, confirmed as a 6090 Ti launch feature, represents the most significant generational leap in Nvidia's upscaling technology since DLSS 3 introduced frame generation. DLSS 5 combines full resolution reconstruction with neural frame prediction — generating not just one interpolated frame between rendered frames, but up to three — while simultaneously introducing a "pre-render" mode that reduces perceived input latency below what even a natively rendered frame can achieve. Benchmarks show effective 8K gaming at above 60fps in current-generation titles with DLSS 5 enabled.

The rumoured $1,599 MSRP is aggressive — $400 more than the RTX 5090's launch price — though analysts point out that the 6090 Ti's performance ratio versus its predecessor is significantly better than any previous xx90 Ti launch. Availability at MSRP remains the historical challenge; Nvidia's Founders Edition direct purchase programme will be the primary route for consumers hoping to avoid scalper pricing at launch.""",
    },
    {
        "id": 27, "category": """PC""",
        "tag": """Review""", "tag_class": """tag-pc""",
        "headline": """Stalker 2 Patch 1.4 Review Update — 8.9 / 10""",
        "summary": """A year of patches has transformed Stalker 2 into a masterclass in atmospheric survival horror. The Zone has never felt more alive — or more dangerous. This is now one of the best open-world games ever made.""",
        "author": """Alex Mercer""", "date": """Apr 8, 2026""",
        "score": 8.9,
        "image": """https://es.kotaku.com/app/uploads/2024/11/f4af4ade59f643e5a5e7e4aa3fd49eae.jpg""",
        "image_position": """48% 94%""",
        "featured": False,
        "body": """GSC Game World's Stalker 2: Heart of Chornobyl launched in late 2024 as a deeply ambitious but profoundly broken game. Our original review awarded it a 7.2, noting extraordinary atmosphere and world-building undermined by catastrophic technical failures. With Patch 1.4, released March 2026, we are revising that score significantly upward. The game that exists now is not the game that shipped — it is better in almost every dimension, and in some dimensions it has no equal.

The Zone in Patch 1.4 is a living system of astonishing complexity. The A-Life 2.0 AI now functions as GSC intended: mutant migration patterns shift weekly, faction warfare ebbs and flows based on resource scarcity, and anomaly fields mutate their geometry in ways that make revisited areas feel genuinely different. Encounters feel unscripted in a way that even open-world games ten times the budget rarely achieve. The emergent storytelling generated by the AI — a starving Bloodsucker raiding a military camp, a rival faction stumbling into your carefully laid ambush because they were fleeing something worse — is consistently remarkable.

Performance has stabilised to a point where a mid-range PC can maintain 60fps in the open world with good visual fidelity. The DX12 path has been optimised substantially, and stuttering — the original launch's defining technical complaint — is now occasional rather than constant. Story bugs that blocked questlines in the original version have been addressed in their entirety. Stalker 2 at Patch 1.4 is one of the best open-world games ever made.""",
    },
    {
        "id": 28, "category": """PC""",
        "tag": """Mod""", "tag_class": """tag-pc""",
        "headline": """Elden Ring 'Lands Between Expanded' Mod — 80 New Areas""",
        "summary": """The massive Elden Ring overhaul mod reaches version 2.0 with 80 handcrafted areas, 200 new enemies, a full voice-acted questline with 6 original NPCs, and a reworked invasion system for PvP enthusiasts.""",
        "author": """Tom Bradley""", "date": """Apr 5, 2026""",
        "score": None,
        "image": """https://img.redbull.com/images/c_limit,w_1500,h_1000/f_auto,q_auto/redbullcom/2022/2/8/ynu2k9yf882la76z9nxk/elden-ring-key-art""",
        "image_position": """48% 100%""",
        "featured": False,
        "body": """The Lands Between Expanded mod for Elden Ring has reached version 2.0, and in doing so has crossed a threshold that few fan-made modifications ever achieve: it is genuinely comparable in scope and craftsmanship to the game's official Shadow of the Erdtree DLC. Developed over three years by a distributed team of 34 modders — artists, programmers, quest designers, and three professional voice actors — LBE 2.0 adds 80 handcrafted areas to the Lands Between's geography, each designed with the environmental storytelling rigour that FromSoftware's world-building established.

The new areas occupy three distinct regions: the Sunken Altus, an archaeological ruin layer beneath the Altus Plateau flooded by an ancient catastrophe; the Rot Marshes of the Far East, a spiritual sibling of Caelid rendered in sickly chartreuse; and the Abyssal Shore, a coastal region at the world's physical edge where reality frays into something resembling a fever dream. All 80 areas have unique enemy placements, boss encounters — 14 original bosses, five of which are multi-phase — and environmental puzzles that feed into a central questline voiced entirely by original talent.

The 200 new enemies are designed to complement vanilla Elden Ring's combat vocabulary rather than introduce new mechanics abruptly. Six new NPCs advance a questline that intersects with Miquella's lore in ways FromSoftware themselves left deliberately unresolved — the mod's writers have made bold, well-researched lore decisions that the community has largely received as coherent with the source material.""",
    },
    {
        "id": 29, "category": """PC""",
        "tag": """Cyberpunk""", "tag_class": """tag-pc""",
        "headline": """Cyberpunk 2077 'Neon Requiem' — Final Expansion Announced""",
        "summary": """CD Projekt Red announces one final Cyberpunk 2077 story chapter introducing a new playable character and an entirely new district of Night City. Launching September 2026, 'Neon Requiem' closes V's saga for good.""",
        "author": """Alex Mercer""", "date": """Apr 2, 2026""",
        "score": None,
        "image": """https://static0.polygonimages.com/wordpress/wp-content/uploads/chorus/uploads/chorus_asset/file/22150614/ss_ae4465fa8a44dd330dbeb7992ba196c2f32cabb1.jpg?w=1600&h=900&fit=crop""",
        "image_position": """56% 52%""",
        "featured": False,
        "body": """CD Projekt Red has announced Neon Requiem, the final story expansion for Cyberpunk 2077, and with it the definitive end of V's story in Night City. The announcement was accompanied by a four-minute cinematic trailer — the most narratively suggestive marketing content the expansion has released since Phantom Liberty — showing a new protagonist, River Ward's estranged sister Dasha, navigating a freshly unveiled district of Night City called the Waterfront: a post-corporate reclamation zone where the city's homeless and displaced have built an autonomous community in the ruins of a decommissioned commercial harbour.

Neon Requiem introduces Dasha as a playable character with a distinct build philosophy from V: street-level, low-tech, and deeply human in a world of chrome excess. CDPR describes her as "Night City through uncybered eyes" — a character who survives on wit, community, and improvised hardware rather than military-grade cyberware. The Waterfront district is structurally different from Night City's other zones: vertical density gives way to horizontal sprawl, and the community's self-governance creates a faction system unlike anything in the base game.

V's story continues in parallel through the expansion's second act, with the two protagonists' narratives converging in the third. CDPR has promised resolution for several questlines left open by Phantom Liberty and commitments to "close every door we opened in 2077." Neon Requiem launches September 18, 2026, with a $34.99 price point. After this, CDPR's full focus shifts to Project Orion — Cyberpunk 2.""",
    },
    {
        "id": 30, "category": """PC""",
        "tag": """Hardware""", "tag_class": """tag-pc""",
        "headline": """Steam Deck 2 Announced — OLED, Snapdragon X Elite, 4K Dock""",
        "summary": """Valve surprises the gaming world with Steam Deck 2 featuring a 9-inch 1600p OLED screen, Snapdragon X Elite chip, 4K HDR dock, and a 4-hour battery estimate under demanding titles. Pre-orders open May 1.""",
        "author": """Tom Bradley""", "date": """Mar 30, 2026""",
        "score": None,
        "image": """https://images.unsplash.com/photo-1612287230202-1ff1d85d1bdf?w=900&q=80""",
        "image_position": """center center""",
        "featured": False,
        "body": """Valve has announced Steam Deck 2, the successor to the device that fundamentally changed the handheld PC gaming market, and the specifications are a significant generational jump. The headline upgrade is a 9-inch 1600p OLED display — brighter, more contrast-rich, and larger than the LCD OLED hybrid of the original — paired with a Snapdragon X Elite chip that Valve claims delivers "native desktop-equivalent performance in handheld mode" for the majority of the Steam library. Fan noise has been substantially reduced through a new vapour chamber cooling solution and a redesigned dual-fan configuration.

The 4K HDR Dock is the second major announcement, launching simultaneously with the hardware. The dock connects via USB 4 and enables 4K HDR output at 60fps for titles that support it, with XeSS upscaling available for games running at lower internal resolutions. Valve has worked with Intel's Display Solutions division on the dock's output pipeline, ensuring compatibility with HDMI 2.1 and DisplayPort 2.0 displays without additional configuration.

Battery life estimates of 4 hours under demanding modern titles and 7-8 hours for less intensive games are honest by handheld PC standards. Pre-orders open May 1 at $649 for the 512 GB model and $749 for the 1 TB NVMe configuration. Existing Steam Deck accessories — including thumbstick modules and carrying cases — are confirmed compatible with Steam Deck 2's revised but dimensionally similar chassis.""",
    },
    {
        "id": 31, "category": """PC""",
        "tag": """GTA 6""", "tag_class": """tag-pc""",
        "headline": """GTA 6 PC — Rockstar Confirms Day-One PC Launch""",
        "summary": """Breaking a decade-long tradition of delayed PC ports, Rockstar Games officially confirms GTA 6 will launch simultaneously on PC alongside consoles in October 2026 with full ray tracing, DLSS 5, and an unlocked frame rate.""",
        "author": """Alex Mercer""", "date": """Mar 26, 2026""",
        "score": None,
        "image": """https://i.blogs.es/763a99/gta6/840_560.jpeg""",
        "image_position": """61% 37%""",
        "featured": False,
        "body": """Rockstar Games has officially confirmed that Grand Theft Auto 6 will launch simultaneously on PC alongside PS5 and Xbox Series X|S in October 2026, breaking the studio's established tradition of delaying PC releases by 12 to 18 months. The confirmation, buried in a PC Gaming Show technical deep-dive segment, was accompanied by the first PC-specific gameplay footage — running on an RTX 6090 with DLSS 5 enabled — and the visual fidelity on display is extraordinary even by modern standards.

PC-specific features confirmed include full path-traced global illumination (ray tracing at a level beyond what consoles will offer at launch), DLSS 5 and AMD FSR 4 upscaling support, an unlocked frame rate with native 4K at 120fps achievable on high-end hardware, and ultrawide monitor support at 21:9 and 32:9 aspect ratios. Rockstar has confirmed official mod support via the Rockstar Mod Toolkit, a significant philosophical shift from the company's historically adversarial relationship with the modding community — prompted, insiders suggest, by the extraordinary longevity GTA 5 has enjoyed due to mod-driven content.

The PC version will launch with all console content parity and will share the same online infrastructure as console players, with cross-platform sessions confirmed as optional. Minimum specifications have not yet been published, but Rockstar has stated that the recommended configuration for 1080p at 60fps should be achievable on hardware from 2022 onwards.""",
    },
    {
        "id": 32, "category": """PC""",
        "tag": """AMD""", "tag_class": """tag-pc""",
        "headline": """AMD Radeon RX 9090 XT Review — Trades Blows with RTX 5090""",
        "summary": """AMD's RDNA 5 flagship arrives swinging. The RX 9090 XT matches or beats the RTX 5090 in rasterization workloads at $999 — $600 less than NVIDIA's card. A landmark value for the red team.""",
        "author": """Tom Bradley""", "date": """Mar 22, 2026""",
        "score": None,
        "image": """https://www.amd.com/content/dam/amd/en/images/products/graphics/2922918-future-ready_03.jpg""",
        "image_position": """83% 79%""",
        "featured": False,
        "body": """The AMD Radeon RX 9090 XT is the most competitive flagship GPU AMD has shipped in a decade, and its value proposition is remarkable: at $999 MSRP, it matches or exceeds the RTX 5090 — a $1,199 card — in traditional rasterised rendering workloads across the majority of the game library. In titles without ray tracing, the 9090 XT is within 3% of Nvidia's flagship on average, and in several compute-heavy workloads it leads by a meaningful margin. This is AMD's first genuine performance parity at the high end since the Fury X in 2015.

The RDNA 5 architecture's most significant improvement is in shader throughput efficiency. AMD's "Infinity Cache 4.0" — now scaling to 512 MB on the 9090 XT — virtually eliminates memory bandwidth as a bottleneck in rasterised scenarios, explaining the performance gains without proportional increases in power consumption. The 9090 XT draws 380W under full load, comparable to the RTX 5090 and significantly below the 5090's 600W peak.

Where the 9090 XT falls short is ray tracing. In full path-traced scenarios, it trails the RTX 5090 by 30-40%, reflecting the architectural difference in dedicated RT acceleration. FSR 4, AMD's latest upscaling solution, closes the gap considerably in practice — delivering good quality at Performance mode settings — but DLSS 5's frame generation capability gives Nvidia a practical advantage in supported titles. For rasterised gaming on a budget relative to Nvidia's flagship, the RX 9090 XT is an exceptional choice.""",
    },
    {
        "id": 33, "category": """eSports""",
        "tag": """eSports""", "tag_class": """tag-esports""",
        "headline": """Worlds 2026 — T1 Wins Third Consecutive World Championship""",
        "summary": """Faker cements his legacy as the greatest of all time with an unprecedented third consecutive Worlds title, defeating Gen.G 3-1 in an electrifying final watched by 73 million concurrent viewers worldwide.""",
        "author": """Jin-Ho Park""", "date": """Apr 12, 2026""",
        "score": None,
        "image": """https://esportsinsider.com/wp-content/uploads/2025/11/league-of-legends-worlds-2026-texas-new-york.jpg""",
        "image_position": """63% 28%""",
        "featured": True,
        "body": """T1 has won the 2026 League of Legends World Championship, defeating Gen.G 3-1 in a Seoul final that drew 73 million concurrent viewers — the largest esports audience in history. The victory is Lee "Faker" Sang-hyeok's unprecedented third consecutive Worlds title and his eighth overall, extending a legacy that has become the defining story of competitive gaming's first generation. When the Nexus fell in Game 4, the Jamsil Arena crowd eruption measured on nearby seismographs.

The series was technically flawless and narratively perfect. Gen.G took Game 2 in dominant fashion, silencing T1 supporters and opening the genuine possibility of an upset. Faker's response in Game 3 — a Lissandra mid-lane performance of surgical aggression — is already being called one of the greatest individual championship performances in the history of the format. T1's macro play in Games 3 and 4 was structurally perfect: vision control suffocating Gen.G's early game while Gumayusi's Jinx built to a scaling threshold that Gen.G's composition had no answer for.

The closing ceremony featured a 20-minute holographic production that projected the history of Worlds across the stadium's ceiling, ending with Faker's silhouette ascending through every Worlds trophy he has won. Whether by design or circumstance, there was no cleaner image for the end of an era — and the beginning of the question of what comes next for a player who has won everything the game has to offer.""",
    },
    {
        "id": 34, "category": """eSports""",
        "tag": """CS2""", "tag_class": """tag-esports""",
        "headline": """CS2 Major — NaVi Beats Vitality in Overtime Classic""",
        "summary": """Natus Vincere outlasts Team Vitality in an overtime thriller at the Paris Major, securing their second CS2 Major trophy with a clutch 1v3 from s1mple on match point that the crowd will never forget.""",
        "author": """Elena Kovacs""", "date": """Apr 9, 2026""",
        "score": None,
        "image": """https://upload.wikimedia.org/wikipedia/commons/d/d9/MLG_Columbus_-_Luminosity_vs_Navi.jpg""",
        "image_position": """50% 50%""",
        "featured": False,
        "body": """The Paris CS2 Major final between Natus Vincere and Team Vitality will be remembered for a single moment, but the match that produced it was 44 rounds of relentless, technically exquisite Counter-Strike played at a level that justified every superlative the commentators reached for. Vitality, spearheaded by ZywOo's otherworldly AWP work on the T-side, took the first map convincingly and pushed NaVi to the edge on Map 2 before Aleksandr "s1mple" Kostyliev delivered a defining career moment.

Down 15-14 in Map 2 overtime, NaVi in a 1v3 disadvantage, s1mple held the Mirage B-site with a pistol and three bullets. What followed over 40 seconds is already in the highlights reel of all-time great CS plays: a blind grenade that isolated the first enemy, a pixel-perfect wall shot through smokes on the second, and a knife finisher on the third that the crowd's reaction rendered inaudible on the broadcast. The round win swung momentum irreversibly.

NaVi took Map 3 methodically, with b1t providing consistent rifle support that complemented s1mple's playmaking without redundancy. The 2-1 victory is NaVi's second CS2 Major and their fifth Major overall, cementing the organisation's position as the most decorated in the format's history. s1mple's performance across the entire tournament — 1.32 HLTV rating across 47 maps — is statistically the greatest Major run ever recorded.""",
    },
    {
        "id": 35, "category": """eSports""",
        "tag": """Valorant""", "tag_class": """tag-esports""",
        "headline": """Valorant Champions 2026 — Sentinels Claim the Trophy""",
        "summary": """Sentinels make history as the first North American team to win the Valorant Champions World Championship, defeating Paper Rex in a thrilling 3-2 grand final after a reverse sweep.""",
        "author": """Jin-Ho Park""", "date": """Apr 5, 2026""",
        "score": None,
        "image": """https://cdn.sanity.io/images/zoz4y99f/production/96733ef674f782bef0c3c5b748ff5212016c5d40-1600x900.jpg?w=1600&auto=format""",
        "image_position": """51% 50%""",
        "featured": False,
        "body": """Sentinels are Valorant Champions. The North American organisation — the most storied brand in Valorant's competitive history, carrying the weight of years of near-misses and roster turbulence — have finally delivered the result their fanbase has waited four years for, defeating Paper Rex 3-2 in a grand final reverse sweep that will define the tournament forever. When Zellsis hit the winning shot in Map 5 overtime, the sheer volume of the viewer reaction across broadcast platforms broke multiple platform streaming records simultaneously.

The series was a study in contrasts. Paper Rex played their signature hyper-aggressive style to near-perfection in Maps 1 and 2, and at 2-0 up the match looked finished. Sentinels' back-to-back comeback maps — both requiring extraordinary individual performances under maximum pressure — are the best sustained team play NA Valorant has ever produced at international level. TenZ, whose legacy had been complicated by years of strong regular season performances unmatched in international tournaments, was the best player on the server for the final three maps.

The win ends a North American drought in international Valorant that had become a defining narrative of the title's competitive era. NA teams had reached seven Champions finals before this edition without winning; the perception of a structural skill gap with Pacific teams had calcified into assumed truth. Sentinels have shattered it, and the implications for Valorant esports' competitive landscape heading into the 2027 season are significant.""",
    },
    {
        "id": 36, "category": """eSports""",
        "tag": """Rocket League""", "tag_class": """tag-esports""",
        "headline": """RLCS 2026 World Championship — Vitality Ends Europe's Drought""",
        "summary": """Team Vitality's Rocket League squad completes a dominant world championship run, going 8-0 across bracket play and becoming the first European team to lift the RLCS World Championship trophy since 2019.""",
        "author": """Elena Kovacs""", "date": """Apr 2, 2026""",
        "score": None,
        "image": """https://images.start.gg/images/tournament/844139/image-f73342e8787431e985662a325b5eae24.jpg""",
        "image_position": """50% 50%""",
        "featured": False,
        "body": """Team Vitality's Rocket League roster has claimed the 2026 RLCS World Championship in convincing fashion, going an undefeated 8-0 through the bracket stage and defeating North American powerhouse NRG 4-1 in the grand final. The victory ends a seven-year European drought at the World Championship level and validates a roster rebuild that looked chaotic on paper but has proven cohesive beyond all expectation in practice.

Vatira's mechanical ceiling was the story of the tournament. Playing primarily as the team's second man in rotations, his aerial precision and speed in 50/50 situations was measurably beyond any other player at the event. His 8.6 shots-on-goal average per game across the championship is a World Championship record. Alongside Jstn's playmaking reliability and Alpha54's defensive anchoring, Vitality's core three functioned as a unit without apparent hierarchy — the most complete team at the event by statistical measures across every key category.

NRG pushed Vitality harder than the scoreline suggests. Games 3 and 4 of the grand final went to overtime, and two critical goalkeeper errors in Game 4 that ultimately cost NRG the series were the difference. Jstn's post-match address was among the most articulate and emotionally honest championship speeches in Rocket League history, acknowledging the years of losing regional finals before this result and the organisational patience that made it possible.""",
    },
    {
        "id": 37, "category": """eSports""",
        "tag": """Dota 2""", "tag_class": """tag-esports""",
        "headline": """The International 2026 — $40M Prize Pool Breaks All Records""",
        "summary": """Valve announces The International 2026 will return to Seattle's Climate Pledge Arena with a record-breaking $40 million prize pool, a new Battle Pass structure, and eight new regional qualifiers.""",
        "author": """Jin-Ho Park""", "date": """Mar 29, 2026""",
        "score": None,
        "image": """https://news.cgtn.com/news/3d4d444e344d544e3167444f774d444d7a596a4e31457a6333566d54/img/67b25936b15844d7a4dcb03df390e612/67b25936b15844d7a4dcb03df390e612.jpg""",
        "image_position": """61% 22%""",
        "featured": False,
        "body": """Valve has officially announced The International 2026, confirming the event will return to Seattle's Climate Pledge Arena — home of TI10, the tournament widely regarded as Dota 2's greatest — with a confirmed base prize pool of $40 million. The figure shatters the previous record of $34.3 million set at TI11, driven by a rebuilt Battle Pass structure that Valve promises will fund pool contributions more transparently and equitably than the previous crowdfunding model that raised concerns about long-term community sustainability.

The new Battle Pass structure separates cosmetic progression from prize pool contribution: a fixed annual subscription funds the community prize pool contribution directly, while optional cosmetic passes fund new hero skins, terrain overhauls, and seasonal events without pool pressure attached. Valve claims this model will deliver a more stable prize pool floor across Dota 2 seasons while preventing the "all-or-nothing" community anxiety that accompanied previous crowdfunding campaigns.

Eight regional qualifiers replace the previous six-region system, splitting the Western Europe and Southeast Asia regions into sub-regions that better represent the competitive distribution of professional teams. The main event bracket expands from 18 to 20 teams. Dates are confirmed for August 3–18, with qualifier windows opening in June. Given TI's history at Climate Pledge Arena — OG's back-to-back TI8/TI9 wins, Neon Esports' miracle run at TI11 — there is no shortage of story to build upon.""",
    },
    {
        "id": 38, "category": """eSports""",
        "tag": """Fortnite""", "tag_class": """tag-esports""",
        "headline": """FNCS Global Finals 2026 — Bugha Wins His Second Title""",
        "summary": """Kyle 'Bugha' Giersdorf recaptures Fortnite's top prize at the FNCS Global Finals in London, seven years after his legendary 2019 World Cup win, making him the only player to win both events.""",
        "author": """Elena Kovacs""", "date": """Mar 25, 2026""",
        "score": None,
        "image": """https://cms-assets.unrealengine.com/cm6l5gfpm05kr07my04cqgy2x/cmixikc3r1g9u07olqysqm677""",
        "image_position": """51% 50%""",
        "featured": False,
        "body": """Kyle "Bugha" Giersdorf has won the 2026 FNCS Global Finals, capturing his second world championship title seven years after the legendary 2019 World Cup victory that made him the most recognised name in competitive Fortnite history. The London O2 Arena final drew the largest in-person Fortnite audience since 2019, and the result — Bugha finishing with 42 points across nine games, six points clear of the field — made for a narrative so clean it would have felt contrived as fiction.

The competitive Fortnite landscape of 2026 bears little resemblance to 2019. Building mechanics have been reworked three times; the map has cycled through five distinct eras; the player pool is younger, faster, and more technically complete than it was when Bugha first won. His victory in this environment, against players who grew up studying his 2019 run, is a different order of achievement. In Games 7 and 8, where the title was genuinely in contention with two competitors within striking distance, Bugha's decision-making under pressure — positioning, engagement selection, resource management — was textbook in ways that left the broadcast analysts running out of analytical language.

Epic Games confirmed a record $16 million prize pool for FNCS 2026, with Bugha taking home $3 million for the win. His post-match interview, characteristically unshowy, focused entirely on thanking his coach and acknowledging the competitors who pushed him. At 23 years old, with another world championship, Bugha's place in gaming history is beyond debate.""",
    },
    {
        "id": 39, "category": """Mobile""",
        "tag": """Pokémon GO""", "tag_class": """tag-mobile""",
        "headline": """Pokémon GO Celebrates 10th Anniversary with Kanto Tour 2026""",
        "summary": """Niantic announces a global in-person Kanto Tour for Pokémon GO's 10th anniversary, featuring all original 151 Pokémon with shiny variants, a new AR battle mode, and a worldwide live event in 50 cities.""",
        "author": """Sofia Nguyen""", "date": """Apr 11, 2026""",
        "score": None,
        "image": """https://images.unsplash.com/photo-1613771404784-3a5686aa2be3?w=900&q=80""",
        "image_position": """center center""",
        "featured": False,
        "body": """Pokémon GO turns ten years old in July 2026, and Niantic is marking the occasion with the most ambitious live event in the game's history: a global Kanto Tour spanning 50 cities across 30 countries simultaneously. The event, running across the first weekend of July, will feature all 151 original Kanto Pokémon available as wild encounters, including shiny variants for every species — a completion that has been systematically built toward since the original Kanto Tour event in 2021.

The headline new feature is AR Battle Mode, a technology Niantic has been developing for three years and is finally debuting at scale. Using the phone's rear camera and depth sensors, AR Battle Mode places your Pokémon into real-world environments for battles that occur in augmented physical space rather than the abstract battle screen. The system tracks real terrain — stairs become obstacles, walls provide cover — in ways that create genuinely novel battle dynamics. Limited testing at smaller Niantic events has produced extremely positive community feedback on the core experience.

The 50 city events will each feature location-exclusive Pokémon encounters tied to each city's geographic and cultural identity — a design decision that rewards travel between events for the most dedicated trainers. Niantic has confirmed special GO Fest-style raids at each location, a global unified storyline event running throughout the weekend, and a commemorative physical TCG card set available exclusively at in-person locations. Ticket pre-registration opens April 20.""",
    },
    {
        "id": 40, "category": """Mobile""",
        "tag": """Review""", "tag_class": """tag-mobile""",
        "headline": """Diablo Immortal Season 12 Review — 7.1 / 10""",
        "summary": """The latest season adds a compelling new class and dungeon biome, but the predatory monetization model continues to hold back what could be a genuinely great mobile ARPG.""",
        "author": """Sofia Nguyen""", "date": """Apr 6, 2026""",
        "score": 7.1,
        "image": """https://sm.ign.com/ign_es/review/d/diablo-imm/diablo-immortal-review-in-progress_ehss.jpg""",
        "image_position": """53% 41%""",
        "featured": False,
        "body": """Diablo Immortal Season 12 introduces the Runemaster class — a long-requested addition for fans of the Diablo universe's runic magic systems — and it is, by a significant margin, the most mechanically interesting class the game has shipped since launch. The Runemaster builds power by inscribing runes onto environmental surfaces during combat, creating persistent magical fields that interact with skills and enemy types in ways that reward spatial awareness and pre-combat preparation. In dungeons, it fundamentally changes the texture of play.

The new Fractured Vault dungeon biome is similarly impressive: a multi-layered labyrinth where walls and floors shift based on accumulated rune inscriptions from previous combat encounters, creating a dungeon that physically records your presence as you progress. The visual design is the best Blizzard's mobile team has produced — monolithic obsidian geometry fractured by glowing rune networks, enemy designs that feel genuinely threatening at scale.

And then there is the monetization. Season 12 makes no structural changes to the legendary gem system that has drawn sustained criticism since launch. The Runemaster's ceiling at free-to-play resonance levels is roughly 65% of the potential of a fully gem-upgraded equivalent — a gap that is meaningful in endgame content but not progress-blocking for casual engagement. This tension — genuinely good design held hostage by extractive monetization — has defined Diablo Immortal since day one. Season 12 does not resolve it.""",
    },
    {
        "id": 41, "category": """Mobile""",
        "tag": """Genshin Impact""", "tag_class": """tag-mobile""",
        "headline": """Genshin Impact Version 6.0 — New Nation of Khaenri'ah Revealed""",
        "summary": """HoYoverse unveils the long-awaited Khaenri'ah nation in Genshin Impact Version 6.0, completing the main storyline's six-year build-up with 7 new playable characters and a completely new elemental reaction system.""",
        "author": """Rin Hasegawa""", "date": """Apr 3, 2026""",
        "score": None,
        "image": """https://assets.xboxservices.com/assets/cd/d0/cdd0d11b-dd3f-40f3-8720-41463983fd45.jpg?n=222910044_GLP-Page-Hero-1084_1920x1080.jpg""",
        "image_position": """52% 20%""",
        "featured": False,
        "body": """Version 6.0 of Genshin Impact is HoYoverse's most significant content update in the game's six-year history, delivering the long-teased nation of Khaenri'ah as a fully explorable region and concluding the main Archon Quest storyline that began in Mondstadt in 2020. The update is enormous by any standard: a new region larger than Fontaine, seven new playable characters, a rebuilt elemental reaction system, and a narrative conclusion that players have theorised about for half a decade.

Khaenri'ah as a playable space defies Genshin's usual aesthetic vocabulary. Where other nations draw from recognisable cultural references, Khaenri'ah is sui generis: a civilisation built entirely underground, illuminated by engineered constellations projected on cavern ceilings, its architecture combining mechanical precision with an organic decay that makes every corner feel simultaneously ancient and wrong. The music, composed entirely with synthetic instruments derived from the world's fictional technology, is unlike anything in the existing soundtrack.

The new elemental reaction system introduces a sixth energy state — Voidfire — that interacts with all seven existing elements in unique ways, requiring players to rethink team compositions built over years of play. HoYoverse has balanced the power level carefully: Voidfire reactions are powerful but situational, not power-creeping existing builds into irrelevance. Seven new characters span all existing element types reimagined through Khaenri'an design philosophy, with the nation's cultural aesthetic producing some of the most visually distinctive character designs in the game.""",
    },
    {
        "id": 42, "category": """Mobile""",
        "tag": """Clash""", "tag_class": """tag-mobile""",
        "headline": """Clash of Clans Town Hall 18 — Giant Mechs Enter the Battle""",
        "summary": """Supercell's biggest update in years introduces Town Hall 18 with a new Giant Mech troop, revamped air combat, a dedicated war spectator mode, and the brand-new 'Clash Royale crossover' seasonal event.""",
        "author": """Sofia Nguyen""", "date": """Mar 31, 2026""",
        "score": None,
        "image": """https://media.pocketgamer.com/artwork/na-18945-1715862046/clash-of-clans-erling-haaland_jpg_820.jpg""",
        "image_position": """62% 26%""",
        "featured": False,
        "body": """Clash of Clans Town Hall 18 is the game's largest structural update in three years, and it lands with a confidence that suggests Supercell is very aware of the competitive pressure from newer mobile strategy games. The headline addition is the Giant Mech — a new super troop that towers over existing defences and introduces a mechanic new to the franchise: a pilot system where the Mech is destroyed but a smaller unit ejects and continues fighting independently. It creates a two-phase offensive unit that requires defenders to plan for both phases simultaneously.

Air combat has been substantially revised. The Eagle Artillery has been reworked to target aerial units with a dedicated secondary mode, anti-air defences gain new range parameters at TH18, and two new aerial troops designed specifically for TH18 raids add vertical strategic complexity that ground-focused clans will need to adapt to. The war spectator mode — allowing clanmates to watch ongoing war attacks in real-time through an overhead perspective — has been among the most frequently requested features in the game's history and arrives fully implemented.

The Clash Royale crossover event brings four iconic Royale cards to CoC as temporary seasonal troops, available to all players from Village Hall 6 upward for the event's three-week duration. Gameplay integration is surprisingly cohesive — the Giant Knight and Skeleton Army in particular translate to CoC's mechanics with minimal friction. Supercell has indicated this crossover will be annual, with different Royale card selections each time.""",
    },
    {
        "id": 43, "category": """Mobile""",
        "tag": """Apple Arcade""", "tag_class": """tag-mobile""",
        "headline": """Apple Arcade Adds 10 Premium Titles — No Ads, No IAP""",
        "summary": """Apple Arcade's spring refresh brings 10 new curated titles including a new Infinity Blade-style RPG, a narrative mystery from Annapurna Interactive, and an exclusive Sega arcade classic revival.""",
        "author": """Rin Hasegawa""", "date": """Mar 28, 2026""",
        "score": None,
        "image": """https://i.blogs.es/cc96b6/apple-arcade-2/1366_2000.jpg""",
        "image_position": """50% 50%""",
        "featured": False,
        "body": """Apple Arcade's Spring 2026 refresh brings 10 new titles to the subscription service, continuing the platform's steady evolution from its uneven early years into the most consistently curated premium mobile gaming service available. All 10 titles are zero-ad, zero-in-app-purchase experiences — Apple Arcade's core value proposition — and the quality floor across the lineup is notably higher than comparable addition batches from 2024.

The standout addition is Edge of Eternity: Ascendant, a collaboration between Epic Games' Chair division — original creators of Infinity Blade — and a new studio from former FromSoftware designers. It is explicitly positioned as a spiritual successor to Infinity Blade's touch-based sword combat, rebuilt for modern Apple hardware with haptic feedback integration that makes parrying feel tactile in ways the original never could. Early press previews have described it as the best touchscreen combat system designed for mobile.

Annapurna Interactive's contribution — an untitled narrative mystery set in a 1970s New York art world — represents the publisher's first mobile-exclusive release and features a narrative structure unique to Apple Arcade's offline-first model. The Sega revival is Virtua Fighter Legacy, a fully rebuilt adaptation of the iconic fighting series with portrait-mode controls and an asynchronous tournament mode. Apple Arcade's library now stands at 230 titles, with average subscriber engagement up 34% year-over-year according to Apple's most recent services earnings disclosure.""",
    },
    {
        "id": 44, "category": """Mobile""",
        "tag": """PUBG Mobile""", "tag_class": """tag-mobile""",
        "headline": """PUBG Mobile Season 30 — New Desert Map & Vehicle Warfare""",
        "summary": """Krafton's season 30 update introduces the largest PUBG Mobile map yet — a sprawling desert wasteland with drivable tanks, helicopter gunships, and a new 120-player squad mode exclusive to mobile.""",
        "author": """Rin Hasegawa""", "date": """Mar 24, 2026""",
        "score": None,
        "image": """https://wstatic-prod.pubg.com/web/live/main_3a39d95/img/8253dec.webp""",
        "image_position": """55% 28%""",
        "featured": False,
        "body": """PUBG Mobile Season 30 arrives with the largest map addition in the franchise's history: Sandstorm Wastes, a 16km² desert environment that doubles the playable area of the existing Miramar map and introduces a category of military hardware previously absent from the mobile game. Tanks — fully drivable, destructible, and requiring a two-player crew to operate at full effectiveness — are the headline vehicle addition, along with light scout helicopters that can carry a single pilot and provide the game's first fully aerial traversal option.

Sandstorm Wastes is architecturally distinct from PUBG's existing desert aesthetic. Where Miramar evokes the American Southwest, Sandstorm Wastes draws from Central Asian steppe geography: abandoned Soviet-era military installations half-buried by dune migration, underground bunker networks that provide safe passage between surface danger zones, and a dynamic sandstorm mechanic that periodically reduces visibility to near-zero and disables vehicle GPS. The weather event creates tactical windows that invert normal engagement logic — close-range infantry combat becomes dominant when the storm peaks.

The 120-player squad mode is exclusive to mobile — PC and console PUBG maintain the 100-player standard — enabled by server infrastructure improvements that Krafton has been building toward for 18 months. Six-player squads (up from four) allow for more complex tactical roles within a team: dedicated driver/pilot crews, support specialists, and sniper overwatch positions become viable without reducing core combat effectiveness. Season 30 launches April 1 with a coordinated global rollout across all supported devices.""",
    },
    {
        "id": 45, "category": """PlayStation""",
        "tag": """Review""", "tag_class": """tag-ps""",
        "headline": """Stellar Blade 2 Review — 8.7 / 10""",
        "summary": """Shift Up's follow-up refines everything that made the original divisive: tighter combat, a stronger narrative, and a world that earns its spectacle. A confident step forward.""",
        "author": """Lena Park""", "date": """Apr 11, 2026""",
        "score": 8.7,
        "image": """https://gaming-cdn.com/images/news/articles/17264/cover/shift-up-ha-desvelado-una-primera-imagen-de-stellar-blade-2-cover696e040e30ad5.jpg""",
        "image_position": """50% 9%""",
        "featured": False,
        "body": """Shift Up arrived with Stellar Blade in 2024 and divided critics cleanly down the middle: extraordinary combat, underwhelming story, too much borrowed from Nier. Two years on, Stellar Blade 2 addresses every significant complaint while keeping what worked. Eve returns, the post-apocalyptic Earth setting expands dramatically, and a co-developer relationship with Guerrilla Games has lent the world-building a coherence the original sorely lacked.

Combat remains the centrepiece and it's never felt better. The Beta Gauge system has been redesigned so that offensive and defensive mechanics share a single resource, forcing constant trade-off decisions that keep every encounter tense. New enemy classes introduced in the second half actively punish passive playstyles, pushing the game into genuinely difficult territory without resorting to cheap hits. Boss design is consistently excellent — the third-act confrontation in particular ranks among the best PS5 has offered.

Where Stellar Blade 2 truly earns its score is in its willingness to slow down. Environmental storytelling has improved enormously; the ruins of what was once Seoul are filled with audio logs, murals and architectural details that reward careful exploration. The narrative still leans on familiar sci-fi tropes but delivers them with enough sincerity that the emotional beats land. Not flawless, but a confident and impressive sequel.""",
    },
    {
        "id": 46, "category": """PlayStation""",
        "tag": """Review""", "tag_class": """tag-ps""",
        "headline": """Until Dawn Remake Review — 7.4 / 10""",
        "summary": """Ballistic Moon's PS5 rebuild looks the part but struggles to justify its existence. The core horror is intact, yet the additions feel thin and the pacing suffers in the new chapters.""",
        "author": """Marco Vidal""", "date": """Apr 2, 2026""",
        "score": 7.4,
        "image": """https://assetsio.gnwcdn.com/Until-Dawn-PS5-PC.png?width=1200&height=630&fit=crop&enable=upscale&auto=webp""",
        "image_position": """53% 19%""",
        "featured": False,
        "body": """The original Until Dawn was a perfectly calibrated teen-horror fantasy that understood exactly what it was trying to be. Ballistic Moon's PS5 remake preserves that quality almost entirely — which raises the obvious question: why bother? The visual overhaul is undeniably impressive, with photorealistic character models and a new Unreal Engine 5 presentation that does justice to Blackwood Mountain's gothic atmosphere. But a remake needs to do more than look better, and Until Dawn 2025 struggles to articulate what that more actually is.

The new epilogue chapter, set one year after the main events, is the addition with the most potential and the least execution. It introduces a returning survivor whose arc feels truncated, resolving in under 90 minutes with a twist that undercuts the original's ambiguity. The butterfly effect system has been expanded with new decision nodes, though most lead to outcomes indistinguishable from the 2015 version. Dedicated fans will find a handful of genuinely new endings, but the path to them feels artificially gated.

On its own terms — as an introduction for newcomers or a nostalgia run for veterans on PS5 — Until Dawn still delivers. The horror setpieces hold up, the cast performances remain excellent, and the interactive film format is as accessible as ever. It's a good game. It's just a remake that can't quite justify the full price tag.""",
    },
    {
        "id": 47, "category": """Xbox""",
        "tag": """Review""", "tag_class": """tag-xbox""",
        "headline": """Fable Review — 8.1 / 10""",
        "summary": """Playground Games' long-awaited revival delivers a charming, funny, and mechanically rich action-RPG. It doesn't reinvent the genre but it does revive a beloved one with genuine love.""",
        "author": """David Kim""", "date": """Apr 13, 2026""",
        "score": 8.1,
        "image": """https://i.blogs.es/7acf25/fable/500_333.webp""",
        "image_position": """60% 7%""",
        "featured": False,
        "body": """After five years of development and more than a few raised eyebrows at Playground Games — best known for Forza Horizon — taking the helm, Fable is finally here. The verdict: it's good, sometimes great, occasionally frustrating, and unmistakably Fable. The Albion of 2026 is a world thick with satirical wit, absurdist folk horror, and a moral system that genuinely shapes your character's appearance and the way NPCs interact with you. It is, in other words, exactly what the series always was.

Combat is the biggest upgrade from the originals. Playground's experience building Forza translates surprisingly well to third-person action: movement feels weighty and responsive, spell combinations have real depth, and the hero system — which lets you invest in warrior, mage, or rogue archetypes simultaneously rather than committing to one — gives builds meaningful variety. A mid-game skill ceiling spike may deter some players, but those who invest in mastery will find a satisfying loop.

The story falters slightly in its middle act, spreading itself thin across too many villain factions before a confident finale. But the writing is consistently sharp and the world is densely inhabited with memorable NPCs whose lives evolve based on player choices over a surprisingly long play time. Fable is not the revolution some hoped for, but it is a triumphant, confident return for one of gaming's most beloved franchises.""",
    },
    {
        "id": 48, "category": """Xbox""",
        "tag": """Review""", "tag_class": """tag-xbox""",
        "headline": """Avowed Review — 7.9 / 10""",
        "summary": """Obsidian's first-person RPG in the Pillars of Eternity universe is dense, literate, and mechanically satisfying — though its open zones feel underpopulated and the pacing is uneven.""",
        "author": """Sarah Thompson""", "date": """Mar 28, 2026""",
        "score": 7.9,
        "image": """https://www.denofgeek.com/wp-content/uploads/2024/11/avowed.jpg?fit=2000%2C1125""",
        "image_position": """51% 42%""",
        "featured": False,
        "body": """Obsidian Entertainment has been the quiet giant of western RPGs for two decades, and Avowed confirms that reputation once again. Set in the Living Lands — a region of Eora previously unexplored in the Pillars of Eternity series — Avowed translates the franchise's philosophical depth and faction-driven politics into a first-person action-RPG format that splits the difference between The Elder Scrolls and Prey. The result is a game with extraordinary writing and uneven execution.

The combat system is Avowed's most pleasant surprise. Two-handed weapon combinations — sword and wand, arquebus and grimoire, twin daggers and off-hand pistol — feel meaningfully distinct, and the Godlike abilities unlocked through the main story create build-defining moments that shift combat rhythm significantly. Enemy variety is adequate without being exceptional, but the tactical depth of the system earns genuine respect.

Where Avowed stumbles is spatial. The open zones — six in total — are architecturally beautiful but feel underpopulated with meaningful content. Side quests cluster around zone entrances, leaving large swathes of the map as scenic backdrop rather than playable space. A tighter, more curated experience would have served the game's strengths better. Still, for RPG fans willing to meet it on its own terms, Avowed delivers one of the most genuinely mature narratives in the genre this generation.""",
    },
    {
        "id": 49, "category": """Nintendo""",
        "tag": """Review""", "tag_class": """tag-nin""",
        "headline": """Mario Kart World Review — 9.4 / 10""",
        "summary": """Nintendo's open-world racing reinvention is a masterpiece of joyful design. Mario Kart World is the biggest leap the franchise has taken since Double Dash, and it sticks the landing completely.""",
        "author": """Yuki Tanaka""", "date": """Apr 10, 2026""",
        "score": 9.4,
        "image": """https://www.nintenderos.com/wp-content/uploads/2025/06/truco-impulsarte-alto-Mario-Kart-World.jpg""",
        "image_position": """62% 66%""",
        "featured": False,
        "body": """Nintendo promised that Mario Kart World would reimagine what a racing game could be, and for once the marketing undersells the reality. What Bandai Namco and Nintendo have delivered is not merely the best Mario Kart ever made — it is a fundamental reconsideration of the kart-racing genre, built around a seamless open world that transforms the space between races into as much fun as the races themselves.

The Mushroom Kingdom map is staggering in scale and density. Twenty-four interconnected regions flow into one another without load screens, each with distinct racing circuits, hidden shortcuts, collectible coins, and roaming NPC drivers whose behaviour adapts to your presence. Between Grand Prix events you're free to explore, challenge wandering rivals, discover secret routes, or simply drive across the landscape enjoying the most technically impressive Nintendo game ever made. Switch 2 hardware is pushed hard here: stable 60fps, draw distances that shame comparable open-world racers, and a dynamic weather system that visually transforms every region.

Online play — 24 racers in open-world lobbies — is the mode that will define Mario Kart World for years. Organised chaos at its finest. The item balance is the best the series has seen, steering away from rubber-band frustration while keeping late-race drama intact. A triumph on every level.""",
    },
    {
        "id": 50, "category": """Nintendo""",
        "tag": """Review""", "tag_class": """tag-nin""",
        "headline": """Donkey Kong Bananza Review — 8.8 / 10""",
        "summary": """A fully destructible world and Donkey Kong's most expressive moveset yet make Bananza one of Switch 2's best launch titles. It's loud, chaotic, and brilliantly designed.""",
        "author": """Camila Reyes""", "date": """Apr 4, 2026""",
        "score": 8.8,
        "image": """https://www.irrompibles.net/irrwp/wp-content/uploads/2025/07/DK-bananza-key-art.jpg""",
        "image_position": """58% 53%""",
        "featured": False,
        "body": """Donkey Kong Bananza arrives as the clearest statement yet that Nintendo intends Switch 2 to be a showcase platform, not just a hardware upgrade. Developed by the team behind Super Mario Odyssey, Bananza is a 3D platformer centred entirely on environmental destruction: every surface, wall, floor, and ceiling in every level is damageable, collapsible, or smashable, and the game's puzzles, combat, and traversal are built entirely around this premise.

DK's moveset is the most developed it has ever been. Ground pounds create craters that reveal underground paths. Charged punches blow holes through walls that persist permanently, creating new routes for backtracking. The Primal Fury meter — built by rhythmic button presses matching on-screen prompts — unleashes a berserker mode where DK can collapse entire columns, excavate buried treasure chambers, or simply destroy an enemy base in seconds. It is enormously satisfying on a physical level that few games achieve.

The level design is where Bananza truly earns its score. Each of the eight worlds is built as a multi-layered geological cross-section, with surface routes, mid-layer cave networks, and deep underground zones all accessible through destruction at any time. Boss encounters are spectacular, the soundtrack is a hip-hop-inflected banger from start to finish, and the two-player co-op mode — one player as DK, one as Pauline with her own unique mechanics — is one of Nintendo's best co-op implementations in years.""",
    },
    {
        "id": 52, "category": """PC""",
        "tag": """Review""", "tag_class": """tag-pc""",
        "headline": """Hollow Knight: Silksong Review — 9.1 / 10""",
        "summary": """Team Cherry's follow-up is bigger, bolder, and more mechanically ambitious than its predecessor. Hornet's adventure through Pharloom is a defining achievement in the Metroidvania genre.""",
        "author": """Sofia Nguyen""", "date": """Mar 10, 2026""",
        "score": 9.1,
        "image": """https://img.asmedia.epimg.net/resizer/v2/S3SRO4PPJVC6RBBNI2JUXOPYVY.jpg?auth=36f3c3cb71a129d3d9c1c5cb267a799bd125aba43a5e992e34be4b12dd8c45a3&width=1472&height=828&smart=true""",
        "image_position": """64% 0%""",
        "featured": False,
        "body": """Six years after its announcement, Hollow Knight: Silksong arrives carrying a weight of expectation that would collapse most games. Team Cherry has not only met that expectation — they have exceeded it in ways that suggest the extended development time was used to rethink, from the ground up, what a follow-up to Hollow Knight needed to be. The result is a game that stands fully independent of its predecessor while rewarding deep familiarity with the original's systems and lore.

Hornet's moveset centres on silk and needle: thread-based traversal that allows mid-air redirection, a combat system built on binding enemies before delivering killing blows, and a crafting mechanic — using materials harvested from the environment — that creates persistent upgrades rather than temporary buffs. The skill ceiling is higher than Hollow Knight's, and the game respects that investment with boss encounters that are consistently the best Team Cherry has designed. The final gauntlet, in particular, is extraordinary.

Pharloom is a more varied world than Hallownest, cycling through biomes that range from overgrown clockwork towers to flooded ceremonial ruins to a canopy village suspended between sleeping giants. The art direction, already legendary after Hollow Knight, has evolved into something even more confident. The soundtrack by Christopher Larkin is a masterwork. Silksong is, simply, one of the best games ever made in its genre.""",
    },
    {
        "id": 53, "category": """eSports""",
        "tag": """Review""", "tag_class": """tag-esports""",
        "headline": """Valorant Episode 9 Review — 8.2 / 10""",
        "summary": """Riot's tactical shooter enters its most polished season yet. New agent Kestrel, a reworked economy system, and the best map pool in the game's history make Episode 9 the definitive Valorant.""",
        "author": """Marcus Bell""", "date": """Apr 7, 2026""",
        "score": 8.2,
        "image": """https://cmsassets.rgpub.io/sanity/images/dsfx7636/news_live/67fbd4c273f3d5e92a18666c6379db09e74b7cda-1920x1080.jpg?accountingTag=VAL&auto=format&fit=fill&q=80&w=1541""",
        "image_position": """70% 0%""",
        "featured": False,
        "body": """Riot Games has spent five years refining Valorant into the dominant force in tactical shooters, and Episode 9 represents the clearest distillation of that work. New agent Kestrel — a recon-focused controller who deploys sonic tripwires and can temporarily deafen enemies through walls — slots into the meta cleanly without breaking it, filling a genuine gap in the information-gathering toolkit without rendering existing agents obsolete. Her design shows Riot's growing maturity in balancing utility-heavy agents.

The economy rework is the most significant systemic change since Episode 1. Loss bonus scaling has been adjusted to reduce comeback snowballs, and a new "partial buy" system allows full-team half-buys with a coordinated bonus pool — rewarding teams that communicate over those who simply follow individual buy instincts. At the professional level, this has already produced more diverse round-by-round strategies. At ranked, it smooths out the frustrating buy-mismatch dynamic that plagued the previous economy for years.

The map pool is, genuinely, the best it has ever been. The return of Split in its reworked form, paired with the new Bastion map — a brutalist concrete fortress with three distinct vertical layers — gives the competitive pool genuine variety. Valorant in 2026 is not a perfect game, but it is a deeply refined one, and Episode 9 earns the loyalty of its enormous player base.""",
    },
    {
        "id": 54, "category": """eSports""",
        "tag": """Review""", "tag_class": """tag-esports""",
        "headline": """League of Legends Season 2026 Review — 7.6 / 10""",
        "summary": """Riot's annual reset brings meaningful map changes and a revamped item system that freshens a 16-year-old game. Pacing remains a concern, but Season 2026 is the most balanced LoL in years.""",
        "author": """Yuki Tanaka""", "date": """Feb 20, 2026""",
        "score": 7.6,
        "image": """https://cmsassets.rgpub.io/sanity/images/dsfx7636/news_live/b3ceff2c095ca3799116a3b45ae3a930721319d7-1920x1080.jpg?accountingTag=LoL""",
        "image_position": """53% 34%""",
        "featured": False,
        "body": """Reviewing a live-service game annually is an inherently imprecise exercise — the game you review in February may not resemble the game in August. But League of Legends' season-start represents the closest thing to a defined release point the game has, and Season 2026's opening patch is the most substantive reset Riot has delivered in half a decade.

The Rift overhaul is the headline change: Summoner's Rift has received structural alterations for the first time since 2015. The Baron pit has been relocated to open up the north-east approach, a new secondary objective — the Voidgate — spawns at 20 minutes and offers a temporary fast-travel mechanic for flanking, and the river terrain now includes elevated ground that allows certain champions genuine line-of-sight advantages. These aren't revolutionary changes, but they disrupt 16 years of deeply encoded positional habits in ways that make the early season feel genuinely fresh.

The item system overhaul — consolidating the bloated 200-item catalogue to 140 more meaningfully differentiated options — is the change competitive players will care most about. Build diversity across the competitive meta is at a historic high; champions that have been fringe picks for years are emerging as serious threats. The pacing issue — games running long due to tower resilience — persists and needs addressing before Worlds. But as season resets go, 2026 is a strong one.""",
    },
    {
        "id": 55, "category": """eSports""",
        "tag": """Review""", "tag_class": """tag-esports""",
        "headline": """Rocket League Season 14 Review — 8.5 / 10""",
        "summary": """Psyonix delivers the most content-rich Rocket League season since going free-to-play. New arena physics, a reworked rank system, and a competitive scene at its peak make this essential.""",
        "author": """David Kim""", "date": """Mar 5, 2026""",
        "score": 8.5,
        "image": """https://fotografias-neox.atresmedia.com/clipping/cmsimages02/2018/07/18/BAB39E22-EFA6-4FA8-A795-F8FC37F617C8/98.jpg?crop=1920,1080,x0,y0&width=1900&height=1069&optimize=high&format=webply""",
        "image_position": """52% 88%""",
        "featured": False,
        "body": """Rocket League turns eleven this year and shows no signs of the entropy that typically afflicts games of its age. Season 14 is evidence of a development team that understands its audience precisely: changes are measured, meaningful, and consistently directed at the things that matter most to competitive play. This is a game that respects its player base's time investment, and Season 14 reinforces that reputation.

Arena physics variation is the boldest new system. Five of the game's competitive maps now have subtly distinct ball physics — slightly different coefficient of restitution, marginal variance in boost pad regeneration timing — creating genuine home/away-style tactical preparation for serious players. Critics will note this adds complexity that beginners don't need; Psyonix has responded by making physics-variable maps optional in ranked queues below Diamond. A fair compromise.

The rank reset and new Grand Champion subdivisions address years of complaints about the ceiling tier becoming overcrowded. SSL (Supersonic Legend) now requires a rolling performance metric rather than a static point threshold, meaning rank is maintained only by continued excellence rather than accumulated by a single good streak. Early data suggests rank distribution has normalised significantly. The Season 14 cosmetic pass is also the most generous since free-to-play launch, with three fan-designed cars included at the premium tier. Rocket League endures because it keeps earning it.""",
    },
    {
        "id": 56, "category": """Mobile""",
        "tag": """Review""", "tag_class": """tag-mobile""",
        "headline": """Pokémon TCG Pocket Season 2 Review — 8.0 / 10""",
        "summary": """DeNA's digital card game matures enormously in its second season. Improved deck-building, a ranked ladder that rewards skill over spending, and gorgeous new card art make this hard to put down.""",
        "author": """Rin Hasegawa""", "date": """Apr 9, 2026""",
        "score": 8.0,
        "image": """https://images.unsplash.com/photo-1606503153255-59d8b8b82176?w=900&q=80""",
        "image_position": """center center""",
        "featured": False,
        "body": """Pokémon TCG Pocket launched to enormous fanfare in 2024 and immediately attracted criticism for aggressive monetisation that undermined competitive integrity. Season 2 represents a genuine course correction. DeNA has restructured the card acquisition system so that a dedicated free-to-play player can build a competitive deck within three weeks of consistent daily play — a marked improvement over Season 1's near-impossible grind for meta staples.

The core card game has been refined significantly. The two-prize rule that distinguished Pocket from the physical TCG has evolved into a more nuanced three-prize variant for ranked play, opening up deck archetypes that previously had no viable win condition within the restricted format. Trainer card rebalancing — several previously dominant support cards adjusted down — has opened the meta to more diverse strategies, and the new Paradox expansion introduces mechanics borrowed from the physical game in ways that translate surprisingly well to the mobile format.

What elevates Season 2 is the art. The new Illustrator Rare card tier — featuring original artwork commissioned from contemporary artists outside the traditional Pokémon design stable — produces cards of genuine aesthetic beauty. The animated versions, available at higher rarity, are among the most impressive digital card presentations in any mobile card game. The game still has a monetisation ceiling that separates fully invested spenders from free players, but Season 2 demonstrates meaningful commitment to competitive fairness.""",
    },
    {
        "id": 57, "category": """Mobile""",
        "tag": """Review""", "tag_class": """tag-mobile""",
        "headline": """Diablo Immortal Season 6 Review — 7.3 / 10""",
        "summary": """Blizzard's mobile dungeon-crawler finally addresses its most notorious systems. Season 6 is the most generous and mechanically sound Diablo Immortal has been — though old habits linger.""",
        "author": """Marco Vidal""", "date": """Mar 15, 2026""",
        "score": 7.3,
        "image": """https://blz-contentstack-images.akamaized.net/v3/assets/bltf408a0557f4e4998/blt2f22d77ab01a5d15/693bb5dd549186d04950dbeb/Combat_Scosglen_Multiplayer_World_Boss_(1).png?imwidth=1920&imdensity=2.625""",
        "image_position": """52% 42%""",
        "featured": False,
        "body": """Diablo Immortal's launch in 2022 produced one of gaming's most dramatic critical pile-ons, and much of the criticism was warranted: the monetisation was predatory, the pay-to-win ceiling in PvP was essentially limitless, and the gem system created a progression wall that demanded either enormous spending or years of grinding. Four years on, Season 6 represents the most significant structural overhaul the game has received, and the results are genuinely impressive.

The Legendary Gem system has been redesigned from the ground up. The infamous Resonance stat — which translated directly to combat power and was monetised aggressively — has been replaced with a more complex Attunement system where gem synergies between equipped items produce multiplicative bonuses. This decouples raw power from gem quantity, meaning a thoughtfully assembled set of lower-rarity gems can outperform a poorly considered set of higher-rarity ones. PvP brackets have also been stratified by Attunement score range, preventing the most invested players from dominating lobbies of newcomers.

The core game underneath the systems has always been excellent — Blizzard's dungeon-crawler fundamentals are as polished here as anywhere in the franchise. Season 6's new zone, the Sunken Library of Kehjistan, delivers the best endgame content the game has offered: multi-floor procedural dungeons with modifiable difficulty, new enemy families with distinct telegraphed attack patterns, and a boss encounter that genuinely requires coordinated group strategy. Progress, at last.""",
    },
    {
        "id": 58, "category": """PlayStation""",
        "tag": """gaming""", "tag_class": """cat-ps""",
        "headline": """PS5 Pro Firmware 3.0 Enables Boost Mode for All PS4 Games""",
        "summary": """Sony has rolled out firmware 3.0 for the PS5 Pro, enabling a new Boost Mode that targets all PS4 titles with improved frame rates and resolution upscaling.""",
        "author": """Aria Nakamura""", "date": """2026-04-10""",
        "score": None,
        "image": """https://images.unsplash.com/photo-1607853202273-797f1c22a38e?w=900""",
        "image_position": """50% 50%""",
        "featured": False,
        "body": """Sony has rolled out firmware 3.0 for the PS5 Pro with sweeping improvements. The headline feature is an expanded Boost Mode that now applies to nearly all PS4 titles, pushing frame rates towards 60fps where possible and activating the Pro hardware upscaler for resolution boosts.

The calibration tool for spatial audio is another standout addition. Sony also patched several stability issues including occasional crashes in rest mode. The full patch notes run to over forty line items, reflecting a genuine commitment to polish.""",
    },
    {
        "id": 59, "category": """PlayStation""",
        "tag": """exclusive""", "tag_class": """tag-ps""",
        "headline": """Horizon Zero Dawn 3: Forbidden Frontier Revealed at Summer Game Fest""",
        "summary": """Guerrilla Games officially announced Horizon Zero Dawn 3: Forbidden Frontier at Summer Game Fest, confirming Aloy returns alongside a new co-op companion system and dynamic weather engine.""",
        "author": """James Okafor""", "date": """2026-04-08""",
        "score": None,
        "image": """https://img.redbull.com/images/c_limit,w_1500,h_1000/f_auto,q_auto/redbullcom/2020/8/12/vb5hmlaxmksqnvhtptni/hzd-pc-imagen-promocional""",
        "image_position": """57% 4%""",
        "featured": False,
        "body": """Guerrilla Games officially announced Horizon Zero Dawn 3: Forbidden Frontier at Summer Game Fest. The reveal trailer showed dense jungle biomes with new machine types. The companion system lets a second player drop in as Erend or new character Kassi.

The game targets holiday 2027 for PS5 and PS5 Pro, with PC following six months later. The Pro version will run at native 4K 60fps with path-traced lighting.""",
    },
    {
        "id": 60, "category": """PlayStation""",
        "tag": """update""", "tag_class": """tag-ps""",
        "headline": """Astro Bot Cosmic Edition DLC Brings 30 New Levels and PlayStation Icons""",
        "summary": """Team Asobi has announced Cosmic Edition DLC for Astro Bot, delivering 30 brand new levels, over 60 collectible PlayStation cameos, and a DualSense-exclusive haptic challenge world.""",
        "author": """Priya Sharma""", "date": """2026-04-06""",
        "score": None,
        "image": """https://es.kotaku.com/app/uploads/2024/09/7fcb852134df20d90052babc71205d5b.jpg""",
        "image_position": """56% 17%""",
        "featured": False,
        "body": """Team Asobi announced the Cosmic Edition DLC for Astro Bot, delivering 30 new levels, over 60 collectible PlayStation cameos ranging from Lara Croft to Sackboy, and a dedicated DualSense haptic challenge world.

The DLC builds on the GOTY-winning foundation with gravitational puzzles and a new Boss Rush mode. The Cosmic Edition retails at $19.99 and launches alongside a free update adding photo mode, accessibility subtitle scaling, and a colorblind assist toggle.""",
    },
    {
        "id": 61, "category": """PlayStation""",
        "tag": """news""", "tag_class": """tag-ps""",
        "headline": """Wolverine by Insomniac Games Slips to Early 2027 After Creative Overhaul""",
        "summary": """Insomniac Games confirmed that Marvel's Wolverine is moving to Q1 2027 following an internal creative review that reshaped the game's tone and combat system.""",
        "author": """Carlos Rivera""", "date": """2026-04-04""",
        "score": None,
        "image": """https://gameinformer.com/sites/default/files/styles/content_header_l/public/2025/09/24/73cd5604/wolverineb.jpg.webp""",
        "image_position": """50% 43%""",
        "featured": False,
        "body": """Insomniac Games confirmed Marvel Wolverine is moving to Q1 2027 following an internal creative review. A new creative director joined in mid-2025 and championed a grittier approach inspired by the Logan film.

Insomniac also confirmed the game will be a PS5 and PC exclusive, dropping the previously hinted Xbox version. A story trailer is scheduled for Gamescom in August.""",
    },
    {
        "id": 62, "category": """PlayStation""",
        "tag": """news""", "tag_class": """tag-ps""",
        "headline": """Destiny 2: The Pantheon Expansion Brings New Raid and Open World Zone""",
        "summary": """Bungie unveiled The Pantheon expansion for Destiny 2, introducing a brand-new raid, a revamped Void subclass tree, and the largest open-world patrol zone in franchise history.""",
        "author": """Aria Nakamura""", "date": """2026-04-02""",
        "score": None,
        "image": """https://cdn1.epicgames.com/offer/428115def4ca4deea9d69c99c5a5a99e/MX_Bungie_D2_Renegades_FeaturedMedia_1920x1080_1920x1080-78bd7abc00ff048bbe5d96d6676c0d86""",
        "image_position": """57% 72%""",
        "featured": False,
        "body": """Bungie unveiled The Pantheon, the next major Destiny 2 expansion. The headline attraction is a six-player raid set inside a pocket dimension where physics shift between encounters.

The expansion also overhauls the Void subclass with a new Resonance mechanic. A new patrol zone called the Ashen Sprawl spans three interconnected biomes. The Pantheon launches in September and is included in the Year Seven Annual Pass.""",
    },
    {
        "id": 63, "category": """PlayStation""",
        "tag": """news""", "tag_class": """tag-ps""",
        "headline": """PlayStation Network Premium Adds Day-One Downloads for All Sony First-Party Titles""",
        "summary": """Sony announced an upgrade to PlayStation Network Premium, granting day-one download access to all Sony first-party releases starting from July 2026.""",
        "author": """James Okafor""", "date": """2026-03-30""",
        "score": None,
        "image": """https://static.tweaktown.com/news/1/1/110544_9987789_playstation-is-phasing-out-the-playstation-network-branding_full.png""",
        "image_position": """67% 58%""",
        "featured": False,
        "body": """Sony announced an upgrade to PlayStation Network Premium, granting day-one download access to every Sony first-party release starting July 2026. The change aligns PSN Premium more closely with Microsoft Game Pass.

The expanded catalogue will include Gran Turismo 8, Ghost of Yotei, and a Naughty Dog project. The monthly price for Premium rises by three dollars globally. Legacy subscribers are grandfathered at the current rate for twelve months.""",
    },
    {
        "id": 64, "category": """PlayStation""",
        "tag": """news""", "tag_class": """tag-ps""",
        "headline": """Bloober Team's Silent Hill 2 Remake Wins BAFTA Game of the Year 2026""",
        "summary": """Bloober Team took home the top prize at the 2026 BAFTA Game Awards as Silent Hill 2 Remake was named Game of the Year, defeating Elden Ring DLC and Horizon 3.""",
        "author": """Priya Sharma""", "date": """2026-03-28""",
        "score": None,
        "image": """https://media.revistagq.com/photos/6356961fc39eb51840f8af32/16:9/w_2560%2Cc_limit/silent-hill-2-remake-2.jpeg""",
        "image_position": """70% 8%""",
        "featured": False,
        "body": """Bloober Team took home the top prize at the 2026 BAFTA Game Awards as Silent Hill 2 Remake was named Game of the Year. Director Mateusz Lenart accepted the award and dedicated it to Konami and the original Team Silent.

The BAFTA ceremony saw PlayStation titles dominate, with Astro Bot Cosmic Edition picking up Best Family Game. The remake also won Audio Achievement and Narrative Design.""",
    },
    {
        "id": 65, "category": """PlayStation""",
        "tag": """news""", "tag_class": """tag-ps""",
        "headline": """PSVR2 Price Cut to $349 as Sony Pushes Spatial Gaming for Holiday Season""",
        "summary": """Sony reduced the PSVR2 headset price to $349, a $150 reduction, and announced eight new titles arriving in Q3 to bolster the platform library heading into the holiday window.""",
        "author": """Carlos Rivera""", "date": """2026-03-25""",
        "score": None,
        "image": """https://mixed-news.com/en/wp-content/uploads/2022/09/Astro_Bot_PSVR.jpg""",
        "image_position": """59% 51%""",
        "featured": False,
        "body": """Sony reduced the PSVR2 headset to $349 and announced eight new titles arriving in Q3. The titles include a VR-exclusive Resident Evil entry and a multiplayer arena shooter built around PSVR2 eye-tracking.

Sony also confirmed that from October, PSVR2 will be compatible with PC VR via USB-C adapter, opening the headset to the Steam catalogue. Analysts expect this to significantly reverse the platform fortunes.""",
    },
    {
        "id": 66, "category": """Xbox""",
        "tag": """exclusive""", "tag_class": """tag-xbox""",
        "headline": """Fable Gameplay Deep-Dive: Heroism System, Consequence Engine and Co-op Explained""",
        "summary": """Playground Games released a 20-minute gameplay deep-dive for Fable, detailing the Heroism System tracking every NPC faction and a Consequence Engine that permanently alters the world.""",
        "author": """Daniel Park""", "date": """2026-04-11""",
        "score": None,
        "image": """https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/2769570/1f2699edd4bbb52b29eb30c869c286c0d33bd088/page_bg_raw.jpg?t=1769707177""",
        "image_position": """49% 73%""",
        "featured": False,
        "body": """Playground Games released a 20-minute gameplay deep-dive for Fable, revealing the Heroism System and a Consequence Engine that permanently reshapes the world. Kill a merchant and their stall stays empty for the rest of the playthrough.

Two-player online co-op is confirmed where both heroes carry individual reputations. Fable launches October 14 on Xbox Series X and PC via Game Pass. All future story DLC is included in the Game Pass price.""",
    },
    {
        "id": 67, "category": """Xbox""",
        "tag": """news""", "tag_class": """tag-xbox""",
        "headline": """Gears 6 Officially Announced with 2027 Release and Cross-Gen Support""",
        "summary": """The Coalition unveiled Gears 6 with a cinematic trailer at Xbox Developer Direct, confirming a 2027 release and cross-gen support for Xbox Series X and PC.""",
        "author": """Sofia Chen""", "date": """2026-04-09""",
        "score": None,
        "image": """https://cdn.gearsofwar.com/gearsofwar/sites/2/2025/05/GoW_Reloaded_4K_ScreenShot_02-683757e094fc8-scaled.jpg""",
        "image_position": """64% 6%""",
        "featured": False,
        "body": """The Coalition unveiled Gears 6 at Xbox Developer Direct, confirming a 2027 release. The lead protagonist is Kait Diaz continuing from Gears 5, but Marcus Fenix returns in a mentor role.

Multiplayer features a 5v5 zone-capturing mode with dedicated servers from day one. Gears 6 will be available via Game Pass Ultimate on launch day.""",
    },
    {
        "id": 68, "category": """Xbox""",
        "tag": """hardware""", "tag_class": """tag-xbox""",
        "headline": """Xbox Handheld Leaked: Snapdragon X Elite Chip, 8-Inch OLED, Holiday 2026 Target""",
        "summary": """Leaked FCC filings point to Xbox handheld codenamed Project Pebble featuring a Snapdragon X Elite chip, 8-inch 120Hz OLED display, and a holiday 2026 release at around $399.""",
        "author": """Daniel Park""", "date": """2026-04-07""",
        "score": None,
        "image": """https://platform.theverge.com/wp-content/uploads/sites/2/2025/08/VLS_5789-copy.jpg?quality=90&strip=all&crop=0.31250000000001%2C0%2C99.375%2C100&w=1080""",
        "image_position": """55% 16%""",
        "featured": False,
        "body": """Leaked FCC filings and supply chain sources point to Xbox handheld Project Pebble. The device features a Qualcomm Snapdragon X Elite chip, an 8-inch 120Hz OLED display with VRR support, and a custom cooling solution.

The controller layout mirrors the Xbox Series controller with added back paddles and a dedicated AI button. Battery life targets six hours at medium settings. Retailers in Germany received shelf-space allocation for a holiday 2026 SKU priced around $399.""",
    },
    {
        "id": 69, "category": """Xbox""",
        "tag": """exclusive""", "tag_class": """tag-xbox""",
        "headline": """Perfect Dark Gameplay Revealed: Open City, Dynamic Threats and Classic Cameos""",
        "summary": """The Initiative showed Perfect Dark gameplay footage, revealing an open San Francisco setting, a dynamic threat system, and cameos from Jo Dark and Dr. Caroll from the 2000 original.""",
        "author": """Sofia Chen""", "date": """2026-04-05""",
        "score": None,
        "image": """https://cdn.mos.cms.futurecdn.net/S2cfRzTGFZ2dTnzoPYnR7T.jpg""",
        "image_position": """47% 100%""",
        "featured": False,
        "body": """The Initiative showed substantial Perfect Dark gameplay footage. The game is set in near-future San Francisco where corporate towers float above a flooded bay. The dynamic threat system escalates enemy response based on how loudly you operate.

Jo Dark from the original N64 game appears as an older mentor figure. The game launches spring 2027 on Xbox Series X and PC, day one on Game Pass.""",
    },
    {
        "id": 70, "category": """Xbox""",
        "tag": """news""", "tag_class": """tag-xbox""",
        "headline": """Game Pass Q3 Adds Baldur's Gate 4, Halo: The Flood and Vampire Survivors 2""",
        "summary": """Microsoft confirmed the Q3 Game Pass wave, headlined by Baldur's Gate 4, Halo: The Flood and Vampire Survivors 2 all launching on Game Pass day one.""",
        "author": """Daniel Park""", "date": """2026-04-03""",
        "score": None,
        "image": """https://elceo.com/wp-content/uploads/2025/10/microsoft_aumento_precio_xboxgamepasss.jpg""",
        "image_position": """49% 79%""",
        "featured": False,
        "body": """Microsoft confirmed Q3 Game Pass additions: Baldur Gate 4, Halo: The Flood, and Vampire Survivors 2 all arriving on Game Pass Ultimate on their respective launch days.

Baldur Gate 4 is developed by Larian Studios. Halo: The Flood is a narrative action-adventure set during Halo 1. Vampire Survivors 2 features a fully 3D engine and four-player online cooperative play.""",
    },
    {
        "id": 71, "category": """Xbox""",
        "tag": """news""", "tag_class": """tag-xbox""",
        "headline": """Hellblade III Targets 2027 Release as Ninja Theory Confirms Technical Showcase""",
        "summary": """Ninja Theory confirmed Senua's Saga: Hellblade III is targeting a 2027 release with a new technical showcase planned for The Game Awards.""",
        "author": """Sofia Chen""", "date": """2026-04-01""",
        "score": None,
        "image": """https://media.wired.com/photos/598cdf3bf9873438308c953b/master/pass/netflix2-FA.jpg""",
        "image_position": """58% 0%""",
        "featured": False,
        "body": """Ninja Theory confirmed Senua Saga Hellblade III is targeting 2027 with a technical showcase at The Game Awards. The studio called it the most technically ambitious first-person narrative game ever attempted.

Hellblade III will release on Xbox Series X, PC via Game Pass, and — surprising many — PlayStation 5, marking a significant shift in Microsoft exclusivity strategy.""",
    },
    {
        "id": 72, "category": """Xbox""",
        "tag": """update""", "tag_class": """tag-xbox""",
        "headline": """Sea of Thieves Season 14 Introduces Permanent Islands, Player Housing and Guild Wars""",
        "summary": """Rare unveiled Season 14 of Sea of Thieves, the most substantial content drop in game history, introducing permanent buildable islands, player housing, and a Guild Wars competitive mode.""",
        "author": """Daniel Park""", "date": """2026-03-29""",
        "score": None,
        "image": """https://gmedia.playstation.com/is/image/SIEPDC/sea-of-thieves-screenshots-01-en-11mar24?$2400px$""",
        "image_position": """54% 26%""",
        "featured": False,
        "body": """Rare unveiled Season 14 of Sea of Thieves. Permanent buildable islands let crews claim ocean plots, construct their own tavern and dock, and defend against raid events.

Player housing allows customisation of a personal cabin across seventeen room categories. Guild Wars pits the five largest active guilds against each other monthly. Season 14 launches May 7 on Xbox, PC, and PlayStation.""",
    },
    {
        "id": 73, "category": """Xbox""",
        "tag": """update""", "tag_class": """cat-xbox""",
        "headline": """Forza Motorsport Update 12 Adds Nürburgring GP Layout and Weather Overhaul""",
        "summary": """Turn 10 Studios released Forza Motorsport Update 12, bringing the Nürburgring GP layout, 18 new cars led by the Ferrari 296 GT3, and a complete weather system overhaul with dynamic rain accumulation.""",
        "author": """Sofia Chen""", "date": """2026-03-27""",
        "score": None,
        "image": """https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=900""",
        "image_position": """50% 50%""",
        "featured": False,
        "body": """Turn 10 Studios released Forza Motorsport Update 12, headlined by the Nürburgring GP layout. Eighteen new cars arrive led by the Ferrari 296 GT3, McLaren 750S, and a Williams FW46 F1 car.

The weather system overhaul features dynamic rain accumulation with puddles in realistic positions and a drying racing line that emerges gradually. A Quality of Life update adds pre-race setup screen and lap-delta HUD customisation.""",
    },
    {
        "id": 74, "category": """Nintendo""",
        "tag": """news""", "tag_class": """tag-nin""",
        "headline": """Nintendo Switch 2 Hits 12 Million Units in 60 Days — Fastest Console Launch Ever""",
        "summary": """Nintendo confirmed the Switch 2 sold 12 million units in its first 60 days, surpassing the Wii and original Switch to become the fastest-selling dedicated gaming console in history.""",
        "author": """Yuki Tanaka""", "date": """2026-04-10""",
        "score": None,
        "image": """https://img.asmedia.epimg.net/resizer/v2/TST46A4DI5DD5IKEPZXZULFLLI.jpg?auth=985ef270393aaa6d2a59acb5ee7216601270dcec48ea37a416c57a33ea8c646d&width=1472&height=828&smart=true""",
        "image_position": """50% 50%""",
        "featured": False,
        "body": """Nintendo confirmed the Switch 2 sold 12 million units in its first 60 days, surpassing both the Wii and original Switch to claim the title of fastest-selling dedicated gaming console in history.

President Furukawa credited the strong launch lineup including Mario Kart World and Donkey Kong Odyssey. Switch 1 game compatibility has been validated across 94% of the released library.""",
    },
    {
        "id": 75, "category": """Nintendo""",
        "tag": """update""", "tag_class": """tag-nin""",
        "headline": """Mario Kart World DLC Wave 1: Two New Cups, 16 Racers and Mirror Online Mode""",
        "summary": """Nintendo confirmed the first paid DLC wave for Mario Kart World, bringing two new cups with eight tracks each, 16 new playable characters and a new Mirror Online ranked mode.""",
        "author": """Hana Watanabe""", "date": """2026-04-08""",
        "score": None,
        "image": """https://gaming-cdn.com/images/news/articles/12729/cover/mas-contenido-del-mundo-abierto-de-mario-kart-world-cover6835e33b0e111.jpg""",
        "image_position": """75% 48%""",
        "featured": False,
        "body": """Nintendo confirmed Mario Kart World DLC Wave 1 arriving in June. The Starlight Cup features Mario Galaxy-inspired tracks while the Underworld Cup features Bowser castles in the 3D open-world treatment.

Sixteen new racers join the roster including Pauline, Kamek, and Waluigi. Mirror Online is a new ranked mode exclusive to online play. Wave 1 DLC is included in the Nintendo Switch Online Expansion Pass.""",
    },
    {
        "id": 76, "category": """Nintendo""",
        "tag": """news""", "tag_class": """tag-nin""",
        "headline": """Metroid Prime 4: Beyond Ships June 5 With Switch 2 Enhanced Version Confirmed""",
        "summary": """Nintendo set June 5 as the release date for Metroid Prime 4: Beyond, confirming a Switch 2 enhanced version running at 4K 60fps with HDR and new environmental detail settings.""",
        "author": """Yuki Tanaka""", "date": """2026-04-06""",
        "score": None,
        "image": """https://lootlevelchill.com/wp-content/uploads/2025/12/Metroid-Prime-4-screenshot.webp""",
        "image_position": """53% 100%""",
        "featured": False,
        "body": """Nintendo set June 5 as the release date for Metroid Prime 4: Beyond. The Switch 2 enhanced version runs at 4K 60fps via the dock with HDR and new environmental detail settings.

The enhanced version adds a new Exploration Mode that disables combat for atmosphere immersion. Retro Studios confirmed the game runs approximately 18 hours on a first playthrough with 100% completion extending to 30+ hours.""",
    },
    {
        "id": 77, "category": """Nintendo""",
        "tag": """news""", "tag_class": """tag-nin""",
        "headline": """Pokémon Legends: Z-A Arrives September 12 — Lumiose City Fully 3D Open World""",
        "summary": """The Pokémon Company confirmed Pokémon Legends: Z-A launches September 12, featuring a fully 3D open-world Lumiose City with day-night cycles and a new Mega Awakening mechanic.""",
        "author": """Hana Watanabe""", "date": """2026-04-04""",
        "score": None,
        "image": """https://media.es.wired.com/photos/68f651814ea4ad05e5e77397/16:9/w_2560%2Cc_limit/Pokemon-Legends-ZA-Cover.jpg""",
        "image_position": """65% 69%""",
        "featured": False,
        "body": """The Pokemon Company confirmed Pokemon Legends Z-A launches September 12 worldwide. The game features a fully 3D open-world Lumiose City with over 800 buildings, a working tram system, and a day-night cycle.

The new Mega Awakening mechanic differs from standard Mega Evolution by being available in the field. A Co-op Expedition mode lets two players explore together with shared progress.""",
    },
    {
        "id": 78, "category": """Nintendo""",
        "tag": """gaming""", "tag_class": """tag-nin""",
        "headline": """Donkey Kong Odyssey Review — 9.2 / 10""",
        "summary": """Donkey Kong Odyssey is a triumphant return for the franchise, blending the feel of classic DK Country with a fresh world-exploration structure that rivals Super Mario Odyssey in ambition.""",
        "author": """Yuki Tanaka""", "date": """2026-04-02""",
        "score": 9.2,
        "image": """https://images.immediate.co.uk/production/volatile/sites/3/2025/07/donkey-kong-bananza-levels-layers-list-1476409.jpg""",
        "image_position": """58% 41%""",
        "featured": False,
        "body": """Donkey Kong Odyssey is the game fans of the franchise have been waiting decades for. Nintendo EPD applies the Moon-collecting structure of Super Mario Odyssey to a jungle-hopping world tour — it works magnificently.

The barrel-rolling feel is preserved in 3D, with wall jumps carrying the satisfying weight of DKC Returns. The new Ground Surge move that charges through terrain while accruing combo multipliers is instantly iconic. Each of the nine worlds holds several hours of content. An easy recommendation.""",
    },
    {
        "id": 79, "category": """Nintendo""",
        "tag": """news""", "tag_class": """tag-nin""",
        "headline": """Kirby and the Crystal Stars Announced for Switch 2 with Four-Player Co-op""",
        "summary": """HAL Laboratory announced Kirby and the Crystal Stars for Switch 2, bringing back four-player co-op, a new Star Weave copy ability, and the largest Kirby world map ever designed.""",
        "author": """Hana Watanabe""", "date": """2026-03-30""",
        "score": None,
        "image": """https://a.storyblok.com/f/178900/3840x2157/c598f21c98/kirby-sw2.webp""",
        "image_position": """50% 66%""",
        "featured": False,
        "body": """HAL Laboratory announced Kirby and the Crystal Stars for Switch 2. The Star Weave system allows fusions like Fire plus Ice for a Steam Knight ability or Sword plus Bomb for a Blast Blade — over 200 combinations.

The game world is a continuous landscape of seven interconnected kingdoms without loading screens. Crystal Stars releases holiday 2026 and will support Switch 1 at reduced visual settings.""",
    },
    {
        "id": 80, "category": """Nintendo""",
        "tag": """update""", "tag_class": """tag-nin""",
        "headline": """Zelda: Echoes of Wisdom Expansion Pass — Two New Dungeons and a New Villain""",
        "summary": """Nintendo announced an Expansion Pass for The Legend of Zelda: Echoes of Wisdom, adding two new dungeons, a new antagonist and a Hard Mode variant of the full game.""",
        "author": """Yuki Tanaka""", "date": """2026-03-27""",
        "score": None,
        "image": """https://npr.brightspotcdn.com/dims3/default/strip/false/crop/1920x1080+0+0/resize/1920x1080!/?url=http%3A%2F%2Fnpr-brightspot.s3.amazonaws.com%2F97%2F08%2Ff13590ed48349dcdfbd2a03cf5f5%2Fswitch-thelegendofzelda-echoesofwisdom-scrn-18.jpg""",
        "image_position": """50% 71%""",
        "featured": False,
        "body": """Nintendo announced the paid Expansion Pass for Zelda Echoes of Wisdom. The first dungeon involves navigating a location across three different historical time periods. The second is an underwater palace with water pressure mechanics.

The new villain is described as an echo of a previous Zelda-world figure. The Expansion Pass costs $19.99 and arrives alongside a free update adding Boss Rematch Mode and a photo challenge quest.""",
    },
    {
        "id": 81, "category": """PC""",
        "tag": """hardware""", "tag_class": """tag-pc""",
        "headline": """NVIDIA GeForce RTX 6090 Ti Official: 2x RTX 5090 Raster, 3x Ray-Tracing Performance""",
        "summary": """NVIDIA officially announced the GeForce RTX 6090 Ti, delivering twice the raster throughput of the RTX 5090 and three times the ray-tracing performance at 4K with DLSS 4 enabled.""",
        "author": """Marcus Webb""", "date": """2026-04-11""",
        "score": None,
        "image": """https://www.nvidia.com/content/dam/en-zz/Solutions/geforce/graphic-cards/50-series/geforce-rtx-50series-og-1200x630.jpg""",
        "image_position": """56% 100%""",
        "featured": False,
        "body": """NVIDIA officially announced the RTX 6090 Ti, built on the Blackwell GB202 Ultra die with 24,576 CUDA cores and 48GB of GDDR7X memory. Benchmark results show twice the raster throughput of the RTX 5090 and three times the ray-tracing frame rates at 4K.

TDP is 575W, requiring a 1000W PSU. The RTX 6090 Ti launches May 20 at $2,199 MSRP, with the 6090 non-Ti following in July at $1,699.""",
    },
    {
        "id": 82, "category": """PC""",
        "tag": """exclusive""", "tag_class": """tag-pc""",
        "headline": """Half-Life 3 Confirmed: Valve Announces 2027 Release and Portal Crossover Storyline""",
        "summary": """Valve officially announced Half-Life 3 with a 2027 release date and confirmation of a Portal storyline crossover involving GLaDOS as an unlikely ally against the Combine.""",
        "author": """Elena Volkov""", "date": """2026-04-09""",
        "score": None,
        "image": """https://sm.ign.com/t/ign_latam/news/d/details-of/details-of-multiple-cancelled-valve-projects-revealed-includ_bgb3.1280.jpg""",
        "image_position": """58% 0%""",
        "featured": False,
        "body": """Valve officially announced Half-Life 3 with a 2027 release. Gordon Freeman returns 20 years after the Combine occupation collapsed. GLaDOS serves as an unlikely intelligence-sharing ally through Aperture Science infrastructure.

Source 2 powers the game with native VR support via the Index 2 headset. A simultaneous Steam Deck version is planned from launch day. Gaming forums have essentially broken the internet.""",
    },
    {
        "id": 83, "category": """PC""",
        "tag": """hardware""", "tag_class": """cat-pc""",
        "headline": """AMD Radeon RX 9090 XT Matches RTX 6090 in Rasterisation, Undercuts by $400""",
        "summary": """AMD revealed the Radeon RX 9090 XT, a flagship RDNA 5 GPU that matches NVIDIA RTX 6090 Ti rasterisation performance at a $400 lower price, though ray-tracing still lags behind.""",
        "author": """Marcus Webb""", "date": """2026-04-07""",
        "score": None,
        "image": """https://images.unsplash.com/photo-1591488320449-011701bb6704?w=900""",
        "image_position": """50% 50%""",
        "featured": False,
        "body": """AMD revealed the Radeon RX 9090 XT on RDNA 5 architecture. Benchmark results show it matching the RTX 6090 Ti in rasterisation while launching at $1,799 — $400 less than the NVIDIA flagship.

The ray-tracing gap remains at 25-35% behind NVIDIA. The RX 9090 XT ships with 32GB of GDDR7 memory and a 450W TDP. AMD is bundling three months of Xbox Game Pass PC with every 9090 series card.""",
    },
    {
        "id": 84, "category": """PC""",
        "tag": """news""", "tag_class": """tag-pc""",
        "headline": """GTA VI PC Confirmed for March 2027 with 8K Support and DLSS 4""",
        "summary": """Rockstar Games confirmed GTA VI will arrive on PC in March 2027, six months after the console launch, with 8K resolution support, DLSS 4, ray reconstruction, and Vulkan API.""",
        "author": """Elena Volkov""", "date": """2026-04-05""",
        "score": None,
        "image": """https://www.memorypc.es/media/f4/6a/1c/1772191851/GTA_6_Release.jpg?ts=1772191851""",
        "image_position": """54% 6%""",
        "featured": False,
        "body": """Rockstar confirmed GTA VI arrives on PC in March 2027 with 8K support, DLSS 4, Ray Reconstruction, and a Vulkan API backend. The PC version is being developed by a dedicated team including veterans from the GTA V and Red Dead Redemption 2 PC ports.

Minimum specifications require an RTX 4070 equivalent and 24GB of RAM. An NVIDIA-exclusive Neural City feature uses Tensor cores to generate pedestrian animations procedurally, reducing the Vice City memory footprint by 30%.""",
    },
    {
        "id": 85, "category": """PC""",
        "tag": """gaming""", "tag_class": """tag-pc""",
        "headline": """Baldur's Gate 4 Review — 9.5 / 10""",
        "summary": """Baldur's Gate 4 is a staggering achievement — a sequel that honours the legacy of the franchise while pushing role-playing games to a new standard of depth, freedom and emotional resonance.""",
        "author": """Marcus Webb""", "date": """2026-04-03""",
        "score": 9.5,
        "image": """https://gaming-cdn.com/images/news/articles/2658/cover/1000x563/ya-esta-aqui-el-primer-gran-parche-de-baldur-s-gate-3-con-mas-de-1-000-correcciones-cover64e8be6f4956f.jpg""",
        "image_position": """62% 0%""",
        "featured": False,
        "body": """Baldur Gate 4 is a staggering achievement. The game begins six months after the Absolute Cult is defeated. Your protagonist can import a BG3 save to carry narrative decisions forward — the best cross-game save import ever tested.

Combat on Tactician difficulty is the finest turn-based challenge available in any RPG. Enemy AI adapts to tactical patterns across encounters within the same playthrough. Baldur Gate 4 is essential. Clear your calendar.""",
    },
    {
        "id": 86, "category": """PC""",
        "tag": """news""", "tag_class": """cat-pc""",
        "headline": """Steam Spring Sale Breaks Records: 145 Million Users and $2.1B in Transactions""",
        "summary": """Valve's Spring Sale set platform records with 145 million active users and $2.1 billion in transactions over ten days, with GTA VI pre-orders and Baldur's Gate 4 dominating the chart.""",
        "author": """Elena Volkov""", "date": """2026-04-01""",
        "score": None,
        "image": """https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?w=900""",
        "image_position": """50% 50%""",
        "featured": False,
        "body": """Valve Spring Sale set records with 145 million unique active users and $2.1 billion in transactions. GTA VI pre-orders led the chart, followed by Baldur Gate 4 and Half-Life 3 pre-orders despite none being discounted.

The Steam Deck OLED 2 broke into the top ten hardware bestsellers globally. Valve updated the Steam Points Shop with animated backgrounds from upcoming releases during the sale.""",
    },
    {
        "id": 87, "category": """PC""",
        "tag": """news""", "tag_class": """tag-pc""",
        "headline": """Diablo V Announced for PC and Consoles with 2028 Release and Offline Mode""",
        "summary": """Blizzard officially announced Diablo V with a cinematic trailer, confirming a 2028 release across PC, PS5, Xbox Series and Switch 2, with a fully offline single-player mode confirmed.""",
        "author": """Marcus Webb""", "date": """2026-03-29""",
        "score": None,
        "image": """https://cdn.mos.cms.futurecdn.net/RF22r6dPKodUTeQmGFmmTL.jpg""",
        "image_position": """69% 0%""",
        "featured": False,
        "body": """Blizzard officially announced Diablo V for 2028 across all major platforms with a fully offline single-player mode. Two new classes join: the Archon, a celestial mage, and the Warden who fights alongside a spirit bear companion.

Blizzard confirmed no Battle Pass and all endgame updates are included free for two years. Microtransactions are limited to cosmetics only. The announcement generated the highest pre-registration count in Blizzard history.""",
    },
    {
        "id": 88, "category": """eSports""",
        "tag": """news""", "tag_class": """tag-esports""",
        "headline": """T1 Wins Worlds 2026: Faker Claims Record Eighth World Championship Title""",
        "summary": """T1 claimed the League of Legends World Championship 2026, with Faker lifting his record eighth Summoner's Cup after a 3-1 victory over Cloud9 in the Seoul final watched by 120 million viewers.""",
        "author": """Jamie Leung""", "date": """2026-04-10""",
        "score": None,
        "image": """https://esportsinsider.com/wp-content/uploads/2025/11/league-of-legends-worlds-2026-texas-new-york.jpg""",
        "image_position": """55% 20%""",
        "featured": False,
        "body": """T1 claimed the League of Legends World Championship 2026, with Faker lifting his record eighth Summoners Cup after a 3-1 victory over Cloud9 in a sold-out Seoul final watched by 120 million viewers.

Faker played Azir and Syndra across the four games, receiving a standing ovation lasting several minutes. Cloud9 became the first North American team to contest a Worlds final since 2018. T1 receive $2.5 million in prize money.""",
    },
    {
        "id": 89, "category": """eSports""",
        "tag": """news""", "tag_class": """tag-esports""",
        "headline": """CS2 Major Copenhagen: s1mple Returns from Retirement to Lead NaVi to Grand Final""",
        "summary": """Oleksandr s1mple Kostyliev rejoined NaVi for the Copenhagen Major after 18 months in retirement, leading the team to the Grand Final before falling to MOUZ in overtime.""",
        "author": """Ryan Torres""", "date": """2026-04-08""",
        "score": None,
        "image": """https://gaming-cdn.com/images/news/articles/3011/cover/si-counter-strike-2-es-free-to-play-cover651522e8c1178.jpg""",
        "image_position": """58% 13%""",
        "featured": False,
        "body": """Oleksandr s1mple rejoined NaVi for the Copenhagen Major after 18 months in retirement. He posted a 1.31 tournament rating and a 40-kill performance in the NaVi semifinal against FaZe.

NaVi reached the Grand Final — their first since 2022 — before falling 16-19 to MOUZ in overtime. S1mple confirmed he will remain active through 2027 with a goal to win one more Major. Peak Twitch viewership hit 1.2 million, a CS2 record.""",
    },
    {
        "id": 90, "category": """eSports""",
        "tag": """news""", "tag_class": """tag-esports""",
        "headline": """Valorant Champions 2026 Finals Break Esports Viewership Record with 4.2M Peak""",
        "summary": """Valorant Champions 2026 set a new esports viewership record with 4.2 million concurrent viewers for the Grand Final between Team Vitality and Paper Rex.""",
        "author": """Jamie Leung""", "date": """2026-04-06""",
        "score": None,
        "image": """https://cmsassets.rgpub.io/sanity/images/dsfx7636/news/aefe3c7dbe39ef1da3f4241f4c6b771c535038fc-1920x1080.jpg?accountingTag=VAL""",
        "image_position": """70% 1%""",
        "featured": False,
        "body": """Valorant Champions 2026 set a new esports viewership peak record with 4.2 million concurrent viewers for the Grand Final between Team Vitality and Paper Rex.

Paper Rex claimed the Champions title in a five-map series. The viewership surge was partly attributed to Riot broadcasting the event on Netflix in twelve markets. Riot confirmed the Netflix deal extends to VCT 2027 Masters.""",
    },
    {
        "id": 91, "category": """eSports""",
        "tag": """news""", "tag_class": """tag-esports""",
        "headline": """Dota 2 The International 2026: Team Liquid Claims $40M Grand Prize in Singapore""",
        "summary": """Team Liquid claimed The International 2026 crown in Singapore, defeating PSG.LGD in a thrilling 3-2 Grand Final to claim the $40 million prize, the largest in esports history.""",
        "author": """Ryan Torres""", "date": """2026-04-04""",
        "score": None,
        "image": """https://img.redbull.com/images/c_limit,w_1500,h_1000/f_auto,q_auto/redbullcom/2017/08/06/7e51070d-86dd-4142-9949-e08fe4274b77/dota-2""",
        "image_position": """60% 26%""",
        "featured": False,
        "body": """Team Liquid claimed The International 2026 crown in Singapore, defeating PSG.LGD in a five-game Grand Final to claim $40 million — the largest single prize in esports history.

Carry Nisha delivered back-to-back Morphling performances in Games 4 and 5 called the best two consecutive Dota games ever played. Valve president Gabe Newell appeared on stage to present the Aegis in a surprise appearance. Peak concurrent viewership hit 3.1 million, a Dota record.""",
    },
    {
        "id": 92, "category": """eSports""",
        "tag": """news""", "tag_class": """tag-esports""",
        "headline": """Overwatch World Cup Returns in 2026: 36 Nations, LAN Finals at Blizzcon""",
        "summary": """Blizzard confirmed the Overwatch World Cup returns in 2026 after a three-year hiatus, with 36 national teams competing in regional qualifiers before a LAN Grand Final at Blizzcon in November.""",
        "author": """Jamie Leung""", "date": """2026-04-02""",
        "score": None,
        "image": """https://bnetcmsus-a.akamaihd.net/cms/page_media/1I7C4ZDOWWIE1731050111113.png""",
        "image_position": """57% 46%""",
        "featured": False,
        "body": """Blizzard confirmed the Overwatch World Cup returns in 2026 after a three-year hiatus. Thirty-six national teams will compete across four regional qualifier stages before a LAN Grand Final at Blizzcon in November.

The returning format allows players from OWL rosters to represent their home nations. Prize pools are $5 million for the finals. Broadcasting rights sold to ESPN, Twitch, and YouTube Gaming for APAC markets.""",
    },
    {
        "id": 93, "category": """eSports""",
        "tag": """news""", "tag_class": """tag-esports""",
        "headline": """EVO 2026: Daigo Umehara Claims Street Fighter 6 Title at Age 44""",
        "summary": """Daigo Umehara claimed the EVO 2026 Street Fighter 6 championship at age 44, defeating defending champion MenaRD to claim his fourth EVO title.""",
        "author": """Ryan Torres""", "date": """2026-03-31""",
        "score": None,
        "image": """https://www.allkeyshop.com/blog/wp-content/uploads/evo-2026-dates.webp""",
        "image_position": """53% 100%""",
        "featured": False,
        "body": """Daigo Umehara claimed the EVO 2026 Street Fighter 6 championship at 44 years old, defeating MenaRD in the Grand Final with a Ryu performance that drew an immediate standing ovation from the Las Vegas crowd.

His parry reads in the Grand Final set were described by professionals as being at a level nobody in the world could match. The victory gives Daigo his fourth EVO title across Street Fighter 3, SF4, and two SF6 crowns.""",
    },
    {
        "id": 94, "category": """eSports""",
        "tag": """news""", "tag_class": """tag-esports""",
        "headline": """RLCS 2026 World Championship: NRG Defeats Vitality in Historic 7-Game Series""",
        "summary": """NRG Esports claimed the RLCS 2026 World Championship after defeating Team Vitality in the longest Grand Final in Rocket League Championship Series history, decided in double overtime.""",
        "author": """Jamie Leung""", "date": """2026-03-29""",
        "score": None,
        "image": """https://cdn.sanity.io/images/6znhzi10/production/ef5e6ab87a110dbee238e8b07212a0fb0f3dcb3c-1920x1080.jpg?w=1600&auto=format""",
        "image_position": """50% 50%""",
        "featured": False,
        "body": """NRG Esports claimed the RLCS 2026 World Championship in a seven-game Grand Final — the longest in RLCS history. The decisive game went to double overtime before jstn scored a ceiling shot redirect to end the tournament.

RLCS 2026 set a new concurrent viewer record of 820,000, a 40% increase over the previous year. The championship comes with a $500,000 prize and automatic qualification for next season World Championship group stage.""",
    },
    {
        "id": 95, "category": """eSports""",
        "tag": """news""", "tag_class": """tag-esports""",
        "headline": """Rainbow Six Siege World Cup: FURIA Reaches Grand Final as Brazil's Best-Ever R6 Result""",
        "summary": """FURIA Esports reached the Rainbow Six Siege World Cup Grand Final, the best result ever for a Brazilian team, before falling to Fnatic in a closely contested 3-2 series.""",
        "author": """Ryan Torres""", "date": """2026-03-27""",
        "score": None,
        "image": """https://i.blogs.es/7278f8/rainbowsixsiege/1366_2000.jpg""",
        "image_position": """51% 55%""",
        "featured": False,
        "body": """FURIA Esports reached the Rainbow Six Siege World Cup Grand Final in the best result ever for a Brazilian team. FURIA defeated reigning champions Team Empire in the semifinal in a 3-0 sweep that shocked every analyst.

The Grand Final against Fnatic was decided by a single round in Map 5 Clubhouse. Brazilian player HerdsZ was named tournament MVP despite being on the losing team. FURIA take home $200,000.""",
    },
    {
        "id": 96, "category": """Mobile""",
        "tag": """update""", "tag_class": """tag-mobile""",
        "headline": """Pokemon GO Spring Festival 2026 Brings Mythical Pecharunt and 12-Hour Community Day""",
        "summary": """Niantic announced the Spring Festival 2026 for Pokemon GO, introducing Mythical Pecharunt as a Timed Research exclusive and a 12-hour Community Day for Rowlet.""",
        "author": """Kenji Matsuda""", "date": """2026-04-10""",
        "score": None,
        "image": """https://lh3.googleusercontent.com/_hpVC_FfXKyiyQyAScEHT19zmprSPm6N_MueVEAod5KJNfDvl3LvZntgsY2Q6dscc2y-CSr8Tq5EOVgoFrli6EhyOWt_kTRKqh2S=s0-e365""",
        "image_position": """60% 51%""",
        "featured": False,
        "body": """Niantic announced the Pokemon GO Spring Festival 2026, introducing Mythical Pecharunt as a Timed Research exclusive. Rowlet Community Day runs for 12 hours — the most requested CD Pokemon in the community survey.

The festival runs over two weekends with double XP, triple Stardust, and reduced hatching distances. Niantic also confirmed the long-awaited cross-trainer battle feature enters beta during the festival.""",
    },
    {
        "id": 97, "category": """Mobile""",
        "tag": """update""", "tag_class": """tag-mobile""",
        "headline": """Genshin Impact 5.8 Concludes Natlan Arc with Pyro Archon Boss Fight""",
        "summary": """HoYoverse revealed Genshin Impact 5.8, which concludes the Natlan storyline with the Pyro Archon boss fight, adds two new characters and introduces Co-op Exploration Mode for the first time.""",
        "author": """Lena Fischer""", "date": """2026-04-08""",
        "score": None,
        "image": """https://static0.gamerantimages.com/wordpress/wp-content/uploads/2022/09/genshin-impact-mobile-3-billion-revenue-2.jpg""",
        "image_position": """64% 0%""",
        "featured": False,
        "body": """HoYoverse revealed Genshin Impact 5.8, the update concluding the Natlan main storyline with the multi-phase Pyro Archon boss fight.

The update adds Citlali, a new five-star Cryo catalyst user, and Iansan, a four-star Electro bow user. A Co-op Exploration Mode allows up to four players to traverse open-world Natlan together — the most significant co-op expansion in Genshin history. The update deploys globally on April 23.""",
    },
    {
        "id": 98, "category": """Mobile""",
        "tag": """update""", "tag_class": """tag-mobile""",
        "headline": """Call of Duty: Mobile Season 5 Adds Verdansk Map and Ranked 2.0 System""",
        "summary": """Activision confirmed Call of Duty Mobile Season 5, introducing the legendary Verdansk Warzone map adapted for mobile, three iconic operator skins and a fully rebuilt Ranked 2.0 system.""",
        "author": """Kenji Matsuda""", "date": """2026-04-06""",
        "score": None,
        "image": """https://www.callofduty.com/content/dam/atvi/callofduty/cod-touchui/mobile/home/gamemodes/GameModes_Multiplayer.webp""",
        "image_position": """50% 50%""",
        "featured": False,
        "body": """Activision confirmed Call of Duty Mobile Season 5, introducing Verdansk adapted for mobile battle royale. Three iconic operator skins feature Ghost, Soap, and Price from Modern Warfare 2.

Ranked 2.0 introduces Champion Division for the top 500 players globally per season, with exclusive animated calling card rewards and a live leaderboard. Season 5 premieres May 1.""",
    },
    {
        "id": 99, "category": """Mobile""",
        "tag": """update""", "tag_class": """tag-mobile""",
        "headline": """Clash of Clans Builder Base 3.0 Arrives with Mega Builder Mechanics and PvE Raids""",
        "summary": """Supercell released Builder Base 3.0 for Clash of Clans, a complete redesign with a new Mega Builder mechanics system, 15 fully redesigned building layouts and PvE raid challenges.""",
        "author": """Lena Fischer""", "date": """2026-04-04""",
        "score": None,
        "image": """https://media.newyorker.com/photos/590977c9019dfc3494ea2f7f/16:9/w_1280,c_limit/Johnston-Clash-Clans.jpg""",
        "image_position": """53% 51%""",
        "featured": False,
        "body": """Supercell released Builder Base 3.0, a complete redesign of the secondary village. The Mega Builder can be assigned to any building to augment its function — assigning it to Cannon creates a miniature X-Bow effect.

Fifteen redesigned layout templates are provided for free. PvE Raid Challenges add cooperative play against AI-controlled villages with communal loot rewards. Builder Base 3.0 is the most-discussed Clash of Clans update since launch.""",
    },
    {
        "id": 100, "category": """Mobile""",
        "tag": """news""", "tag_class": """tag-mobile""",
        "headline": """Roblox Economy Overhaul: Creator Royalties Double, Marketplace Fees Cut by Half""",
        "summary": """Roblox Corporation announced a major economy overhaul doubling creator royalties from 30% to 60% and cutting marketplace transaction fees in half, effective immediately for premium creators.""",
        "author": """Kenji Matsuda""", "date": """2026-04-02""",
        "score": None,
        "image": """https://media.revistagq.com/photos/604f28f7267aa4eef01d2d82/16:9/w_1280,c_limit/Roblox.png""",
        "image_position": """59% 27%""",
        "featured": False,
        "body": """Roblox Corporation announced the most significant economy overhaul in company history. Creator royalties double from 30% to 60% of Robux revenue, and marketplace transaction fees are cut by 50%.

CEO David Baszucki acknowledged pressure from developers directly. An independent analyst firm estimated the creator community will receive an additional $800 million annually. Roblox stock rose 7% on the announcement day.""",
    },
    {
        "id": 101, "category": """Mobile""",
        "tag": """news""", "tag_class": """tag-mobile""",
        "headline": """Apple Arcade Spring Showcase: 12 New Games Including Fez 2 and Sayonara Wild Hearts 2""",
        "summary": """Apple announced 12 new Apple Arcade titles in its Spring Showcase, headlined by Fez 2 and Sayonara Wild Hearts 2, both launching exclusively on Arcade before any other platform.""",
        "author": """Lena Fischer""", "date": """2026-03-31""",
        "score": None,
        "image": """https://i.blogs.es/cdc216/apple_arcade/1366_2000.jpeg""",
        "image_position": """53% 46%""",
        "featured": False,
        "body": """Apple announced 12 new Apple Arcade titles headlined by Fez 2 from Polytron and Sayonara Wild Hearts 2 from Simogo, both launching exclusively on Arcade before any other platform.

Fez 2 expands the dimension-rotation mechanic into a three-dimensional puzzle architecture. Phil Fish confirmed his direct involvement. Both games launch this summer. Apple confirmed price holds for Apple Arcade through end of 2027 at $6.99 monthly.""",
    },
    {
        "id": 102, "category": """Mobile""",
        "tag": """update""", "tag_class": """tag-mobile""",
        "headline": """Diablo Immortal Season 14 Brings Level Cap Increase and Cross-Save with PC""",
        "summary": """Blizzard announced Diablo Immortal Season 14, featuring a level cap increase to 1000, a brand new Runeweaver class and full cross-save synchronisation with the PC client.""",
        "author": """Kenji Matsuda""", "date": """2026-03-29""",
        "score": None,
        "image": """https://i.ytimg.com/vi/Ab2-WW1skOM/maxresdefault.jpg""",
        "image_position": """69% 0%""",
        "featured": False,
        "body": """Blizzard announced Diablo Immortal Season 14 with the first level cap increase since launch — raising the ceiling from 800 to 1000. The new Runeweaver class inscribes magical runes onto enemies mid-combat creating combo interactions.

Cross-save between mobile and PC is fully implemented in Season 14, the most requested Diablo Immortal feature since the PC port launched in 2022. Season 14 launches April 28.""",
    },
    {
        "id": 103, "category": """Mobile""",
        "tag": """update""", "tag_class": """tag-mobile""",
        "headline": """Final Fantasy VII Ever Crisis Chapter 7 Reveals Young Sephiroth's Wutai Campaign""",
        "summary": """Square Enix released Chapter 7 of Final Fantasy VII Ever Crisis, focusing on young Sephiroth's Wutai Campaign and introducing an exclusive Remake continuity tie-in scene.""",
        "author": """Lena Fischer""", "date": """2026-03-27""",
        "score": None,
        "image": """https://static0.srcdn.com/wordpress/wp-content/uploads/2023/09/ff7-ever-crisis-is-still-missing-one-important-but-obvious-feature-an-image-many-of-the-main-cast-members-as-seen-in-gameplay-in-final-fantasy-7-ever-crisis.jpg""",
        "image_position": """55% 69%""",
        "featured": False,
        "body": """Square Enix released Chapter 7 of Final Fantasy VII Ever Crisis, the most story-rich chapter to date. The chapter focuses on young Sephiroth Wutai Campaign, defining his relationship with Genesis and Angeal.

Two new characters join: Hollander as a support with debuff mechanics, and new OC Kael whose backstory connects the Wutai War to the Remake continuity. A new PvP War of Wills mode lets players take Wutai or Shinra-aligned teams into weekly faction wars.""",
    },
    {
        "id": 104, "category": """Mobile""",
        "tag": """news""", "tag_class": """tag-mobile""",
        "headline": """Mobile Gaming Revenue Hits $110 Billion in 2025: Asia Pacific Drives 60% of Total""",
        "summary": """Mobile gaming revenue reached $110 billion globally in 2025 according to Newzoo, with Asia Pacific accounting for 60% and the subscription segment growing 45% year-on-year.""",
        "author": """Kenji Matsuda""", "date": """2026-03-25""",
        "score": None,
        "image": """https://www.verdict.co.uk/wp-content/uploads/2022/09/shutterstock_1934243669.jpg""",
        "image_position": """56% 49%""",
        "featured": False,
        "body": """Mobile gaming revenue reached $110 billion globally in 2025 according to Newzoo. Asia Pacific accounts for 60% driven by China, South Korea, and a resurgent Japanese mobile market. The subscription segment grew 45% year-on-year.

HoYoverse remains the highest-grossing mobile publisher globally. The report predicts mobile gaming will cross $125 billion in 2026, driven by 5G adoption in emerging markets and continued growth of cloud gaming on mobile.""",
    },

]

CATEGORIES = ["PlayStation", "Xbox", "Nintendo", "PC", "eSports", "Mobile"]


def get_all():
    return ARTICLES


def get_by_category(category):
    return [a for a in ARTICLES if a["category"].lower() == category.strip().lower()]


def get_featured():
    return [a for a in ARTICLES if a.get("featured")]
