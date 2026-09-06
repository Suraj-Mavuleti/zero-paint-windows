#!/bin/bash
# AUTO-UPDATER
cd /home/suraj/.gemini/antigravity/scratch/zero_suite/zero-paint-windows
git pull origin main --quiet
python3 zero_paint_gui.py
