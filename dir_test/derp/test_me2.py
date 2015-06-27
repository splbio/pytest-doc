import pytestdoc

TEST_CATEGORY="derps"

def func(x):
    return x + 1

@pytestdoc.tattr_redmine_bug(7474)
@pytestdoc.tattr_incomplete
@pytestdoc.tattr_doc("""
This is the documentation for my function

""")
def test_answer():
    assert func(4) == 5


def dump_test(f):
    if hasattr(f, 'redmine_bug'):
        print "Redmine bug: %d " % f.redmine_bug
    if hasattr(f, 'redmine_feature'):
        print "Redmine feature: %d " % f.redmine_feature
    if hasattr(f, 'tattr_incomplete') and f.tattr_incomplete is True:
        print "Test incomplete"
    if hasattr(f, 'tattr_docstr'):
        print "Test doc: " + f.tattr_docstr

print dir(test_answer)
test_answer()

dump_test(test_answer)
