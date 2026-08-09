.PHONY: install run test lint format typecheck migrate

install:
	python -m pip install -e ".[dev]"

run:
	uvicorn property_utility.api.app:app --host 0.0.0.0 --port 8000

test:
	pytest

lint:
	ruff check .

format:
	ruff format .

typecheck:
	mypy src

migrate:
	alembic upgrade head
