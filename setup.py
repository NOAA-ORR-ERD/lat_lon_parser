#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function

import os

from setuptools import setup, find_packages


def get_version():
    with open(os.path.join("lat_lon_parser", "__init__.py")) as initfile:
        for line in initfile:
            # __version__ = '1.0.0'
            if line.strip().startswith("__version__"):
                version = line.split('=')[1].strip().strip("'")
                return version
    raise ValueError("__version__ isnot specified in __init__.py")


with open('README.rst') as readme_file:
    readme = readme_file.read()
#    readme = readme_file.read().decode('utf-8')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='lat_lon_parser',
    version=get_version(),
    description="simple parser for latitude-longitude strings",
    long_description=readme,
    author="Christopher Barker",
    author_email='Chris.Barker@noaa.gov',
    url='https://github.com/ChrisBarker-NOAA/lat_lon_parser',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='lat_lon_parser',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 3',
    ],
    test_suite='tests',
    tests_require=test_requirements
)

