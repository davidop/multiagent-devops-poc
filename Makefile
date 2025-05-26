.PHONY: setup lint test start clean

VENV ?= .venv
PIP = $(VENV)/bin/pip
PY = $(VENV)/bin/python

setup:
	python -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt pytest pytest-cov flake8 black azure-functions

lint:
	$(PY) -m black --check .
	$(PY) -m flake8 .

test:
	$(PY) -m pytest --cov=.

start:
	func start

clean:
	rm -rf $(VENV)
