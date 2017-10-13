#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

version = '0.0.1'

setup(
    name='releaser_demo',
    version=version,
    description='Zest Releaser Demo',
    long_description=('loooooooooooooooooooooooooooooooooooooonnng description.....................'*10),
    author='Tomas Pulmano',
    author_email='tomas@scopely.com',
    keywords='demo',
    url='github.com/scopely',
    packages=find_packages(),
    install_requires=(),
    include_package_data=True,
    license='Apache 2.0',
    zip_safe=True,
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
    extras_require={
        'dev': ['zest.releaser[recommended]']
    }
)
