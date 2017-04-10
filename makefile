build: test_requirements test

clean:
	-find . -type f -name "*.pyc" -delete
	-find . -type d -name "__pycache__" -delete

test_requirements:
	pip install -r requirements_test.txt

flake8:
	flake8 . --exclude=.venv

pytest:
	pytest . --cov=. $(pytest_args)

test: flake8 pytest

.PHONY: build clean test_requirements flake8 pytest test
