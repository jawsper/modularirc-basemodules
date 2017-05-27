#!/usr/bin/env python3

from setuptools import setup

import sys
sys.path.insert(0, 'src/modularirc/modules')
from basemodules import __version__

setup(
    name='modularirc.basemodules',
    version=__version__,
    author='Jasper Seidel',
    author_email='code@jawsper.nl',
    packages=['modularirc.modules.basemodules'],
    package_dir={'': 'src'},
    url='https://github.com/jawsper/modularirc-basemodules',
    license='LICENSE.txt',
    description='The default modules of modularirc.',
    long_description=open('README.md').read(),
    install_requires=[
        'modularircbot',
        'requests',
        'python-mpd',
        'python-dateutil',
        'hurry.filesize',
        'pytz',
    ],

    test_suite='tests',
)