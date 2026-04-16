"""
sync_seed.py — Run this before committing after editing articles via the admin panel.

What it does:
  Reads every article's current image, image_position, body, and metadata from
  the live DB and rewrites the ARTICLES list in news_data.py so the seed file
  stays in sync with whatever you set in the admin panel.

Usage:
  python backend/sync_seed.py

After running, review with:
  git diff backend/news_data.py
Then commit news_data.py to push the changes to the repo.
"""

import sys, os

sys.path.insert(0, os.path.dirname(__file__))
import db

# ── 1. Pull all articles from DB ───────────────────────────────────────────────
conn = db.get_conn()
rows = conn.execute(
    """SELECT id, category, tag, tag_class, headline, summary, body,
              author, date, score, image, image_position, featured
       FROM articles ORDER BY id"""
).fetchall()
conn.close()

print(f"[sync] Read {len(rows)} articles from DB")

# ── 2. Helpers ─────────────────────────────────────────────────────────────────
def py_str(s):
    """Render a value as a Python literal suitable for news_data.py."""
    if s is None:
        return "None"
    # Use triple-quoted strings so newlines and apostrophes survive safely
    safe = str(s).replace("\\", "\\\\").replace('"""', r'\"\"\"')
    return '"""' + safe + '"""'

def py_val(v):
    """Render a Python value (None, bool, number, or str)."""
    if v is None:
        return "None"
    if isinstance(v, bool):
        return "True" if v else "False"
    if isinstance(v, (int, float)):
        return repr(v)
    return py_str(v)

# ── 3. Build the ARTICLES list source ─────────────────────────────────────────
article_blocks = []
for r in rows:
    score_val    = float(r["score"]) if r["score"] is not None else None
    featured_val = bool(r["featured"])

    block = (
        "    {\n"
        f'        "id": {r["id"]}, "category": {py_str(r["category"])},\n'
        f'        "tag": {py_str(r["tag"])}, "tag_class": {py_str(r["tag_class"])},\n'
        f'        "headline": {py_str(r["headline"])},\n'
        f'        "summary": {py_str(r["summary"])},\n'
        f'        "author": {py_str(r["author"])}, "date": {py_str(r["date"])},\n'
        f'        "score": {py_val(score_val)},\n'
        f'        "image": {py_str(r["image"] or "")},\n'
        f'        "image_position": {py_str(r["image_position"] or "50% 50%")},\n'
        f'        "featured": {py_val(featured_val)},\n'
        f'        "body": {py_str(r["body"] or "")},\n'
        "    },"
    )
    article_blocks.append(block)

articles_source = "\n".join(article_blocks)

# ── 4. Write the complete news_data.py ────────────────────────────────────────
seed_path = os.path.join(os.path.dirname(__file__), "news_data.py")

new_source = '''\
"""
news_data.py — Seed articles for RESPAWN News.
Auto-managed: run  python backend/sync_seed.py  after changing images or
content via the admin panel, then commit the result to keep the repo in sync.
"""

ARTICLES = [

''' + articles_source + '''

]

CATEGORIES = ["PlayStation", "Xbox", "Nintendo", "PC", "eSports", "Mobile"]


def get_all():
    return ARTICLES


def get_by_category(category):
    return [a for a in ARTICLES if a["category"].lower() == category.strip().lower()]


def get_featured():
    return [a for a in ARTICLES if a.get("featured")]
'''

with open(seed_path, "w", encoding="utf-8") as f:
    f.write(new_source)

print(f"[sync] news_data.py rewritten with {len(rows)} articles.")
print("[sync] Review changes:  git diff backend/news_data.py")
print("[sync] Then commit:     git add backend/news_data.py && git commit -m 'sync seed from DB'")
