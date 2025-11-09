# Code Quality Tools Guide

## Quick Commands

### Auto-fix before committing

```bash
# Option 1: Use the script (recommended)
./scripts/autofix.sh

# Option 2: Run commands manually
uv run black spotty/ main.py
uv run ruff check --fix spotty/ main.py
uv run ruff format spotty/ main.py

# Option 3: Use make (if you have make installed)
make format
```

### Check for issues without fixing

```bash
# Ruff (fast)
uv run ruff check spotty/ main.py

# Pylint (not fast but probably better)
uv run pylint spotty/ main.py

# Or with make
make lint
```

## Pre-commit Hooks (Auto-run before each commit)

### Setup (one-time)

```bash
uv pip install -e ".[dev]"  # Install dev dependencies
uv run pre-commit install    # Install git hooks
```

### Usage

After setup, the tools will run automatically when you commit:

```bash
git add .
git commit -m "Your message"
# -> Pre-commit hooks run automatically and fix issues
```

### Manual run

```bash
uv run pre-commit run --all-files
```

## What Each Tool Does

### **Black** (Formatter)

- Automatically formats code to be consistent
- Fixes spacing, line length, quotes, etc.
- Opinionated - no configuration needed

### **Ruff** (Linter + Formatter)

- Super fast linter (replaces flake8, isort, etc.)
- Auto-fixes many common issues:
  - Unused imports
  - Import sorting
  - Simple syntax issues
  - Code style violations

### **Pylint** (Static Analyzer)

- Thorough code analysis
- Finds bugs, code smells, and style issues
- Some issues can't be auto-fixed (need manual fixes)

## Workflow

### Before committing

```bash
# 1. Auto-fix everything possible
./scripts/autofix.sh

# 2. Check what's left
uv run pylint spotty/

# 3. Fix remaining issues manually (if bothered)

# 4. Commit
git add .
git commit -m "Your commit message"
```

## Tips

- Run `./scripts/autofix.sh` frequently while developing (it's like a sanity check or smth idk)
- Don't worry about minor pylint warnings, just fix the important ones plz
- The pre-commit hooks will catch most issues automatically (probably :3)
- If a tool blocks your commit, fix the issues it mentions and try again (or pray to the elders)
