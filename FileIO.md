﻿#summary An Overview of the FileIO system in PySAL.
#labels Deprecated,Phase-Support

# Introduction #

PySAL contains a new file input-output API that should be used for all file IO operations. The goal is to abstract file handling and return native PySAL data types when reading from known file types. A list of known extensions can be found by issuing the following command.

```
>>> pysal.open.check()
PySAL File I/O understands the following file extensions:
Ext: '.shp', Modes: ['r', 'wb', 'w', 'rb']
Ext: '.shx', Modes: ['r', 'wb', 'w', 'rb']
Ext: '.geoda_txt', Modes: ['r']
Ext: '.dbf', Modes: ['r', 'w']
Ext: '.gwt', Modes: ['r']
Ext: '.gal', Modes: ['r']
Ext: '.csv', Modes: ['r']
Ext: '.wkt', Modes: ['r']
>>>
```

Note that in some cases the FileIO module will peek instead your file to determine it's type. For example "geoda\_txt" is just a unique scheme for ".txt" files, so when opening a ".txt" pysal will peek inside the file to determine it if has the necessary header information and dispatch accordingly.  In the event that pysal does not understand your file IO operations will be dispatched to python's internal open.

# Examples #

## Reading files into Python ##

**NOTE**: all the examples assume you are in the directory `../trunk/pysal/examples`

**Shapefiles**
```
>>> import pysal
>>> shp = pysal.open('10740.shp')
>>> shp.next()
<pysal.cg.shapes.Polygon object at 0xd01e50>
>>> len(shp)
195
>>> shp.get(len(shp)-1).id
195
>>> polys = list(shp)
>>> len(polys)
195
```

**DBF Files**
```
>>> import pysal
>>> db = pysal.open('10740.dbf','r')
>>> db.header
['GIST_ID', 'FIPSSTCO', 'TRT2000', 'STFID', 'TRACTID']
>>> db.field_spec
[('N', 8, 0), ('C', 5, 0), ('C', 6, 0), ('C', 11, 0), ('C', 10, 0)]
>>> db.next()
[1, '35001', '000107', '35001000107', '1.07']
>>> db[0]
[[1, '35001', '000107', '35001000107', '1.07']]
>>> db[0:3]
[[1, '35001', '000107', '35001000107', '1.07'], [2, '35001', '000108', '35001000108', '1.08'], [3, '35001', '000109', '35001000109', '1.09']]
>>> db[0:5,1]
['35001', '35001', '35001', '35001', '35001']
>>> db[0:5,0:2]
[[1, '35001'], [2, '35001'], [3, '35001'], [4, '35001'], [5, '35001']]
>>> db[-1,-1]
['9712']
```

**CSV Files**
```
>>> import pysal
>>> db = pysal.open('stl_hom.csv')
>>> db.header
['WKT', 'NAME', 'STATE_NAME', 'STATE_FIPS', 'CNTY_FIPS', 'FIPS', 'FIPSNO', 'HR7984', 'HR8488', 'HR8893', 'HC7984', 'HC8488', 'HC8893', 'PO7984', 'PO8488', 'PO8893', 'PE77', 'PE82', 'PE87', 'RDAC80', 'RDAC85', 'RDAC90']
>>> db[0]
[['POLYGON ((-89.585220336914062 39.978794097900391,-89.581146240234375 40.094867706298828,-89.603988647460938 40.095306396484375,-89.60589599609375 40.136119842529297,-89.6103515625 40.3251953125,-89.269027709960938 40.329566955566406,-89.268562316894531 40.285579681396484,-89.154655456542969 40.285774230957031,-89.152763366699219 40.054969787597656,-89.151618957519531 39.919403076171875,-89.224777221679688 39.918678283691406,-89.411857604980469 39.918041229248047,-89.412437438964844 39.931644439697266,-89.495201110839844 39.933486938476562,-89.4927978515625 39.980186462402344,-89.585220336914062 39.978794097900391))', 'Logan', 'Illinois', 17, 107, 17107, 17107, 2.1154280000000001, 1.2907219999999999, 1.624458, 4, 2, 3, 189087, 154952, 184677, 5.1043200000000004, 6.5957800000000004, 5.8329510000000004, -0.99125600000000003, -0.94026500000000002, -0.84500500000000001]]
>>> fromWKT = pysal.core._FileIO.wkt.WKTParser()
>>> db.cast('WKT',fromWKT)
>>> db[0]
[[<pysal.cg.shapes.Polygon object at 0xd048b0>, 'Logan', 'Illinois', 17, 107, 17107, 17107, 2.1154280000000001, 1.2907219999999999, 1.624458, 4, 2, 3, 189087, 154952, 184677, 5.1043200000000004, 6.5957800000000004, 5.8329510000000004, -0.99125600000000003, -0.94026500000000002, -0.84500500000000001]]
>>> polys = db.by_col('WKT')
>>> from pysal.cg import standalone
>>> standalone.get_bounding_box(polys)[:]
[-92.700675964355469, 36.881809234619141, -87.916572570800781, 40.329566955566406]
```

## Writing out files ##

**Shapefiles**
```
#Having shp from the reading example, write the second polygon (.dbf order)
>>> fo=pysal.open('scnd_poly.shp','w')
>>> fo.write(polys[1])
>>> fo.close()
```

**DBF files**
```
#With the object db from the DBF reading example, create a .dbf for scnd_poly.shp
>>> odb=pysal.open('scnd_poly.dbf','w')
>>> odb.header=db.header
>>> odb.field_spec=db.field_spec
>>> odb.write(db[1][0])
>>> odb.close()
```