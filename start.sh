#!/usr/bin/env bash
# ── RESPAWN News — Start server ──────────────────────────────────────────────
# Run from the project root: bash start.sh

set -e

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo ""
echo "  🎮  RESPAWN News"
echo "  ─────────────────────────────────────"
echo "  Starting backend on http://localhost:8765"
echo "  Open your browser at:  http://localhost:8765"
echo "  Press Ctrl+C to stop."
echo ""

cd "$PROJECT_DIR"
python3 backend/server.py
