#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os
from os.path import join as pjoin

from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-doc',
    version=__import__('pytest_doc').__version__,
    description='A documentation plugin for py.test.',
    author='Alfred Perlstein',
    author_email='alfred@freebsd.org',
    maintainer="Alfred Perlstein",
    maintainer_email="alfred@freebsd.org",
    url='http://pytest-doc.readthedocs.org/',
    license='BSD-2-Clause',
    packages=['pytest_doc'], # 'pytestdoc_util'],
    py_modules=['pytestdoc'],
    scripts=[pjoin('bin', 'json2rst')],
    long_description=read('README.rst'),
    install_requires=['pytest>=2.5'],
    classifiers=['Development Status :: 5 - Production/Stable',
                 #'Framework :: pytest',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Software Development :: Testing',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.2',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                ],
    # the following makes a plugin available to py.test
    entry_points={'pytest11': ['docs = pytest_doc.plugin']})
