setup:
	pip install pipenv
	pipenv install --ignore-pipfile
	pipenv shell

install:
	pipenv install --ignore-pipfile

init:
	pipenv shell

lint:
	black .
	isort .
	pytest --pylint -m "not test_cases"

test:
	pytest

