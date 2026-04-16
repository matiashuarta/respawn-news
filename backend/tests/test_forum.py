"""
Tests for forum categories, topics, posts, and hot-topic scoring.
Uses a temporary DB seeded via init_db() which inserts the full category list.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
import db


@pytest.fixture
def forum_db(monkeypatch, tmp_path):
    """Fresh DB with full schema, admin user, and seeded forum categories/topics."""
    db_file = str(tmp_path / "forum_test.db")
    monkeypatch.setattr(db, "DB_PATH", db_file)
    db.init_db()
    return db_file


# ── Categories ────────────────────────────────────────────────────────────────

def test_forum_has_18_categories(forum_db):
    cats = db.get_forum_categories()
    assert len(cats) == 18

def test_forum_categories_have_required_fields(forum_db):
    cats = db.get_forum_categories()
    for c in cats:
        assert "id"          in c
        assert "name"        in c
        assert "slug"        in c
        assert "description" in c
        assert "icon"        in c
        assert "color"       in c
        assert "topic_count" in c

def test_general_category_exists(forum_db):
    cats = db.get_forum_categories()
    slugs = [c["slug"] for c in cats]
    assert "general" in slugs

def test_all_expected_slugs_present(forum_db):
    expected = [
        "general", "playstation", "xbox", "nintendo", "pc", "esports",
        "mobile", "vr-ar", "retro", "gamedev", "tech", "deals", "lfg",
        "sports", "movies-tv", "music", "anime", "off-topic",
    ]
    cats  = db.get_forum_categories()
    slugs = [c["slug"] for c in cats]
    for slug in expected:
        assert slug in slugs, f"Missing category slug: {slug}"


# ── Topics ────────────────────────────────────────────────────────────────────

def test_get_topics_for_general_returns_results(forum_db):
    topics, total = db.get_forum_topics(category_slug="general")
    assert total > 0
    assert len(topics) > 0

def test_get_topics_for_nonexistent_category_returns_empty(forum_db):
    topics, total = db.get_forum_topics(category_slug="doesnotexist")
    assert topics == []
    assert total  == 0

def test_create_topic_and_retrieve_it(forum_db):
    # get admin user id
    import sqlite3
    conn = sqlite3.connect(forum_db)
    conn.row_factory = sqlite3.Row
    admin = conn.execute("SELECT id FROM users WHERE role='admin'").fetchone()
    conn.close()

    topic, err = db.create_forum_topic(
        category_slug = "xbox",
        title         = "Test topic created by pytest",
        body          = "This is the opening post body.",
        user_id       = admin["id"],
        username      = "admin",
    )
    assert err   is None
    assert topic is not None
    assert topic["title"] == "Test topic created by pytest"

def test_create_topic_invalid_category_returns_error(forum_db):
    topic, err = db.create_forum_topic(
        category_slug = "fakecategory",
        title         = "Should fail",
        body          = "Body",
        user_id       = 1,
        username      = "admin",
    )
    assert topic is None
    assert err   is not None


# ── Posts ─────────────────────────────────────────────────────────────────────

def test_get_forum_topic_returns_posts(forum_db):
    topics, _ = db.get_forum_topics(category_slug="general")
    assert len(topics) > 0
    topic_id = topics[0]["id"]
    topic, posts = db.get_forum_topic(topic_id)
    assert topic is not None
    assert len(posts) >= 1           # seeded topics have at least the opening post

def test_get_forum_topic_increments_view_count(forum_db):
    topics, _ = db.get_forum_topics(category_slug="general")
    topic_id  = topics[0]["id"]
    topic_before, _ = db.get_forum_topic(topic_id)
    topic_after,  _ = db.get_forum_topic(topic_id)
    assert topic_after["view_count"] == topic_before["view_count"] + 1

def test_get_nonexistent_topic_returns_none(forum_db):
    topic, posts = db.get_forum_topic(99999)
    assert topic is None
    assert posts == []


# ── Stats ─────────────────────────────────────────────────────────────────────

def test_forum_stats_returns_counts(forum_db):
    stats = db.get_forum_stats()
    assert "topics"  in stats
    assert "posts"   in stats
    assert "members" in stats
    assert stats["topics"]  > 0
    assert stats["posts"]   > 0
    assert stats["members"] > 0


# ── Hot topics ────────────────────────────────────────────────────────────────

def test_hot_topics_returns_up_to_5(forum_db):
    hot = db.get_hot_forum_topics(limit=5)
    assert len(hot) <= 5

def test_hot_topics_excludes_pinned(forum_db):
    hot = db.get_hot_forum_topics(limit=10)
    for t in hot:
        assert t["pinned"] == 0

def test_hot_topics_have_hot_score_field(forum_db):
    hot = db.get_hot_forum_topics(limit=5)
    for t in hot:
        assert "hot_score" in t
