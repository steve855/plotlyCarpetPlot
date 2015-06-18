#!/usr/local/bin/python
"""

    2_indep_1_dep.py 

Carpet plot of two independant variables against one dependant  

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

# =============================================================================
# Extension modules
# =============================================================================
sys.path.append(os.path.abspath('../'))

from carpetPlot import *

# =============================================================================
# 
# =============================================================================

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

# cplot = CarpetPlot(x1,x2,fobj.T, ofst = 3, label1 = 'x1', label2 = 'x2', label1_loc = 'end', label1_ofst = (40,1), label2_ofst = (1,-30), dep_title = 'Dependant Variable')

figure = Figure(data = Data([Contour(x = x1, y = x2, z = fobj, showscale = False, autocontour = False, ncontours = 5, line = Line(color = 'grey', dash = 'dashdot'), contours = Contours(showlines = True, coloring = 'none') )]))

py.plot(figure, filename = 'contour test', overwrite = True)