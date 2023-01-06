.PHONY: all format test install_libs upgrade_all

all: format test

format:  ## Format and static-check
	@echo "Cleaning up dagster-utils"
	@cd dagster-utils; isort . --profile black; black .
	@echo "Cleaning up some-dagster-project"
	@cd some-dagster-project; isort . --profile black; black .

test:
	@echo "Running tests in dagster-utils"
	@cd dagster-utils; poetry run pytest -vv
	@echo "Running tests in some-dagster-project"
	@cd some-dagster-project; poetry run pytest -vv

install_libs:
	@echo "Installing libraries in _deployment"
	@cd _deployment; poetry install; poetry export -f requirements.txt --output requirements.txt --without-hashes
	@echo "Installing libraries in dagster-utils"
	@cd dagster-utils; poetry install
	@echo "Installing libraries in some-dagster-project"
	@cd some-dagster-project; poetry install

upgrade_all:
	@echo "Upgrading libraries in _deployment"
	@cd _deployment; poetry update; poetry export -f requirements.txt --output requirements.txt --without-hashes
	@echo "Upgrading libraries in dagster-utils"
	@cd dagster-utils; poetry update
	@echo "Upgrading libraries in some-dagster-project"
	@cd some-dagster-project; poetry update
