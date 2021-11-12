install:
	poetry install

gendiff-help:
	poetry run gendiff -h

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstal --user dist/*.whl
