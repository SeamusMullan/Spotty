.PHONY: help install dev-install format lint fix test clean

help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install the package
	uv pip install -e .

dev-install:  ## Install with development dependencies
	uv pip install -e ".[dev]"

format:  ## Auto-format code with Black and Ruff
	uv run black spotty/ main.py
	uv run ruff check --fix spotty/ main.py
	uv run ruff format spotty/ main.py

lint:  ## Run linters (pylint and ruff)
	uv run ruff check spotty/ main.py
	uv run pylint spotty/ main.py

fix: format  ## Alias for format

test:  ## Run tests
	uv run pytest

clean:  ## Clean up cache and build files
	rm -rf __pycache__ .pytest_cache .ruff_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

pre-commit-install:  ## Install pre-commit hooks
	uv run pre-commit install

pre-commit-run:  ## Run pre-commit hooks on all files
	pre-commit run --all-files
