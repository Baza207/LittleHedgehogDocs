#
# setup.py
# LittleHedgehogDocs
#
# Created by James Barrow on 10/02/2015.
# Copyright (c) 2015 James Barrow - Pig on a Hill Productions.
# All rights reserved.
#

# !/usr/bin/env python

import os
import re
import lhdocs
from setuptools import setup


package = 'lhdocs'
version = lhdocs.__version__
author = lhdocs.__author__
license = lhdocs.__license__
description = (
    'Little Hedgehog Docs - '
    'A Swift documentation to Markdown parser.'
)

setup(
    name=package,
    version=version,
    description=description,
    author=author,
    author_email='james@pigonahill.com',
    url='https://github.com/Baza207/LittleHedgehogDocs',
    license=license,
    zip_safe=False,
    packages=[package],
    scripts=['scripts/lhdocs'],
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
