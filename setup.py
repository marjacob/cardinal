# -*- coding: utf-8 -*-
# Based on https://github.com/pypa/pip/blob/develop/setup.py

import codecs
import os
import re
import sys

from setuptools import setup, find_packages


def read(*parts):
    here = os.path.abspath(os.path.dirname(__file__))
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


long_description = read('README.md')


setup(
    name="cardinal",
    version=find_version("cardinal", "__init__.py"),
    description="Cardinal the IRC bot.",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
        "Click",
        "coverage",
        "green",
        "irc3",
        "pip",
        "pylint",
        "requests"
    ],
    entry_points="""
        [console_scripts]
        cardinal=cardinal:cli
    """,
)
