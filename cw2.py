
def clockwise(verts):
    """ Clockwise test copied from,
        http://trac.osgeo.org/gdal/browser/branches/1.5/gdal/ogr/ogrlinearring.cpp?rev=16127#L334
    """
    if len(verts) < 2:
        return True
    dfSum = 0.0
    for i in xrange(0,len(verts)-1):
        dfSum += verts[i][0] * verts[i+1][1] - verts[i][1] * verts[i+1][0]
    dfSum += verts[-1][0] * verts[0][1] - verts[-1][1] * verts[0][0]
    return dfSum < 0.0

def main():
    v = [(-106.57798, 35.174143999999998), (-106.583412, 35.174141999999996), (-106.58417999999999, 35.174143000000001), (-106.58377999999999, 35.175542999999998), (-106.58287999999999, 35.180543), (-106.58263099999999, 35.181455), (-106.58257999999999, 35.181643000000001), (-106.58198299999999, 35.184615000000001), (-106.58148, 35.187242999999995), (-106.58127999999999, 35.188243), (-106.58138, 35.188243), (-106.58108, 35.189442999999997), (-106.58104, 35.189644000000001), (-106.58028, 35.193442999999995), (-106.580029, 35.194541000000001), (-106.57974399999999, 35.195785999999998), (-106.579475, 35.196961999999999), (-106.57922699999999, 35.198042999999998), (-106.578397, 35.201665999999996), (-106.57827999999999, 35.201642999999997), (-106.57737999999999, 35.201642999999997), (-106.57697999999999, 35.201543000000001), (-106.56436599999999, 35.200311999999997), (-106.56058, 35.199942999999998), (-106.56048, 35.197342999999996), (-106.56048, 35.195842999999996), (-106.56048, 35.194342999999996), (-106.56048, 35.193142999999999), (-106.56048, 35.191873999999999), (-106.56048, 35.191742999999995), (-106.56048, 35.190242999999995), (-106.56037999999999, 35.188642999999999), (-106.56037999999999, 35.187242999999995), (-106.56037999999999, 35.186842999999996), (-106.56037999999999, 35.186552999999996), (-106.56037999999999, 35.185842999999998), (-106.56037999999999, 35.184443000000002), (-106.56037999999999, 35.182943000000002), (-106.56037999999999, 35.181342999999998), (-106.56037999999999, 35.180433000000001), (-106.56037999999999, 35.179943000000002), (-106.56037999999999, 35.178542999999998), (-106.56037999999999, 35.177790999999999), (-106.56037999999999, 35.177143999999998), (-106.56037999999999, 35.175643999999998), (-106.56037999999999, 35.174444000000001), (-106.56037999999999, 35.174043999999995), (-106.560526, 35.174043999999995), (-106.56478, 35.174043999999995), (-106.56627999999999, 35.174143999999998), (-106.566541, 35.174144999999996), (-106.569023, 35.174157000000001), (-106.56917199999999, 35.174157999999998), (-106.56938, 35.174143999999998), (-106.57061499999999, 35.174143999999998), (-106.57097999999999, 35.174143999999998), (-106.57679999999999, 35.174143999999998), (-106.57798, 35.174143999999998)]

    test = [clockwise(v) for i in xrange(10000)]
    print test.count(True)
    print test.count(False)


if __name__=='__main__':
    import cProfile
    cProfile.run('main()')
