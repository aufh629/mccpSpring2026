#!/bin/bash
# Pull latest from GitHub only (no commit, no stash)
cd "/Users/simonwang/Library/CloudStorage/OneDrive-HongKongBaptistUniversity/GTD/Areas/Teaching/Courses/MCCP 6020/PhDagentSpring2026"
git fetch origin
git pull origin main
echo "Done. Latest changes pulled from https://github.com/tesolchina/mccpSpring2026"
