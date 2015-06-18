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
	def setup(self):	
		f = lambda x1 ,x2: x1**2+x2**2-2*x1-2*x2+2

		x1 = numpy.linspace(2,5,4)
		x2 = numpy.linspace(1,3,3)

		fobj = []
		for i in xrange(len(x1)):
		    tmp = []
		    for j in xrange(len(x2)):
		        tmp.append(f(x1[i], x2[j]))
		    #end
		    fobj.append(tmp)
		#end
		fobj = numpy.array(fobj) 

		self.x1 = x1 
		self.x2 = x2 
		self.y = fobj

	
if __name__ == '__main__':
    unittest.main(verbosity=2)   