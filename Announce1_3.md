# PySAL 1.3 Released (2012-02-01) #

On behalf of the PySAL development team, I'm happy to announce the
official release of PySAL 1.3.
PySAL is a library of tools for spatial data analysis and
geocomputation written in Python. PySAL 1.3, the fourth official
release of PySAL, includes a number of new features and enhancements:

  * The spatial regression module (spreg) has added:
    * Two Stage Least Squares
    * Spatial Two Stage Least Squares
    * GM Error (KP 98-99)
    * GM Error Homoskedasticity (Drukker et. al, 2010)
    * GM Error Heteroskedasticity (Arraiz et. al, 2010)
    * Spatial HAC variance-covariance estimation
    * Anselin-Kelejian test for residual spatial autocorrelation
of residuals from IV regression
    * New utility functions and other helper classes
  * A new contrib module to support user contributed modules. The first
> > contributed modules are:
      * Weights Viewer – A Graphical tool for examining spatial weights
      * World To View Transform – A class for modeling viewing
windows, used by Weights Viewer
      * Shapely Extension – Exposes shapely methods as standalone functions
      * Shared Perimeter Weights – calculate shared perimeters weights


along with many bug fixes and smaller enhancements.

PySAL modules

---


  * pysal.core — Core Data Structures and IO
  * pysal.cg — Computational Geometry
  * pysal.esda — Exploratory Spatial Data Analysis
  * pysal.inequality — Spatial Inequality Analysis
  * pysal.spatial\_dynamics — Spatial Dynamics
  * pysal.spreg - Regression and Diagnostics
  * pysal.region — Spatially Constrained Clustering
  * pysal.weights — Spatial Weights
  * pysal.FileIO — PySAL FileIO: Module for reading and writing
various file types in a Pythonic way

> - pysal.contrib — Contributed Modules

Downloads

---

Binary installers and source distributions are available for download at
http://code.google.com/p/pysal/downloads/list

Documentation

---

The documentation site is here
> http://pysal.org/1.3/contents.html

Web sites

---

PySAL's home is here
> http://pysal.org/

The developer's site is here
> http://code.google.com/p/pysal/

Mailing Lists

---

Please see the developer's list here
> http://groups.google.com/group/pysal-dev

Help for users is here
> http://groups.google.com/group/openspace-list

Bug reports

---

To search for or report bugs, please see
http://code.google.com/p/pysal/issues/list

License information

---

See the file "LICENSE.txt" for information on the history of this
software, terms & conditions for usage, and a DISCLAIMER OF ALL
WARRANTIES.


Many thanks to all who contributed!

Serge, on behalf of the PySAL development team.