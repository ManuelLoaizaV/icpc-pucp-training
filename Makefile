.PHONY: help setup generate add-lecture

EASY ?= 0
MEDIUM ?= 0
HARD ?= 0
YEAR ?=
LECTURE ?=

help:
	@echo "Available commands:"
	@echo "  make setup            Install dependencies using uv"
	@echo "  make add-lecture      Add a lecture to the timeline. Requires YEAR and LECTURE."
	@echo "  make generate         Create a new contest. Requires arguments."

setup:
	uv sync
	mkdir -p data

add-lecture:
	uv run python src/manage.py add-lecture --year $(YEAR) --lecture $(LECTURE)

generate:
	uv run python src/manage.py generate-contest --year $(YEAR) --lecture $(LECTURE) --easy $(EASY) --medium $(MEDIUM) --hard $(HARD)