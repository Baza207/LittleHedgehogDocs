#
# setup.py
# LittleHedgehogDocs
#
# Created by James Barrow on 10/02/2015.
# Copyright (c) 2015 James Barrow - Pig on a Hill Productions.
# All rights reserved.
#

# !/usr/bin/env python
# flake8: noqa

import lhdocs
from setuptools import setup


description = 'Little Hedgehog Docs - A Swift documentation to Markdown parser.'

setup(
    name='lhdocs',
    version=lhdocs.__version__,
    description=description,
    author=lhdocs.__author__,
    author_email='james@pigonahill.com',
    url='https://github.com/Baza207/LittleHedgehogDocs',
    license=lhdocs.__license__,
    zip_safe=False,
    packages=['lhdocs'],
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
