#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

setup(
    name='helloworld',
    version='1.0.0',
    url='https://github.com/yourusername/myprogram',
    author='Daniel Wärnelöv',
    author_email='daniel.pean@gmail.com',
    # py_modules=['helloworld'],
    packages=['helloworld', 'bin'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'helloworld=bin.helloworld:main',
        ],
    },
    # packages=['helloworld']
)