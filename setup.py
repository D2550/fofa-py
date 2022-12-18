#!/usr/bin/env python

from setuptools import setup

setup(
    name = 'FOFA',
    version = '1.0.0',
    description = 'Python library for FOFA (https://fofa.info)',
    author = 'ccadmin',
    author_email = 'ccadmin@88.com',
    url = 'https://github.com/D2550/fofa-py',
    packages = ['fofa', 'fofa.poc', 'fofa.src'],
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)