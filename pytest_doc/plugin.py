import pytest
import copy
import json
import sys
DOC_OUT = None
FIRST_TEST = True

OUT = { 'tests':[]}
TESTS=OUT['tests']

def pytest_addoption(parser):
    group = parser.getgroup('docs')
    group._addoption("--docs", help="output docs to json file")

def pytest_unconfigure(config):
    outfile = config.getoption("--docs")
    if outfile:
        f = open(outfile, "w")
        f.write(json.dumps(OUT, indent=4))

def dump_test(item):
    if not hasattr(item, "function"):
        return
    func = item.function
    if not hasattr(func, 'tattr'):
        func.tattr = {'missing_attr': True}
    obj = copy.deepcopy(func.tattr)
    code = func.__code__
    obj['filename'] = code.co_filename
    obj['fileline'] = code.co_firstlineno
    obj['testname'] = code.co_name
    if not 'category' in obj:
        globals = func.func_globals
        mod = sys.modules[func.__module__]
        if hasattr(mod, 'TEST_CATEGORY'):
            obj['category'] = mod.TEST_CATEGORY

    TESTS.append(obj)

def pytest_runtest_setup(item):
    if item.config.getoption("--docs"):
        dump_test(item)
        pytest.skip("skipping because generating docs")
