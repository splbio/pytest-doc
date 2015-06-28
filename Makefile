.PHONY: docs test clean isort

# port install py-certifi

testenv: bin/py.test

test: bin/py.test
	bin/pip install -e .
	bin/py.test

bin/python bin/pip:
	virtualenv .

bin/py.test: bin/python requirements.txt
	bin/pip install -Ur requirements.txt
	touch $@

bin/sphinx-build: bin/pip
	bin/pip install sphinx

docs: bin/sphinx-build
	SPHINXBUILD=../bin/sphinx-build $(MAKE) -C docs html

# See setup.cfg for configuration.
isort:
	find pytest_django tests -name '*.py' -exec isort {} +

clean:
	rm -rf include/ lib/ man/ pytest_doc.egg-info/ build/

install:
	rm -rf build
	python setup.py build install

pypitest-upload:
	/usr/bin/python setup.py sdist upload -r pypitest

pypitest-register:
	/usr/bin/python setup.py register -r pypitest

pypi-upload:
	/usr/bin/python setup.py sdist upload -r pypi

pypi-register:
	/usr/bin/python setup.py register -r pypi

publish-all:
	/usr/bin/python setup.py build register  -r pypi sdist upload -r pypi

