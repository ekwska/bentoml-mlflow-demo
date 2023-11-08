.PHONY: clean clean-build clean-pyc clean-test coverage dist docs help install lint lint/flake8 lint/black train serve containerize run_mlflow_server
.DEFAULT_GOAL := help
SHELL := /bin/bash

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python3 -c "$$BROWSER_PYSCRIPT"

help:
	@python3 -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

# Project specific make commands
train: ## Run a model training
	poetry run train

serve: ## Serve the latest trained model using BentoML
	poetry run bentoml serve bentoml_service.py:svc --reload

containerize: ## Containerize the latest trained model using BentoML
	poetry run bentoml build -f bentofile.yaml --containerize

run_mlflow_server: ## Run a local MLFlow tracking server to view training results and saved models
	poetry run mlflow server --host 127.0.0.1 --port 8080

# Utility make commands

clean: clean-build clean-pyc clean-test clean-venv ## remove all build, test, coverage and Python artifacts

clean-venv: ## Remove virtual environment
	rm -rf .venv

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint/flake8: ## check style with flake8
	poetry run flake8 bentoml_mlflow_demo tests
lint/black: ## check style with black
	poetry run black --check bentoml_mlflow_demo tests

lint: lint/black lint/flake8 ## check style

format:
	poetry run black bentoml_mlflow_demo tests

test: ## run tests quickly with the default Python
	pytest

test-all: ## run tests on every Python version with tox
	tox

coverage: ## check code coverage quickly with the default Python
	poetry run coverage run --source bentoml_mlflow_demo -m pytest
	poetry run coverage report -m
	poetry run coverage html
	$(BROWSER) htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/bentoml_mlflow_demo.rst
	rm -f docs/modules.rst
	poetry run sphinx-apidoc -o docs/ bentoml_mlflow_demo
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: dist ## package and upload a release
	twine upload dist/*

dist: clean ## builds source and wheel package
	poetry run python setup.py sdist
	poetry run python setup.py bdist_wheel
	ls -l dist

setup-install: clean ## install the package to the active Python's site-packages
	python setup.py install

install: clean
	poetry install -v
