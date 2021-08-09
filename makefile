
DOCS=$(shell find docs *.rst  -name \*.rst)

test:	clean mktestdir
	pytest --cov-config=.coveragerc --cov=pynoteslib  tests/

build:
	python setup.py bdist_wheel

docs:	$(DOCS)
	@mkdir -p dist/docs
	sphinx-build -E   -b html docs dist/docs
	sphinx-build -b linkcheck docs dist/docs

mktestdir:
	-@mkdir __testing__

clean:
	-rm -rf __testing__/*
	tree -a __testing__

tree:
	tree -a __testing__/

importkeys:
	-gpg --import gpgkeys/*

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
