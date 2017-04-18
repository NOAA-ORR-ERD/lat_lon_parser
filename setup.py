#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

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
    packages=[
        'lat_lon_parser',
    ],
    package_dir={'lat_lon_parser':
                 'lat_lon_parser'},
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
