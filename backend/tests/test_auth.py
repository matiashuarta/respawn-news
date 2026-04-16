"""
Tests for password hashing and user authentication logic.
These are unit tests — they do not require the HTTP server to be running.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import db


# ── Password hashing ──────────────────────────────────────────────────────────

def test_hash_password_is_not_plaintext():
    hashed = db.hash_password("admin123")
    assert hashed != "admin123"

def test_hash_password_contains_salt_separator():
    # format is  salt$hash
    hashed = db.hash_password("admin123")
    assert "$" in hashed

def test_same_password_produces_different_hashes():
    # salt is random each time, so two hashes of the same password must differ
    h1 = db.hash_password("admin123")
    h2 = db.hash_password("admin123")
    assert h1 != h2

def test_verify_correct_password():
    hashed = db.hash_password("mysecret")
    assert db.verify_password("mysecret", hashed) is True

def test_verify_wrong_password():
    hashed = db.hash_password("mysecret")
    assert db.verify_password("wrongpassword", hashed) is False

def test_verify_empty_password():
    hashed = db.hash_password("mysecret")
    assert db.verify_password("", hashed) is False

def test_verify_tampered_hash():
    # if someone corrupts the stored hash, verify must return False not crash
    assert db.verify_password("admin123", "badsalt$badhash") is False


# ── Register and login (uses a temporary in-memory DB) ───────────────────────

import sqlite3, tempfile, pytest

@pytest.fixture
def tmp_db(monkeypatch, tmp_path):
    """
    Redirect DB_PATH to a fresh temp file for each test,
    then run init_db() so the schema and admin user are created.
    """
    db_file = str(tmp_path / "test.db")
    monkeypatch.setattr(db, "DB_PATH", db_file)
    db.init_db()
    return db_file


def test_register_new_user(tmp_db):
    user, err = db.register_user("testuser", "test@example.com", "password123")
    assert err is None
    assert user["username"] == "testuser"
    assert user["email"]    == "test@example.com"
    assert user["role"]     == "user"

def test_register_duplicate_username(tmp_db):
    db.register_user("dupeuser", "first@example.com", "password123")
    _, err = db.register_user("dupeuser", "second@example.com", "password123")
    assert err == "Username already taken"

def test_register_duplicate_email(tmp_db):
    db.register_user("user1", "same@example.com", "password123")
    _, err = db.register_user("user2", "same@example.com", "password123")
    assert err == "Email already registered"

def test_login_valid_credentials(tmp_db):
    db.register_user("loginuser", "login@example.com", "pass123")
    token, user, err = db.login_user("login@example.com", "pass123")
    assert err   is None
    assert token is not None
    assert len(token) == 64          # 32 bytes hex = 64 chars
    assert user["username"] == "loginuser"

def test_login_wrong_password(tmp_db):
    db.register_user("loginuser2", "login2@example.com", "correctpass")
    token, user, err = db.login_user("login2@example.com", "wrongpass")
    assert token is None
    assert user  is None
    assert err   == "Invalid email or password"

def test_login_nonexistent_email(tmp_db):
    token, user, err = db.login_user("nobody@example.com", "irrelevant")
    assert token is None
    assert err   == "Invalid email or password"

def test_get_user_by_token(tmp_db):
    db.register_user("tokenuser", "token@example.com", "pass")
    token, _, _ = db.login_user("token@example.com", "pass")
    user = db.get_user_by_token(token)
    assert user is not None
    assert user["username"] == "tokenuser"

def test_get_user_by_invalid_token(tmp_db):
    user = db.get_user_by_token("thisisnotavalidtoken")
    assert user is None

def test_get_user_by_empty_token(tmp_db):
    user = db.get_user_by_token("")
    assert user is None
