Welcome to pytest-docs!
=======================

pytest-docs allows you to annotate your tests and generate documentation
about your tests.
`pytest testing tool <http://pytest.org/>`_.

* `Quick start / tutorial
  <http://pytest-doc.readthedocs.org/en/latest/tutorial.html>`_
* Full documentation: http://pytest-doc.readthedocs.org/en/latest/
* `Contribution docs
  <http://pytest-doc.readthedocs.org/en/latest/contributing.html>`_
* Version compatibility:

  * Python: CPython 2.6-2.7,3.2-3.4 or PyPy 2,3
  * pytest: 2.6.x

* Licence: BSD
* Project maintainers: Alfred Perlstein
* `All contributors <https://github.com/splbio/pytest-doc/contributors>`_
* Github repository: https://github.com/splbio/pytest-doc
* `Issue tracker <http://github.com/splbio/pytest-doc/issues>`_
* `Python Package Index (PyPI) <https://pypi.python.org/pypi/pytest-doc/>`_

See the `pytest documentation <http://pytest.org/latest/>`_ for more information on pytest itself.

Quickstart
==========

Add apporpriate includes and annotates to your test files:

.. code:: python

    import json
    import pytestdoc

    def times(x, y):
        return x * y

    TEST_CATEGORY="derp"

    @pytestdoc.tattr_redmine_feature(7474)
    @pytestdoc.tattr_redmine_bug(7475, 1776)
    @pytestdoc.tattr_incomplete
    @pytestdoc.tattr_category("herp")
    @pytestdoc.tattr_doc("""
    This is the *documentation* for my function

    It tests the following things:

    - if derps are herps
    - all fives are half of 10

    """)
    def test_positive():
        assert times(5,5) == 25

    @pytestdoc.tattr_doc("""Test that this works when first item is negative""")
    @pytestdoc.tattr_category("herp:negatives")
    def test_firstnegative():
        assert times(-2,5) == -10

    @pytestdoc.tattr_doc("""Test that this works when second item is negative""")
    @pytestdoc.tattr_category("herp:negatives")
    def test_secondnegative():
        assert times(3,-12) == -36

    @pytestdoc.tattr_doc("""Test that this works when both items are negative""")
    @pytestdoc.tattr_category("herp:negatives")
    def test_bothnegative():
        assert times(-12,-12) == 144
