"""
server.py — RESPAWN News Backend
Pure Python (stdlib only): http.server + sqlite3

Usage:
    python3 backend/server.py

The server serves:
  • Static files from ../frontend/
  • REST API under /api/
  • Admin API under /api/admin/  (requires role=admin)
"""

import json
import os
import re
import sys
import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer

sys.path.insert(0, os.path.dirname(__file__))

import db

PORT = 8765
FRONTEND_DIR = os.path.join(os.path.dirname(__file__), "..", "frontend")

MIME = {
    ".html": "text/html; charset=utf-8",
    ".css":  "text/css; charset=utf-8",
    ".js":   "application/javascript; charset=utf-8",
    ".json": "application/json",
    ".png":  "image/png",
    ".jpg":  "image/jpeg",
    ".ico":  "image/x-icon",
}

# ── Tag-class helper ──────────────────────────────────────────────────────────

TAG_CLASS_MAP = {
    "playstation": "tag-ps",
    "xbox":        "tag-xbox",
    "nintendo":    "tag-nin",
    "pc":          "tag-pc",
    "esports":     "tag-esports",
    "mobile":      "tag-mobile",
}

def infer_tag_class(category: str) -> str:
    return TAG_CLASS_MAP.get(category.strip().lower(), "tag-pc")


# ── Response helpers ──────────────────────────────────────────────────────────

def _cors_headers(handler):
    handler.send_header("Access-Control-Allow-Origin", "*")
    handler.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
    handler.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")


def json_response(handler, data, status=200):
    body = json.dumps(data, ensure_ascii=False).encode()
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json")
    handler.send_header("Content-Length", str(len(body)))
    _cors_headers(handler)
    handler.end_headers()
    handler.wfile.write(body)


def error_response(handler, message, status=400):
    json_response(handler, {"error": message}, status)


def read_body(handler):
    length = int(handler.headers.get("Content-Length", 0))
    if length == 0:
        return {}
    raw = handler.rfile.read(length)
    try:
        return json.loads(raw)
    except Exception:
        return {}


def get_token(handler):
    auth = handler.headers.get("Authorization", "")
    if auth.startswith("Bearer "):
        return auth[7:].strip()
    return None


def require_auth(handler):
    """Returns user dict or sends 401 and returns None."""
    token = get_token(handler)
    user = db.get_user_by_token(token)
    if not user:
        error_response(handler, "Unauthorized", 401)
        return None
    return user


def require_admin(handler):
    """Returns user dict if role=admin, otherwise sends 401/403 and returns None."""
    user = require_auth(handler)
    if not user:
        return None
    if user.get("role") != "admin":
        error_response(handler, "Forbidden — admin role required", 403)
        return None
    return user


# ── Request Handler ───────────────────────────────────────────────────────────

