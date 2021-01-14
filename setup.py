#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

from setuptools import setup, find_packages


def get_version():
    with open(os.path.join("lat_lon_parser", "__init__.py")) as initfile:
        for line in initfile:
            if line.strip().startswith("__version__"):
                version = line.split('=')[1].strip().strip("'")
                return version
    raise ValueError("__version__ is not specified in __init__.py")


with open('README.rst') as readme_file:
    readme = readme_file.read()

test_requirements = ['pytest']

setup(
    name='lat_lon_parser',
    version=get_version(),
    description="Simple parser for latitude-longitude strings",
    long_description=readme,
    author="Christopher Barker",
    author_email='Chris.Barker@noaa.gov',
    url='https://github.com/NOAA-ORR-ERD/lat_lon_parser',
    packages=find_packages(),
    zip_safe=False,
    keywords='lat_lon_parser',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
    ],
    test_suite='tests',
    tests_require=test_requirements
)

