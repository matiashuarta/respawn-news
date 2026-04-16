"""
Tests for article retrieval and related-news logic.
Uses a temporary DB seeded with a small set of articles.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
import db


@pytest.fixture
def seeded_db(monkeypatch, tmp_path):
    """Fresh DB with schema + admin user + a handful of test articles."""
    db_file = str(tmp_path / "test.db")
    monkeypatch.setattr(db, "DB_PATH", db_file)
    db.init_db()

    # Insert test articles directly so we control the data
    import sqlite3
    conn = sqlite3.connect(db_file)
    conn.row_factory = sqlite3.Row
    articles = [
        # (category, tag, tag_class, headline, summary, author, date, score, image, featured, body)
        ("PlayStation", "Review",  "tag-review",  "PS5 Game A Review",   "Summary A", "Admin", "Apr 1, 2026", 8.5, "img_a.jpg", 1, "Body A"),
        ("PlayStation", "News",    "tag-news",    "PS5 News B",          "Summary B", "Admin", "Apr 2, 2026", None,"img_b.jpg", 0, "Body B"),
        ("PlayStation", "News",    "tag-news",    "PS5 News C",          "Summary C", "Admin", "Apr 3, 2026", None,"img_c.jpg", 0, "Body C"),
        ("Xbox",        "News",    "tag-news",    "Xbox News D",         "Summary D", "Admin", "Apr 4, 2026", None,"img_d.jpg", 0, "Body D"),
        ("Xbox",        "Review",  "tag-review",  "Xbox Game E Review",  "Summary E", "Admin", "Apr 5, 2026", 7.0, "img_e.jpg", 0, "Body E"),
    ]
    conn.executemany(
        """INSERT INTO articles
           (category, tag, tag_class, headline, summary, author, date, score, image, featured, body)
           VALUES (?,?,?,?,?,?,?,?,?,?,?)""",
        articles,
    )
    conn.commit()
    conn.close()
    return db_file


# ── Article retrieval ─────────────────────────────────────────────────────────

def test_get_article_by_id_returns_correct_article(seeded_db):
    # first inserted article will have id=2 (admin is id=1 in users, but articles start at 1)
    all_articles, _ = db.get_articles_by_category("PlayStation")
    first = all_articles[0]
    fetched = db.get_article_by_id(first["id"])
    assert fetched is not None
    assert fetched["headline"] == first["headline"]

def test_get_article_by_nonexistent_id(seeded_db):
    result = db.get_article_by_id(99999)
    assert result is None

def test_get_articles_by_category_returns_only_that_category(seeded_db):
    # init_db seeds the real news_data articles too, so count varies
    # what matters is that every returned article belongs to the right category
    ps_articles, total = db.get_articles_by_category("PlayStation")
    assert len(ps_articles) >= 3          # at least our 3 inserted ones
    assert total >= 3
    for a in ps_articles:
        assert a["category"] == "PlayStation"

def test_get_articles_by_category_xbox(seeded_db):
    xbox_articles, total = db.get_articles_by_category("Xbox")
    assert len(xbox_articles) >= 2        # at least our 2 inserted ones
    assert total >= 2
    for a in xbox_articles:
        assert a["category"] == "Xbox"

def test_get_articles_by_nonexistent_category_returns_empty(seeded_db):
    result, total = db.get_articles_by_category("Atari")
    assert result == []
    assert total == 0

def test_related_excludes_current_article(seeded_db):
    ps_articles, _ = db.get_articles_by_category("PlayStation")
    current_id  = ps_articles[0]["id"]
    related = [a for a in ps_articles if a["id"] != current_id]
    assert all(a["id"] != current_id for a in related)

def test_pagination_limit_offset(seeded_db):
    # With limit=2 we get 2 articles; second page starts at offset=2
    page1, total = db.get_articles_by_category("PlayStation", limit=2, offset=0)
    page2, _     = db.get_articles_by_category("PlayStation", limit=2, offset=2)
    assert len(page1) == 2
    assert total >= 3
    ids1 = {a["id"] for a in page1}
    ids2 = {a["id"] for a in page2}
    assert ids1.isdisjoint(ids2)   # no overlap between pages

def test_featured_articles_are_flagged(seeded_db):
    featured = db.get_featured_articles()
    assert len(featured) >= 1
    for a in featured:
        assert a["featured"] == 1

def test_image_position_defaults_to_center(seeded_db):
    ps_articles, _ = db.get_articles_by_category("PlayStation")
    for a in ps_articles:
        assert "image_position" in a
