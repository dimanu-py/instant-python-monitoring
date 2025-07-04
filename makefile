.DEFAULT_GOAL := help

.PHONY: help
help:  ## Show this help.
	@grep -E '^[a-zA-Z_-]+:.*?## ' $(firstword $(MAKEFILE_LIST)) | \
			awk 'BEGIN {FS = ":.*## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: test
test:  ## Run all test.
	@uv run pytest test -ra

.PHONY: unit
unit:  ## Run all unit test.
	@uv run pytest -m "unit" -ra

.PHONY: integration
integration:  ## Run all integration test.
	@uv run pytest -m "integration" -ra

.PHONY: acceptance
acceptance:  ## Run all acceptance test.
	@docker compose up -d loki
	@uv run pytest -m "acceptance" -ra
	@docker compose down -v

.PHONY: coverage
coverage:  ## Run all test with coverage.
	@uv run coverage run --branch -m pytest test
	@uv run coverage html
	@$(BROWSER) htmlcov/index.html

.PHONY: local-setup
local-setup:  ## Setup git hooks and install dependencies.
	@uv run scripts/local_setup.py
	@make install

.PHONY: install
install:  ## Install dependencies.
	@uv sync --all-groups

.PHONY: update
update:  ## Update dependencies.
	@uv sync --upgrade

.PHONY: add-dep
add-dep:  ## Add a new dependency.
	@uv run scripts/add_dependency.py

.PHONY: remove-dep
remove-dep:  ## Remove a dependency.
	@uv run scripts/remove_dependency.py

.PHONY: check-typing
check-typing:  ## Run mypy type checking.
	@uv run mypy

.PHONY: check-lint
check-lint:  ## Run ruff linting check.
	@uvx ruff check src test

.PHONY: lint
lint:  ## Apply ruff linting fix.
	@uvx ruff check --fix src test

.PHONY: check-format
check-format:  ## Run ruff format check.
	@uvx ruff format --check src test

.PHONY: format
format:  ## Apply ruff format fix.
	@uvx ruff format src test

.PHONY: pre-commit
pre-commit: check-lint check-format ## Run pre-commit checks.

.PHONY: pre-push
pre-push:  unit ## Run pre-push checks.

.PHONY: watch
watch:  ## Run all test with every change.
	@uv run ptw --runner "pytest test -ra"

.PHONY: show
show:  ## Show installed dependencies.
	@uv tree

.PHONY: search
search:  ## Show package details.
	@read -p "Enter package name to search: " package;\
	uv pip show $$package
