install:
	poetry install

gendiff-help:
	poetry run gendiff -h

gendiff:
	poetry run gendiff

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstal dist/*.whl

lint:
	poetry run flake8 gendiff

run_tests:
	poetry run pytest -vv --cov=gendiff --cov-report xml tests/