class RespawnHandler(BaseHTTPRequestHandler):

    def log_message(self, fmt, *args):
        print(f"  {self.address_string()} — {fmt % args}")

    # ── CORS pre-flight ───────────────────────────────────────────────────────
    def do_OPTIONS(self):
        self.send_response(204)
        _cors_headers(self)
        self.end_headers()

    # ── GET ───────────────────────────────────────────────────────────────────
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path   = parsed.path
        params = urllib.parse.parse_qs(parsed.query)

        # /api/news — all articles (optionally filtered by category)
        if path == "/api/news":
            user = require_auth(self)
            if not user:
                return
            category = params.get("category", [None])[0]
            if category:
                articles = db.get_articles_by_category(category)
            else:
                articles = db.get_all_articles()
            return json_response(self, {"articles": articles, "total": len(articles)})

        # /api/news/featured
        if path == "/api/news/featured":
            user = require_auth(self)
            if not user:
                return
            return json_response(self, {"articles": db.get_featured_articles()})

        # /api/news/{id}/related  — same category, excluding this article, max 10
        m = re.match(r"^/api/news/(\d+)/related$", path)
        if m:
            user = require_auth(self)
            if not user:
                return
            article_id = int(m.group(1))
            article    = db.get_article_by_id(article_id)
            if not article:
                return error_response(self, "Article not found", 404)
            related = [
                a for a in db.get_articles_by_category(article["category"])
                if a["id"] != article_id
            ][:10]
            return json_response(self, {"articles": related})

        # /api/news/{id}/comments  (includes per-user votes if ?user_id= provided)
        m = re.match(r"^/api/news/(\d+)/comments$", path)
        if m:
            user = require_auth(self)
            if not user:
                return
            article_id = int(m.group(1))
            comments   = db.get_comments(article_id)
            user_votes = db.get_user_votes(article_id, user["id"])
            return json_response(self, {"comments": comments, "user_votes": user_votes})

        # /api/news/{id}
        m = re.match(r"^/api/news/(\d+)$", path)
        if m:
            user = require_auth(self)
            if not user:
                return
            article = db.get_article_by_id(int(m.group(1)))
            if not article:
                return error_response(self, "Article not found", 404)
            return json_response(self, {"article": article})

        # /api/categories
        if path == "/api/categories":
            import news_data
            return json_response(self, {"categories": news_data.CATEGORIES})

        # /api/me — fresh profile (includes avatar)
        if path == "/api/me":
            user = require_auth(self)
            if not user:
                return
            # Fetch full row so avatar is included
            conn = db.get_conn()
            row = conn.execute(
                "SELECT id, username, email, role, avatar FROM users WHERE id = ?",
                (user["id"],)
            ).fetchone()
            conn.close()
            return json_response(self, {"user": dict(row) if row else user})

        # /api/admin/news — list all articles (admin)
        if path == "/api/admin/news":
            user = require_admin(self)
            if not user:
                return
            articles = db.get_all_articles()
            return json_response(self, {"articles": articles, "total": len(articles)})

        # /api/forum/categories
        if path == "/api/forum/categories":
            user = require_auth(self)
            if not user:
                return
            return json_response(self, {"categories": db.get_forum_categories()})

        # /api/forum/stats
        if path == "/api/forum/stats":
            user = require_auth(self)
            if not user:
                return
            return json_response(self, db.get_forum_stats())

        # /api/forum/topics/hot  (must come before /api/forum/topics/{id})
        if path == "/api/forum/topics/hot":
            user = require_auth(self)
            if not user:
                return
            return json_response(self, {"topics": db.get_hot_forum_topics()})

        # /api/forum/me/rank  — current user's forum post count + rank label
        if path == "/api/forum/me/rank":
            user = require_auth(self)
            if not user:
                return
            count = db.get_user_forum_post_count(user["id"])
            if count >= 200: rank = "Legend"
            elif count >= 50: rank = "Veteran"
            elif count >= 10: rank = "Regular"
            elif count >= 1:  rank = "Recruit"
            else:              rank = "Lurker"
            return json_response(self, {"post_count": count, "rank": rank})

        # /api/forum/rules  — returns the ID of the rules topic
        if path == "/api/forum/rules":
            user = require_auth(self)
            if not user:
                return
            topic_id = db.get_forum_rules_topic_id()
            return json_response(self, {"topic_id": topic_id})

        # /api/forum/topics  (all or ?category=slug)
        if path == "/api/forum/topics":
            user = require_auth(self)
            if not user:
                return
            cat   = params.get("category", [None])[0]
            page  = int(params.get("page", ["1"])[0])
            topics, total = db.get_forum_topics(cat, page)
            return json_response(self, {"topics": topics, "total": total})

        # /api/forum/topics/{id}
        m = re.match(r"^/api/forum/topics/(\d+)$", path)
        if m:
            user = require_auth(self)
            if not user:
                return
            topic, posts = db.get_forum_topic(int(m.group(1)))
            if not topic:
                return error_response(self, "Topic not found", 404)
            return json_response(self, {"topic": topic, "posts": posts})

        # Static files
        self._serve_static(path)

    # ── POST ──────────────────────────────────────────────────────────────────
    def do_POST(self):
        path = urllib.parse.urlparse(self.path).path
        body = read_body(self)

        # Auth: register
        if path == "/api/auth/register":
            username = (body.get("username") or "").strip()
            email    = (body.get("email")    or "").strip()
            password = (body.get("password") or "").strip()

            if not username or not email or not password:
                return error_response(self, "All fields are required")
            if len(password) < 6:
                return error_response(self, "Password must be at least 6 characters")
            if "@" not in email:
                return error_response(self, "Invalid email address")

            user, err = db.register_user(username, email, password)
            if err:
                return error_response(self, err)

            token, user, err = db.login_user(email, password)
            if err:
                return error_response(self, err)
            return json_response(self, {"token": token, "user": user}, 201)

        # Auth: login
        if path == "/api/auth/login":
            email    = (body.get("email")    or "").strip()
            password = (body.get("password") or "").strip()

            if not email or not password:
                return error_response(self, "Email and password are required")

            token, user, err = db.login_user(email, password)
            if err:
                return error_response(self, err, 401)
            return json_response(self, {"token": token, "user": user})

        # Auth: logout
        if path == "/api/auth/logout":
            token = get_token(self)
            if token:
                db.logout_user(token)
            return json_response(self, {"ok": True})

        # POST comment on article (top-level or reply via parent_id)
        m = re.match(r"^/api/news/(\d+)/comments$", path)
        if m:
            user = require_auth(self)
            if not user:
                return
            article_id = int(m.group(1))
            if not db.get_article_by_id(article_id):
                return error_response(self, "Article not found", 404)
            comment_body = (body.get("body") or "").strip()
            if not comment_body:
                return error_response(self, "Comment body is required")
            if len(comment_body) > 1000:
                return error_response(self, "Comment must be 1000 characters or less")
            parent_id = body.get("parent_id")
            if parent_id is not None:
                parent_id = int(parent_id)
            comment, err = db.add_comment(article_id, user["id"], user["username"], comment_body, parent_id)
            if err:
                return error_response(self, err)
            return json_response(self, {"comment": comment}, 201)

        # POST vote on a comment  /api/comments/{id}/vote
        m = re.match(r"^/api/comments/(\d+)/vote$", path)
        if m:
            user = require_auth(self)
            if not user:
                return
            comment_id = int(m.group(1))
            vote = body.get("vote")
            if vote not in (1, -1, 0):
                return error_response(self, "vote must be 1, -1, or 0")
            likes, dislikes, user_vote, err = db.vote_comment(comment_id, user["id"], vote)
            if err:
                return error_response(self, err, 404 if "not found" in err.lower() else 400)
            return json_response(self, {"likes": likes, "dislikes": dislikes, "user_vote": user_vote})

        # Admin: create article
        if path == "/api/admin/news":
            user = require_admin(self)
            if not user:
                return

            headline = (body.get("headline") or "").strip()
            summary  = (body.get("summary")  or "").strip()
            category = (body.get("category") or "").strip()
            tag      = (body.get("tag")      or "").strip()
            author   = (body.get("author")   or "").strip()
            date     = (body.get("date")     or "").strip()
            image    = (body.get("image")    or "").strip()

            if not all([headline, summary, category, tag, author, date, image]):
                return error_response(self, "All fields are required")

            tag_class = body.get("tag_class") or infer_tag_class(category)

            article_data = {
                "category":  category,
                "tag":       tag,
                "tag_class": tag_class,
                "headline":  headline,
                "summary":   summary,
                "author":    author,
                "date":      date,
                "score":     body.get("score"),
                "image":     image,
                "featured":  bool(body.get("featured", False)),
                "body":      (body.get("body") or "").strip(),
            }

            article, err = db.create_article(article_data)
            if err:
                return error_response(self, err)
            return json_response(self, {"article": article}, 201)

        # POST /api/forum/topics — create new topic
        if path == "/api/forum/topics":
            user = require_auth(self)
            if not user:
                return
            cat_slug = (body.get("category") or "").strip()
            title    = (body.get("title")    or "").strip()
            txt      = (body.get("body")     or "").strip()
            if not cat_slug or not title or not txt:
                return error_response(self, "category, title and body are required")
            if len(title) > 200:
                return error_response(self, "Title must be 200 characters or less")
            if len(txt) > 5000:
                return error_response(self, "Post must be 5000 characters or less")
            topic, err = db.create_forum_topic(cat_slug, title, txt, user["id"], user["username"])
            if err:
                return error_response(self, err)
            return json_response(self, {"topic": topic}, 201)

        # POST /api/forum/topics/{id}/posts — reply in a topic
        m = re.match(r"^/api/forum/topics/(\d+)/posts$", path)
        if m:
            user = require_auth(self)
            if not user:
                return
            txt = (body.get("body") or "").strip()
            if not txt:
                return error_response(self, "Post body is required")
            if len(txt) > 5000:
                return error_response(self, "Post must be 5000 characters or less")
            post, err = db.create_forum_post(int(m.group(1)), txt, user["id"], user["username"])
            if err:
                return error_response(self, err)
            return json_response(self, {"post": post}, 201)

        # POST /api/forum/posts/{id}/like
        m = re.match(r"^/api/forum/posts/(\d+)/like$", path)
        if m:
            user = require_auth(self)
            if not user:
                return
            result, err = db.toggle_forum_post_like(int(m.group(1)), user["id"])
            if err:
                return error_response(self, err)
            return json_response(self, result)

        error_response(self, "Not found", 404)

    # ── PUT ───────────────────────────────────────────────────────────────────
    def do_PUT(self):
        path = urllib.parse.urlparse(self.path).path
        body = read_body(self)

        # /api/comments/{id} — edit own comment
        m = re.match(r"^/api/comments/(\d+)$", path)
        if m:
            user = require_auth(self)
            if not user:
                return
            comment_id = int(m.group(1))
            new_body = (body.get("body") or "").strip()
            if not new_body:
                return error_response(self, "Comment body is required")
            if len(new_body) > 1000:
                return error_response(self, "Comment must be 1000 characters or less")
            comment, err = db.edit_comment(comment_id, user["id"], new_body)
            if err:
                return error_response(self, err, 404 if "not found" in err.lower() else 403)
            return json_response(self, {"comment": comment})

        # /api/me — update own profile (non-admin only)
        if path == "/api/me":
            user = require_auth(self)
            if not user:
                return
            if user.get("role") == "admin":
                return error_response(self, "Admin accounts cannot edit profile", 403)
            updated, err = db.update_user_profile(user["id"], body)
            if err:
                return error_response(self, err)
            return json_response(self, {"user": updated})

        # /api/admin/news/{id}
        m = re.match(r"^/api/admin/news/(\d+)$", path)
        if m:
            user = require_admin(self)
            if not user:
                return
            article_id = int(m.group(1))

            # Auto-fill tag_class from category if category changes
            if "category" in body and "tag_class" not in body:
                body["tag_class"] = infer_tag_class(body["category"])

            article, err = db.update_article(article_id, body)
            if err:
                return error_response(self, err, 404 if "not found" in err.lower() else 400)
            return json_response(self, {"article": article})

        error_response(self, "Not found", 404)

    # ── DELETE ────────────────────────────────────────────────────────────────
    def do_DELETE(self):
        path = urllib.parse.urlparse(self.path).path

        # /api/comments/{id} — owner or admin delete
        m = re.match(r"^/api/comments/(\d+)$", path)
        if m:
            user = require_auth(self)
            if not user:
                return
            comment_id = int(m.group(1))
            ok, err = db.delete_comment_by_user(comment_id, user["id"], user.get("role") == "admin")
            if not ok:
                return error_response(self, err, 404 if "not found" in err.lower() else 403)
            return json_response(self, {"ok": True, "deleted_id": comment_id})

        # /api/admin/news/{id}
        m = re.match(r"^/api/admin/news/(\d+)$", path)
        if m:
            user = require_admin(self)
            if not user:
                return
            article_id = int(m.group(1))
            ok, err = db.delete_article(article_id)
            if not ok:
                return error_response(self, err, 404)
            return json_response(self, {"ok": True, "deleted_id": article_id})

        # /api/admin/comments/{id}
        m = re.match(r"^/api/admin/comments/(\d+)$", path)
        if m:
            user = require_admin(self)
            if not user:
                return
            comment_id = int(m.group(1))
            ok, err = db.delete_comment(comment_id)
            if not ok:
                return error_response(self, err, 404)
            return json_response(self, {"ok": True, "deleted_id": comment_id})

        # DELETE /api/forum/posts/{id}
        m = re.match(r"^/api/forum/posts/(\d+)$", path)
        if m:
            user = require_auth(self)
            if not user:
                return
            err = db.delete_forum_post(int(m.group(1)), user["id"], user.get("role") == "admin")
            if err:
                return error_response(self, err, 404 if "not found" in err.lower() else 403)
            return json_response(self, {"ok": True})

        error_response(self, "Not found", 404)

    # ── Static file server ────────────────────────────────────────────────────
    def _serve_static(self, path):
        if path == "/" or path == "":
            path = "/index.html"

        file_path = os.path.normpath(os.path.join(FRONTEND_DIR, path.lstrip("/")))
        if not file_path.startswith(os.path.normpath(FRONTEND_DIR) + os.sep):
            return error_response(self, "Forbidden", 403)

        if not os.path.isfile(file_path):
            return error_response(self, "Not found", 404)

        ext  = os.path.splitext(file_path)[1].lower()
        mime = MIME.get(ext, "application/octet-stream")

        with open(file_path, "rb") as f:
            data = f.read()

        self.send_response(200)
        self.send_header("Content-Type", mime)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    db.init_db()
    server = ThreadingHTTPServer(("0.0.0.0", PORT), RespawnHandler)
    print(f"\n  RESPAWN News - Backend running")
    print(f"  http://localhost:{PORT}")
    print(f"  Admin login: admin@respawn.gg / admin123\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n  Server stopped.")
