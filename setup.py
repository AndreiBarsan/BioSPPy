﻿# -*- coding: utf-8 -*-
"""
BioSPPy
-------

A toolbox for biosignal processing written in Python.

:copyright: (c) 2015-2017 by Instituto de Telecomunicacoes
:license: BSD 3-clause, see LICENSE for more details.
"""

# Imports
from setuptools import find_packages, setup
import os
import re


def read(*paths):
    """Build a file path from *paths and return the contents."""

    with open(os.path.join(*paths), 'r') as fid:
        return fid.read()


def get_version():
    """Get the module version."""

    with open('biosppy/version.py', 'r') as fid:
        txt = fid.read()

    m = re.search("version\s*=\s*'([\w.]+)'", txt)

    if m:
        try:
            ver = m.group(1)
        except IndexError:
            raise Exception("Could not parse version string.")

    ver = ver.strip()

    return ver


setup(name='biosppy',
      version=get_version(),
      description="A toolbox for biosignal processing written in Python.",
      long_description=read('README.rst'),
      url='https://github.com/PIA-Group/BioSPPy',
      license='BSD 3-clause',
      author='Instituto de Telecomunicacoes',
      author_email='carlos.carreiras@lx.it.pt',
      packages=find_packages(exclude=['tests*', 'docs*', 'examples']),
      # install_requires=[],
      include_package_data=True,
      classifiers=['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Education',
                   'Intended Audience :: Science/Research',
                   'License :: OSI Approved :: BSD License',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.5',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Education',
                   'Topic :: Scientific/Engineering',
                   ],
      )
