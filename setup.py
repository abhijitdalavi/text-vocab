#!/usr/bin/env python
from setuptools import find_packages, setup

from __init__ import VERSION

setup(
    name='textvocab',
    version=VERSION,
    url='https://github.com/abhijitdalavi/textvocab.git',
    scripts = ["text_vocab.py","categarization.py","__init__.py"],
    description=(
        "used to create a vocabulary and extract the vocabulary"),
    keywords="TextVocab, textvocab",
    include_package_data=True,
    classifiers=[
        'Development Status :: 0.0.1 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6']
)