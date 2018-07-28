#!/usr/bin/env python

import os
import re
# import sys
# import glob

from setuptools import setup

# Global functions
##################

with open(os.path.join('skeleton', '__init__.py'), encoding='utf-8') as f:
    version = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", f.read(), re.M).group(1)

if not version:
    raise RuntimeError('Cannot find version information.')

with open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

def get_data_files():
    data_files = [
        ('share/doc/skeleton', ['AUTHORS', 'README.rst'])
    ]
    return data_files

def get_install_requires():
    requires = []

    if sys.version_info < (2, 7):
        requires += ['argparse']

    return requires


setup(
    name='skeleton',
    version=version,
    description="Skeleton is ...",
    long_description=long_description,
    author='Nicolas Hennion',
    author_email='nicolas@nicolargo.com',
    url='https://github.com/nicolargo/skeleton',
    license="MIT",
    keywords="...",
    install_requires=get_install_requires(),
    extras_require={},
    packages=['skeleton'],
    include_package_data=True,
    data_files=get_data_files(),
    # test_suite="skeleton.test",
    entry_points={"console_scripts": ["skeleton=skeleton:main"]},
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 2',
    ]
)
