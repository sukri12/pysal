﻿#summary How to build PySAL distributions

# Introduction #

This page explains how to build source and "binary" distributions of PySAL.

# Source Distributions #

The work of specifying files and folders to include in a PySAL source distribution has been done.  These things are specified in setup.py and MANIFEST.in.  To build a new source package, run `python setup.py sdist --formats=gztar,zip` to generate two source distributions.

A good reference is http://docs.python.org/distutils/sourcedist.html

# Binary distros #

## Windows ##
Build distribution installers for Windows on Windows machines to ensure that the proper dynamic libraries are included in the distributables.  There are two Windows installer formats.  The MSI installer allows the user to specify the location to install PySAL, whereas the .exe offers a choice based on the registered Python executables found on the host system.

  * Run `python setup.py bdist_wininst` to build the .EXE graphical installer.
  * Run `python setup.py bdist --formats=msi` to build the MSI installer .

## OS X Darwin ##
To make a Mac OS X graphical installer, first install 'bdist\_mpkg' from the Python Package Index. We recommend downloading the source code and using the included setup.py file to install.  Note that you can install multiple versions of bdist\_mpkg, so be sure you know which one you're calling, and which Python it is associated with.  For instance, below we include edits to alter the .mpkg produced by bdist\_mpkg so that PySAL will be installed in the Current version of Python in the Python Frameworks (i.e. /Library/Frameworks/Python.framework/ ... ). That includes any or most Python distributions **not** included by Apple, such as those from python.org and Enthought.

If you were targeting just one of those distributions, EPD for example, you could forego our edits below by installing a version of bdist\_mpkg using the EPD Python executable. Likewise, if you're only interested to direct the installer to Python 2.6.6 distributed by python.org, you'd use the bdist\_mpkg built by **that** executable, and forego the edits below.  The same will hold true for other versions of Python, such as Python2.7 or 3.2., or for Apple-installed Python located at /usr/bin/python.

Next, build the package by running `bdist_mpkg setup.py build`, which builds your package installer in the dist/ directory.  **The mpkg will need to be modified to install to the correct location.** _Replace wildcards below with actual filenames_.

  1. Edit `pysal*.mpkg/Contents/Info.plist` replacing the path under `IFRequirementDicts` with a generic System path such as, `/Library/Frameworks/Python.framework/Versions/Current/lib/python2.6/site-packages`.  This will check that directory exists before installing.  Note that `Version/Current/lib/python2.6` is a work around to support both 'Frameworks' Python and the Enthought Python Distribution (EPD).
  1. Next find and edit `pysal*.mpkg/Contents/Packages/pysal*.pkg/Contents/Info.plist`.  Change the value after `IFPkgFlagDefaultLocation` to point to `/Library/Frameworks/Python.framework/Versions/Current/lib/python2.6/site-packages`
  1. Next, convert that file (ending in ".mpkg") into a disk image suitable for distribution by executing the following command: `hdiutil create -fs HFS+ -srcfolder pysal*.mpkg/ pysal-x.x.x-py2.X-macosx10.X.dmg`