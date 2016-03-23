# Introduction #
The module `esda` provides classes to perform Exploratory Spatial Data Analysis (ESDA) in PySAL.

**NOTE** All the examples below assume you have loaded some data into Python. You can use some of the data in the examples folder ('/pysal/examples'). To load them, first go to the folder:
`cd /path_to_pysal_trunk/pysal/examples`

Unless explicitly noted, we will use the 'desmith' data. You can load them by copying and pasting the following:

```
>>> import numpy as N
>>> import pysal
# Read the weights matrix as W object
>>> W=pysal.open('desmith.gal')._read()

# Read data
>>> y=pysal.open('desmith.txt')
# Get the column 'z' of the table
>>> y=y._get_col('z')
# Make it a numpy array
>>> y=N.array(y)
```

For more info on reading data into PySAL, see FileIO.

# Classes #

## Geary ##
## **`class Geary`** ##

Computation of Global Geary C autorcorrelation statistic.

### References ###
  * Geary, R.C. (1954). [The Contiguity Ratio and Statistical Mapping](http://www.jstor.org/pss/2986645). 5. The Incorporated Statistician. pp. 115–145
  * Cliff, A. D., Ord, J. K. 1981 Spatial processes, Pion, p. 17
  * [Wikipedia](http://en.wikipedia.org/wiki/Geary%27s_C)

### Arguments ###
  * y: n`*`1 array
  * w: weight instance assumed to be aligned with y
  * transformation: weights transformation, default is row-standardized (`W`). Other options include:
    * `B`: binary
    * `D`: doubly-standardized
    * `U`: untransformed (general weights)
    * `V`: variance-stabilizing
  * permutations: number of random permutations for calculation of pseudo-p\_values (by default set to 999).

### Attributes ###
  * y: original variable
  * w: original w object
  * permutation: number of permutations
  * C: value of statistic
  * C: expected value
  * C: variance of G under normality assumption
  * _norm: z-statistic for C under normality assumption
  *_rand: z-statistic for C under randomization assumption
  * _norm: p-value under normality assumption (one-tailed)
  *_rand: p-value under randomization assumption (one-tailed)

(if permutations>0)

  * im: vector of I values for permutated samples
  * _sim: p-value based on permutations
  * C\_sim: average value of C from permutations
  * C\_sim: variance of C from permutations
  * eC\_sim: standard deviation of C under permutations.
  *_sim: standardized C based on permutations
  * _z\_sim: p-value based on standard normal approximation from permutations_

### Example ###
```
>>> from pysal.esda.geary import Geary
>>> c=Geary(y,W)
>>> c
<pysal.esda.geary.Geary instance at 0x22a9cd8>
>>> c.C
1.0306280397350873
>>> c.EC
1.0
>>> c.z_norm
0.12478140903940312
>>> c.z_rand
0.11778731158293086
>>> c.p_norm
0.39584849345282647
>>> c.p_rand
0.39618442415010757
>>> c.p_sim
0.41699999999999998
>>> c.EC_sim
0.99897710985735588
>>> c.VC_sim
0.060532146040864848
>>> c.seC_sim
0.24603281496756657
>>> c.z_sim
0.12864515606141336
>>> c.p_z_sim
0.39565473818765856
>>> 
```

## Moran ##
## **`class Moran`** ##

Computation of the global version of the Moran's I statistic for spatial autocorrelation.

### References ###
  * Moran, P.A.P. (1948). The interpretation of statistical maps. Journal of the Royal Statistical Society. Series B (Methodological). pp. 243-251.
  * [Wikipedia](http://en.wikipedia.org/wiki/Moran's_I)

### Arguments ###
  * y: n`*`1 array
  * w: weight instance assumed to be aligned with y
  * transformation: weights transformation, default is row-standardized (`W`). Other options include:
    * `B`: binary
    * `D`: doubly-standardized
    * `U`: untransformed (general weights)
    * `V`: variance-stabilizing
  * permutations: number of random permutations for calculation of pseudo-p\_values (by default set to 999)

### Attributes ###
  * y: original variable
  * w: original w object
  * permutation: number of permutations
  * I: value of statistic
  * I: expected value
  * I\_norm: variance of I under normality assumption
  * eI\_norm: standard deviation of I under normality assumption
  * _norm: z-statistic for I under normality assumption
  *_norm: p-value of I under normality assumption (1-tailed)
  * I\_rand: variance of I under randomization assumption
  * eI\_rand: standard deviation of I under randomization assumption
  * _rand: z-statistic for I under randomization assumption
  *_rand: p-value under randomization assumption (one-tailed)

(if permutations>0)

  * im: vector of I values for permutated samples
  * _sim: p-value based on permutations
  * I\_sim: average value of I from permutations
  * I\_sim: variance of I from permutations
  * eI\_sim: standard deviation of I under permutations.
  *_sim: standardized I based on permutations
  * _z\_sim: p-value based on standard normal approximation from permutations_

### Example ###
```
>>> from pysal.esda.moran import Moran
>>> I=Moran(y,W)
>>> I
<pysal.esda.moran.Moran instance at 0x22a9968>
>>> I.I
0.073612431110602214
>>> I.EI
-0.1111111111111111
>>> I.VI_norm
0.057491582491582496
>>> I.seI_norm
0.23977402380487861
>>> I.z_norm
0.77040681592780114
>>> I.p_norm
0.29650183721625545
>>> I.VI_rand
0.029046956609752865
>>> I.seI_rand
0.17043167724854691
>>> I.z_rand
1.0838568580905537
>>> I.p_rand
0.22172633614104503
>>> I.p_sim
0.35899999999999999
>>> I.EI_sim
0.0073148505013345896
>>> I.VI_sim
0.028895203917500886
>>> I.seI_sim
0.16998589328971062
>>> I.z_sim
0.39001813224745208
>>> I.p_z_sim
0.36972506950229339
>>> 
```


## **`class Moran_BV`** ##

Computation of bivariate version of Moran's I global statistic of spatial autocorrelation.

### References ###
  * Anselin, L. (2005). [Exploring Spatial Data with GeoDa: A Workbook](http://www.csiss.org/clearinghouse/GeoDa/geodaworkbook.pdf). Center for Spatially Integrated Social Science. See section 21 (from page 155 on).

### Arguments ###
  * y1: n`*`1 array with the variable to be used as main one
  * y2: n`*`1 array with the variable to be spatially lagged
  * w: weight instance assumed to be aligned with y
  * transformation: weights transformation, default is row-standardized (`W`). Other options include:
    * `B`: binary
    * `D`: doubly-standardized
    * `U`: untransformed (general weights)
    * `V`: variance-stabilizing
  * permutations: number of random permutations for calculation of pseudo-p\_values (by default set to 999)

### Attributes ###
  * y: original variable
  * w: original w object
  * permutation: number of permutations
  * I: value of Moran's I

(if permutations>0)

  * im: vector of I values for permutated samples
  * _sim: p-value based on permutations
  * I\_sim: average value of I from permutations
  * I\_sim: variance of I from permutations
  * eI\_sim: standard deviation of I under permutations.
  *_sim: standardized I based on permutations
  * _z\_sim: p-value based on standard normal approximation from permutations_

**NOTE** Inference is only based on permutations as analytical results are none too reliable.

### Example ###

In this case, we will use the data from `stl_hom.csv`.

```
>>>dat=pysal.open('stl_hom.csv')
>>>y1=dat._get_col('HR7984')
>>>y1=N.array(y1)
>>>
>>>y2=dat._get_col('HR8488')
>>>y2=N.array(y2)
>>>
>>>W=pysal.open('stl.gal').read()
```

Once the data are loaded, you can obtain the bivariate moran as follows:

```
>>>from pysal.esda.moran import Moran_BV
>>> mbv=Moran_BV(y1,y2,W)
>>> mbv
<pysal.esda.moran.Moran_BV instance at 0x219b288>
>>> mbv.I
0.90800739921986295
>>> mbv.p_sim
0.0089999999999999993
>>> mbv.EI_sim
0.010925497047910789
>>> mbv.VI_sim
0.062796961073566859
>>> mbv.seI_sim
0.25059321833115689
>>> mbv.z_sim
3.5798331181750727
>>> mbv.p_z_sim
0.00065784507006177366
>>> 
```

## **`class Moran_Local`** ##

Computes local version of Moran's I, which is a Local Indicator of Spatial Association (LISA).

### References ###
  * Anselin, L. (1995). Local Indicators of Spatial Association-LISA. Geographical Analysis, Vol. 27, Number 2, pp. 93-115
  * [Wikipedia](http://en.wikipedia.org/wiki/Indicators_of_spatial_association)

### Arguments ###
  * y: n`*`1 array
  * w: weight instance assumed to be aligned with y
  * transformation: weights transformation, default is row-standardized (`W`). Other options include:
    * `B`: binary
    * `D`: doubly-standardized
    * `U`: untransformed (general weights)
    * `V`: variance-stabilizing
  * permutations: number of random permutations for calculation of pseudo-p\_values (by default set to 999)

### Attributes ###
  * y: original variable
  * w: original w object
  * permutation: number of permutations
  * Is: values of Moran's I
  * q: array of values indicated quadrat location: 1 HH, 2 LH, 3 LL, 4 HL

(if permutations>0)

  * im: vector of I values for permutated samples
  * _sim: p-value based on permutations
  * I\_sim: average value of I from permutations
  * I\_sim: variance of I from permutations
  * eI\_sim: standard deviation of I under permutations.
  *_sim: standardized I based on permutations
  * _z\_sim: p-value based on standard normal approximation from permutations_

**NOTE** p-values are one sided - where side is based on the original I value for each observation (in self.Is). In other words extreme is considered being further away from the origin and in the same direction than original I statistic  for the focal observation.

### Example ###
```
>>> from pysal.esda.moran import Moran_Local
>>> Is=Moran_Local(y,W)
>>> Is
<pysal.esda.moran.Moran_Local instance at 0x22a9d50>
>>> Is.Is
array([-0.11409277, -0.19940543, -0.13351408, -0.51770383,  0.48095009,
        0.12208113,  1.19148298, -0.58144305,  0.07101383,  0.34314301])
>>> Is.q
array([4, 4, 4, 2, 3, 3, 1, 4, 3, 3])
>>> Is.p_sim
array([ 0.269,  0.249,  0.454,  0.162,  0.152,  0.067,  0.052,  0.246,
        0.426,  0.271])
>>> Is.EI_sim
0.0043962065246146136
>>> Is.VI_sim
0.22196455856433647
>>> Is.seI_sim
0.47113114794538524
>>> Is.z_sim
array([-0.25149893, -0.43257941, -0.29272166, -1.10818408,  1.01151004,
        0.24979228,  2.5196525 , -1.24347383,  0.14139931,  0.71900744])
>>> Is.p_z_sim
array([ 0.38652281,  0.3633092 ,  0.38221136,  0.21589254,  0.23918576,
        0.38668819,  0.0166847 ,  0.18414126,  0.39497397,  0.30807119])
>>>
```