"""Unit tests for gal.py"""
import unittest
import pysal
import tempfile
import os
from pysal.core.IOHandlers.gal import GalIO

class Test_GalIO(unittest.TestCase):
    def setUp(self):
        self.test_file = test_file = '../../../examples/sids2.gal'
        self.obj = GalIO(test_file, 'r')

    def test___init__(self):
        self.assertEqual(self.obj._typ, str)

    def test_close(self):
        f = self.obj
        f.close()
        self.failUnlessRaises(ValueError, f.read)

    def test_read(self):
        # reading a GAL returns a W
        w = self.obj.read()
        self.assertEqual(w.n, 100)
        self.assertAlmostEqual(w.sd, 1.5151237573214935 )
        self.assertEqual(w.s0, 462.0 )
        self.assertEqual(w.s1, 924.0 )

    def test_seek(self):
        # gal_i_o = GalIO(*args, **kwargs)
        # self.assertEqual(expected, gal_i_o.seek(pos))
        assert False # TODO: implement your test here

    def test_write(self):
        w = self.obj.read()
        f = tempfile.NamedTemporaryFile(suffix='.gal')
        fname = f.name
        f.close()
        o = pysal.open(fname,'w')
        o.write(w)
        o.close()
        wnew =  pysal.open(fname,'r').read()
        self.assertEqual(wnew.pct_nonzero, w.pct_nonzero)


if __name__ == '__main__':
    unittest.main()
