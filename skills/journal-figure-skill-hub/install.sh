#!/usr/bin/env bash
set -euo pipefail
python -m venv .venv
./.venv/bin/python -m pip install --upgrade pip
./.venv/bin/python -m pip install -r requirements.txt
command -v git || true
command -v inkscape || true
command -v magick || true
