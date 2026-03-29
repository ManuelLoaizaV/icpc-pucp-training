.PHONY: help setup generate

EASY ?= 0
MEDIUM ?= 0
HARD ?= 0

help:
	@echo "Available commands:"
	@echo "  make setup            - Install dependencies using uv"
	@echo "  make generate         - Create a new contest. Requires arguments."
	@echo "  make format           - Format code with Ruff"

setup:
	uv sync
	mkdir -p data

generate:
	uv run python src/manage.py generate-contest --year $(YEAR) --lecture $(LECTURE) --easy $(EASY) --medium $(MEDIUM) --hard $(HARD)