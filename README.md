# RESPAWN News

A gaming news website with articles, reviews, comments, and user accounts.  
Built with a vanilla Python stdlib HTTP server, SQLite, and plain HTML/CSS/JS — no frameworks required.

---

## Features

- News articles and reviews across PlayStation, Xbox, Nintendo, PC, eSports, and Mobile
- User registration and login (session-based auth, PBKDF2 password hashing)
- Comment system with likes/dislikes, threaded replies, edit, and delete
- Admin panel to create, edit, and delete articles
- Related news sidebar on article pages
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

Or use the included helper script:

```bash
bash start.sh
```

The server starts on **http://localhost:8765**

### 3. Open the site

Navigate to [http://localhost:8765](http://localhost:8765) in your browser.

---

## Default admin account

When the database is created for the first time a seed admin user is created automatically.  
Check `backend/db.py` → `seed_data()` for the credentials and change them after first login.

---

## Project structure

```
respawn-news/
├── backend/
│   ├── server.py       # HTTP request handler + API routes
│   ├── db.py           # SQLite helpers (schema, queries, seeding)
│   └── news_data.py    # Seed article data
├── frontend/
│   ├── index.html      # Login / register page
│   ├── home.html       # Main feed
│   ├── category.html   # Category listing
│   ├── article.html    # Article detail + comments
│   ├── profile.html    # User profile
│   ├── admin.html      # Admin dashboard
│   ├── app.js          # Shared JS utilities
│   └── style.css       # Global styles
├── start.sh            # Quick-start script
├── .gitignore
└── README.md
```

---

## Contributing

1. Fork the repository and create a feature branch
2. Make your changes
3. Open a pull request describing what you changed and why

---

## License

MIT
