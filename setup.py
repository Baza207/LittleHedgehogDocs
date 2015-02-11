#
# setup.py
# LittleHedgehogDocs
#
# Created by James Barrow on 10/02/2015.
# Copyright (c) 2015 James Barrow - Pig on a Hill Productions. All rights reserved.
#

#!/usr/bin/env python

import os, re
from setuptools import setup

def get_version(package):
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)

def get_author(package):
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__author__ = ['\"]([^'\"]+)['\"]", init_py).group(1)

def get_license(package):
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__license__ = ['\"]([^'\"]+)['\"]", init_py).group(1)

package = 'lhdocs'
version = get_version(package)
author = get_author(package)
licence = get_license(package)

setup(
    name=package,
    version=version,
    description='Little Hedgehog Docs - A Swift documentation to Markdown parser.',
    author=author,
    author_email='james@pigonahill.com',
    url='https://github.com/Baza207/LittleHedgehogDocs',
    licence=licence,
    zip_safe=False,
    packages=[package],
    install_requires=['beautifulsoup4==4.3.2'],
    classifiers=[
        'Development Status :: 1 - Development',
        'Environment :: Console',
        'Framework :: Little Hedgehog Docs',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ]
)
