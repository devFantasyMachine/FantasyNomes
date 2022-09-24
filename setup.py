# -*- coding: utf-8 -*-

import os
import sys


# ensure the current directory is on sys.path
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from setuptools import find_packages, setup  # noqa: E402
import versionner as versionner 


setup(
    version = versionner.__version__,
    keywords = 'FantasyNomes',
    package_dir = {'': 'src'},
    packages = find_packages(where='src'),
    # packages_dir = {'CrossSection' : './src/CrossSection'}
)



del os
del sys

