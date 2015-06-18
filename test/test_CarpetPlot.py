#!/usr/local/bin/python
"""

    test_CarpetPloy.py 

Test of CarpetPlot class

Copyright (c) 2015 by Stephen Andrews
All rights reserved.
Revision: 1.0 - $Date: 18/06/2015$


Developers:
-----------
- Stephen Andrews (SA) 

History
-------
    v. 1
   .0  - 
"""

__version__ = '$Revision: $'

"""
To Do:
    - 
"""

# =============================================================================
# Standard Python modules
# =============================================================================
import os, sys
# =============================================================================
# External Python modules
# =============================================================================
import numpy
import unittest
# =============================================================================
# Extension modules
# =============================================================================
sys.path.append(os.path.abspath('../'))

from carpetPlot import *

# =============================================================================
# 
# =============================================================================
class test_CarpetPlot(unittest.TestCase):
    def setUp(self):    
        f = lambda x1 ,x2: x1**2+x2**2-2*x1-2*x2+2

        x1 = numpy.linspace(2,5,4)
        x2 = numpy.linspace(1,3,3)

        fobj = []
        for i in xrange(len(x2)):
            tmp = []
            for j in xrange(len(x1)):
                tmp.append(f(x1[j], x2[i]))
            #end
            fobj.append(tmp)
        #end
        fobj = numpy.array(fobj) 

        self.x1 = x1 
        self.x2 = x2 
        self.y = fobj


    def test_y_shape_test(self):

        CarpetPlot(self.x1, self.x2, self.y)

        with self.assertRaises(Exception):
            CarpetPlot(self.x2, self.x1, self.y)
        #end
            
    def test_valid_labels_loc_keys(self):

        CarpetPlot(self.x1, self.x2, self.y, label1_loc = 'start', label2_loc = 'start')
        CarpetPlot(self.x1, self.x2, self.y, label1_loc = 'end', label2_loc = 'end')
        CarpetPlot(self.x1, self.x2, self.y, label1_loc = None, label2_loc = None)

    def test_invalid_labels_loc_keys(self):

        with self.assertRaises(Exception):
            CarpetPlot(self.x1, self.x2, self.y, label1_loc = 'potato', label2_loc = 'start')
        
        with self.assertRaises(Exception):
            CarpetPlot(self.x1, self.x2, self.y, label1_loc = 0, label2_loc = 'end')

    def test_skip(self):
        pass 

    def test_strings(self):
        CarpetPlot(self.x1, self.x2, self.y, label1 = 'a nice, valid string', label2 = 'a nice, valid string', title ='a nice, valid string', dep_title = 'a nice, valid string')
 
    def test_invalid_strings(self):
        CarpetPlot(self.x1, self.x2, self.y, label1 = 0, label2 = 'a nice, valid string', title ='a nice, valid string', dep_title = 'a nice, valid string')
        CarpetPlot(self.x1, self.x2, self.y, label1 = 'a nice, valid string', label2 = 0.0, title ='a nice, valid string', dep_title = 'a nice, valid string')
        CarpetPlot(self.x1, self.x2, self.y, label1 = 'a nice, valid string', label2 = 'a nice, valid string', title =None, dep_title = 'a nice, valid string')
        CarpetPlot(self.x1, self.x2, self.y, label1 = 'a nice, valid string', label2 = 'a nice, valid string', title ='a nice, valid string', dep_title = 0)
        


if __name__ == '__main__':
    unittest.main(verbosity=2)   