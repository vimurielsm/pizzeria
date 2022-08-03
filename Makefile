help:
	@echo "clean-venv       | removes the virtual environment"
	@echo "install          | build prod env"
	@echo "install-local    | build dev env"
	@echo "shell            | activate the env"

install:
	pipenv install

install-local:
	pipenv install --dev

shell:
	pipenv shell

clean-venv:
	pipenv --rm

clean: clean-pyc clean-build clean-coverage
	rm .coverage
	echo "Done!"

clean-coverage:
	rm -fr htmlcov/

lint:
	prospector


unit:
	python -m unittest discover

tests:
	coverage erase
	coverage run --source=. --omit=main.py  -m unittest discover -s test/unit -t .
	coverage report -m
	if [ -d htmlcov ]; then rm -r htmlcov; echo "removed old htmlcov"; fi
	coverage html