"""
Python Spatial Analysis Library
===============================


Documentation
-------------
PySAL documentation is available in two forms: python docstrings and a html webpage at http://pysal.org/

Available subpackages
---------------------
cg
    Basic data structures and tools for Computational Geometry
core
    Basic functions used by several sub-packages
esda
    Tools for Exploratory Spatial Data Analysis
examples
    Example data sets used by several sub-packages for examples and testing
weights
    Tools for creating and maniputlating weights

Utilities
---------
open <fileio.rst>
    Tool for file input and output, supports many well known file formats
__version__
    PySAL version string
"""
import cg
import core
import esda
import weights

import pysal.core.FileIO # Load IO metaclass
import pysal.core._FileIO # Load IO inheritors

#Assign pysal.open to dispatcher

open = pysal.core.FileIO.FileIO
__version__ = '1.0.0rc1'
