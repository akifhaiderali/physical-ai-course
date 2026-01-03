#!/usr/bin/env bash
# Render build script

set -o errexit

echo "=== Installing Python dependencies ==="
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt --no-cache-dir

echo "=== Build complete ==="
