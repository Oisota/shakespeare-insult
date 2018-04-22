all: build

.PHONY: build
build:
	python setup.py sdist bdist_wheel

.PHONY: upload
upload:
	twine upload dist/*

.PHONY: test
test:
	python -m unittest

.PHONY: clean
clean:
	$(RM) -r build dist *.egg-info

.PHONY: rebuild
rebuild: clean build
