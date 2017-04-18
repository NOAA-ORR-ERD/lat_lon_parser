#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import, division, print_function


from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read().decode('utf-8')

with open('HISTORY.rst') as history_file:
    history = history_file.read().decode('utf-8')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='lat_lon_parser',
    version='0.1.0',
    description="simple parser for latitude-longitude strings",
    long_description=readme + '\n\n' + history,
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
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)

