
OUTNAME=example

all build-docs:
	py.test --docs $(OUTNAME).json
	json2rst < $(OUTNAME).json > $(OUTNAME).rst
	rst2html.py $(OUTNAME).rst > $(OUTNAME).html

