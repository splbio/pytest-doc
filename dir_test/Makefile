all build-docs:
	py.test --docs log.json
	json2rst < log.json > log.rst
	rst2html.py log.rst > log.html

