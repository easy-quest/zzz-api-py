#!/data/data/com.termux/files/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name='zzz-api',
    version='0.0.1',
    packages=find_packages(),
    install_requires=['click', 'rich', 'termux-api'],
    entry_points={
        'console_scripts': [
            'zzz=zzz:cli',
            'colors=colors:cli',
            'termui=termui:cli',
            'kvdb=ex.kvdb:cli',
        ],
    },
)
