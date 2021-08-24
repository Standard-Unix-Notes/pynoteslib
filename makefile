.DEFAULT_GOAL = test

#DOCS=$(shell find docs *.rst  -name \*.rst)

test:	clean mktestdir
	pytest  --cov-config=.coveragerc --cov=pynoteslib  tests/


build:
	python setup.py bdist_wheel

docs:
	@mkdir -p dist/docs
	sphinx-build -E   -b html docs dist/docs
	#sphinx-build -b linkcheck docs dist/docs

pylint:
	pylint pynoteslib tests

isort:
	isort .

flake8:
	flake8 pynoteslib/pynoteslib.py

install:
	pip install -r requirements.txt

publish:  build
	python3 -m twine upload  dist/pynoteslib-*.whl

mktestdir:
	-@mkdir __testing__

clean:
	-rm -rf __testing__/* dist/*
	tree -a __testing__

tree:
	tree -a __testing__/
localinstall:
	pip install -e .

freeze:	setup.py requirements.txt
	pip freeze > requirements.txt

reqinstall:
	pip install -e .

devinstall:
	pip install -e .[dev] .[docs]

black:	reformatlib reformattests

reformatlib:
	black src/*.py

reformattests:
	black tests/*.py

importkeys:
	-gpg --import gpgkeys/*
	(echo 'A692697DCC57084C4E87D66C7D34402EBB3EB284:6:' | gpg --import-ownertrust)
	(echo 'FE326B58CDD40DF70FEAB2722822B15BB44A9055:6:' | gpg --import-ownertrust)

tags: pynoteslib/pynoteslib.py
	ctags -R . 2> /dev/null
