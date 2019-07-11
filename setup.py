#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

requirements = [ ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Pradeep Reddy Raamana",
    author_email='raamana@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="atlas classes and methods for neuroimaging",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description="atlas classes and methods for neuroimaging",
    include_package_data=True,
    keywords='niatlas',
    name='niatlas',
    packages=find_packages(include=['niatlas']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/raamana/niatlas',
    version='0.0.1',
    zip_safe=False,
)
