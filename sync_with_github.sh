#!/bin/bash
# Option C: Commit local work, then pull from GitHub
# Run from terminal: cd PhDagentSpring2026 && bash sync_with_github.sh

set -e
echo "=== Step 1: Staging all changes ==="
git add -A

echo "=== Step 2: Committing ==="
git commit -m "Local updates before sync" || true

echo "=== Step 3: Pulling latest from GitHub ==="
git pull origin main

echo "=== Done. Your repo is synced with https://github.com/tesolchina/mccpSpring2026 ==="
