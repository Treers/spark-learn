# -*- coding: utf-8 -*-

hard_dependencies = ("numpy", "pandas")
missing_dependencies = []

from IPython import get_ipython

ipython = get_ipython()

import logging
logging.captureWarnings(capture=True)

import warnings
warnings.filterwarnings("ignore")


try:
   ipython.magic('%matplotlib inline')
except:
   pass	


for dependency in hard_dependencies:
    try:
        __import__(dependency)
    except ImportError as e:
        missing_dependencies.append(dependency)

if missing_dependencies:
    raise ImportError(
        "Missing required dependencies {0}".format(missing_dependencies))
del hard_dependencies, dependency, missing_dependencies

__version__ = '0.1.0'
