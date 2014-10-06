#!/usr/bin/env python

from setuptools import setup

setup(
    name='pyjs',
    version='0.0.0',
    author='Kevin Schaul',
    author_email='kevin.schaul@gmail.com',
    url='http://kevin.schaul.io',
    description='A basic JavaScript engine.',
    packages=[
        'pyjs',
    ],
    entry_points = {
        'console_scripts': [
            'pyjs = pyjs.pyjs:launch_new_instance',
        ],
    },
)

