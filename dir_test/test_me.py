import json
import pytestdoc

WHAT_IS_THIS = True

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

@pytestdoc.tattr_doc("""Test that this works when first item is negative""")
@pytestdoc.tattr_category("herp:negatives")
def test_firstnegative():
    assert times(-2,5) == -10

