/**
 * app.js — Shared frontend utilities for RESPAWN News
 */

const API_BASE = 'http://localhost:8765';

// ── HTML escape helper ────────────────────────────────────────────────────────
function escHtml(str) {
  return String(str || '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

// ── Authenticated fetch wrapper ───────────────────────────────────────────────
function apiFetch(path, options = {}) {
  const token = localStorage.getItem('respawn_token');
  return fetch(API_BASE + path, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: 'Bearer ' + token } : {}),
      ...(options.headers || {}),
    },
  });
}

// ── Navigate to article detail page ──────────────────────────────────────────
function goToArticle(id) {
  window.location = `article.html?id=${id}`;
}

// ── Render navbar user section ────────────────────────────────────────────────
// Call after DOM ready, pass the stored user object.
// Non-admin: avatar is clickable → profile.html
// Admin: not clickable (admin-only account)
function initNavUser(user) {
  const avatarEl   = document.getElementById('navAvatar');
  const usernameEl = document.getElementById('navUsername');
  if (!avatarEl || !usernameEl) return;

  // Avatar image or initial
  if (user.avatar && user.avatar.trim()) {
    avatarEl.innerHTML = `<img src="${user.avatar.trim()}" alt=""
      style="width:100%;height:100%;object-fit:cover;border-radius:50%;" />`;
  } else {
    avatarEl.textContent = (user.username || '?')[0].toUpperCase();
  }
  usernameEl.textContent = user.username || '';

  // Clickable only for regular users
  if (user.role !== 'admin') {
    const navUser = avatarEl.closest('.nav-user') || avatarEl.parentElement;
    navUser.style.cursor = 'pointer';
    navUser.title = 'Edit profile';
    navUser.addEventListener('click', () => {
      window.location = 'profile.html';
    });
    // Subtle hover highlight
    navUser.addEventListener('mouseenter', () => navUser.style.opacity = '.75');
    navUser.addEventListener('mouseleave', () => navUser.style.opacity = '1');
  }
}

// ── Hero tile (featured grid, large left panel) ───────────────────────────────
function renderHeroTile(a) {
  const score = a.score !== null && a.score !== undefined
    ? `<div class="score-badge"><div class="score-num">${Number(a.score).toFixed(1)}</div><div class="score-label">Score</div></div>`
    : '';
  const imgPos = escHtml(a.image_position || '50% 50%');
  return `
    <div class="tile tile--hero" onclick="goToArticle(${a.id})">
      <img class="tile__img" src="${escHtml(a.image)}" alt="" loading="lazy" style="object-position:${imgPos}" />
      ${score}
      <div class="tile__body">
        <span class="tile__tag ${escHtml(a.tag_class)}">${escHtml(a.tag)}</span>
        <div class="tile__headline">${escHtml(a.headline)}</div>
        <div class="tile__meta">
          <span>${escHtml(a.author)}</span>
          <span class="sep">·</span>
          <span>${escHtml(a.date)}</span>
        </div>
        <div class="tile__read-btn">Read more →</div>
      </div>
    </div>`;
}

// ── Small tile (featured grid, right panel) ───────────────────────────────────
function renderSmTile(a) {
  const score = a.score !== null && a.score !== undefined
    ? `<div class="score-badge"><div class="score-num">${Number(a.score).toFixed(1)}</div><div class="score-label">Score</div></div>`
    : '';
  const imgPos = escHtml(a.image_position || '50% 50%');
  return `
    <div class="tile tile--sm" onclick="goToArticle(${a.id})">
      <img class="tile__img" src="${escHtml(a.image)}" alt="" loading="lazy" style="object-position:${imgPos}" />
      ${score}
      <div class="tile__body">
        <span class="tile__tag ${escHtml(a.tag_class)}">${escHtml(a.tag)}</span>
        <div class="tile__headline">${escHtml(a.headline)}</div>
        <div class="tile__meta">
          <span>${escHtml(a.author)}</span>
          <span class="sep">·</span>
          <span>${escHtml(a.date)}</span>
        </div>
      </div>
    </div>`;
}

// ── News card (sub-grid) ──────────────────────────────────────────────────────
function renderCard(a) {
  const score = a.score !== null && a.score !== undefined
    ? `<span class="card__score">⭐ ${Number(a.score).toFixed(1)}</span>`
    : '';
  const imgPos = escHtml(a.image_position || '50% 50%');
  return `
    <div class="card" onclick="goToArticle(${a.id})">
      <div class="card__img-wrap">
        <img class="card__img" src="${escHtml(a.image)}" alt="" loading="lazy" style="object-position:${imgPos}" />
      </div>
      <div class="card__body">
        <span class="tile__tag ${escHtml(a.tag_class)}">${escHtml(a.tag)}</span>
        <div class="card__headline">${escHtml(a.headline)}</div>
        <div class="card__summary">${escHtml(a.summary)}</div>
        <div class="card__meta">
          <span>${escHtml(a.author)}</span>
          <span>·</span>
          <span>${escHtml(a.date)}</span>
          ${score}
        </div>
      </div>
    </div>`;
}

// ── Mobile hamburger nav (auto-injected) ──────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  const nav = document.querySelector('nav');
  if (!nav) return;

  const btn = document.createElement('button');
  btn.className = 'nav-hamburger';
  btn.setAttribute('aria-label', 'Toggle menu');
  btn.innerHTML = '<span></span><span></span><span></span>';

  // Inject as first child of .nav-right so it sits inside that flex container
  const navRight = nav.querySelector('.nav-right');
  if (navRight) navRight.insertBefore(btn, navRight.firstChild);
  else nav.appendChild(btn);

  btn.addEventListener('click', e => {
    e.stopPropagation();
    nav.classList.toggle('nav-open');
  });

  document.addEventListener('click', e => {
    if (!nav.contains(e.target)) nav.classList.remove('nav-open');
  });

  // Close nav when a link is clicked
  nav.querySelectorAll('.nav-links a').forEach(a => {
    a.addEventListener('click', () => nav.classList.remove('nav-open'));
  });
});
