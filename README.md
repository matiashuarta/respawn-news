# RESPAWN News

A gaming news and community website with articles, reviews, a community forum, comments, and user accounts.  
Built with a vanilla Python stdlib HTTP server, SQLite, and plain HTML/CSS/JS — no frameworks required.

---

## Features

- News articles and reviews across PlayStation, Xbox, Nintendo, PC, eSports, and Mobile
- User registration and login (session-based auth, PBKDF2 password hashing)
- Comment system with likes/dislikes, threaded replies, edit, and delete
- Related news horizontal carousel on article pages
- Community forum with 18 categories, topic sorting, hot-topic scoring, and rank system
- Admin panel to create, edit, and delete articles
- Fully responsive design

---

## Requirements

- Python 3.10 or later (uses the standard library only — no `pip install` needed)

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/respawn-news.git
cd respawn-news
```

### 2. Run the server

```bash
python backend/server.py
```

The server starts on **http://localhost:8765** and auto-creates/seeds the database on first run.

### 3. Open the site

Navigate to [http://localhost:8765](http://localhost:8765) in your browser.

---

## Default admin account

| Field    | Value               |
|----------|---------------------|
| Email    | admin@respawn.gg    |
| Password | admin123            |

Change the password after first login via the Profile page.

---

## Project structure

```
respawn-news/
├── backend/
│   ├── server.py          # HTTP server, all API routes (auth, news, comments, forum)
│   ├── db.py              # SQLite schema, queries, seeding, and migrations
│   └── news_data.py       # Seed article and review data
├── frontend/
│   ├── index.html         # Login / register page
│   ├── home.html          # Main news feed (featured + grid)
│   ├── category.html      # Articles filtered by news category
│   ├── article.html       # Article detail, related news carousel, comments
│   ├── profile.html       # User profile and settings
│   ├── admin.html         # Admin dashboard (create/edit/delete articles)
│   ├── forum.html         # Forum landing (categories, hot topics, rank ladder)
│   ├── forum-category.html# Topic list for a single forum category (sortable)
│   ├── forum-topic.html   # Individual thread view (posts, likes, replies)
│   ├── app.js             # Shared JS utilities (apiFetch, escHtml, nav helpers)
│   └── style.css          # Global dark-theme styles and component classes
├── .gitignore
└── README.md
```

---

## API overview

All routes require a valid session token in the `Authorization: Bearer <token>` header except `/api/auth/login` and `/api/auth/register`.

| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/auth/register` | Create account |
| POST | `/api/auth/login` | Login, returns token |
| POST | `/api/auth/logout` | Invalidate token |
| GET | `/api/me` | Current user info |
| GET | `/api/news` | All articles (optional `?category=`) |
| GET | `/api/news/:id` | Single article |
| GET | `/api/news/:id/related` | Related articles (same category, up to 10) |
| GET | `/api/news/:id/comments` | Comments + user votes |
| POST | `/api/news/:id/comments` | Post a comment or reply |
| GET | `/api/forum/categories` | All forum categories |
| GET | `/api/forum/topics` | Topics (optional `?category=slug`) |
| GET | `/api/forum/topics/hot` | Top 5 topics by hot score |
| GET | `/api/forum/topics/:id` | Thread + all posts |
| POST | `/api/forum/topics` | Create a new topic |
| POST | `/api/forum/topics/:id/posts` | Reply to a topic |
| POST | `/api/forum/posts/:id/like` | Toggle like on a post |
| DELETE | `/api/forum/posts/:id` | Delete a post (owner or admin) |
| GET | `/api/forum/me/rank` | Current user's post count and rank |
| GET | `/api/forum/rules` | Returns the topic ID of the pinned rules topic |

---

## Contributing

See [Branch strategy](#branch-strategy) below.

---

## Branch strategy

| Branch | Purpose |
|--------|---------|
| `master` | Stable, production-ready code |
| `dev` | Integration branch — all PRs target here |

1. Branch off `dev` for any fix or feature
2. Open a pull request into `dev`
3. Once reviewed and tested, `dev` is merged into `master`

---

## License

MIT
