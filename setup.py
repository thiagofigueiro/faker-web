#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import io

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = io.open(os.path.join(here, 'README.rst'), encoding="utf8").read()

version = '0.3.1'

tests_require = [
    'pytest',
    'pytest-cov',
    'pytest-flakes',
    'pytest-pep8',
]

# this module can be zip-safe if the zipimporter implements iter_modules or if
# pkgutil.iter_importer_modules has registered a dispatch for the zipimporter.
try:
    import pkgutil
    import zipimport
    zip_safe = hasattr(zipimport.zipimporter, "iter_modules") or \
        zipimport.zipimporter in pkgutil.iter_importer_modules.registry.keys()
except (ImportError, AttributeError):
    zip_safe = False

setup(
    name='faker_web',
    version=version,
    description="Web-related Provider for the Faker Python package.",
    long_description=README,
    classifiers=[
        # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache Software License'
    ],
    keywords='faker web test data',
    author='thiagofigueiro',
    author_email='thiagocsf+fakerweb@gmail.com',
    url='https://github.com/thiagofigueiro/faker_web',
    license='Apache License, Version 2.0',
    package_dir={'faker_web': 'src/web'},
    packages=['faker_web'],
    platforms=['any'],
    test_suite='pytest',
    zip_safe=zip_safe,
    setup_requires=['pytest-runner'],
    tests_require=tests_require,
    install_requires=['faker'],
    extras_require={'test': tests_require},
)
