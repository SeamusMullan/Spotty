#!/usr/bin/env bash
# Auto-fix script - runs formatters and linters with auto-fix enabled

set -e

echo "Running auto-fix tools..."
echo ""

echo "Step 1: Formatting with Black..."
uv run black spotty/ main.py
echo ""

echo "Step 2: Auto-fixing with Ruff..."
uv run ruff check --fix spotty/ main.py || true
echo ""

echo "3: Formatting with Ruff..."
uv run ruff format spotty/ main.py
echo ""

echo "Auto-fix complete! Review the changes and commit."
echo ""
echo "Tip: Run 'uv run pylint spotty/' to check for remaining issues"
