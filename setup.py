#!/usr/bin/env python

import os

from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
    setup_requires=['pbr'],
    pbr=True,
    name = 'translit',
    packages=[
        'translit',
    ],
    install_requires=[
        'Cython',
        'transliterate'
    ]
)
