#!/usr/local/bin/python
"""

    pyCarpetPlot.py 

Plotly class for generating carpet plot 

Copyright (c) 2004-2013 by pyACDT Developers
All rights reserved.
Revision: Stephen Andrews - $Date: 02/04/2014$


Developers:
-----------
- Stephen Andrews (SA) 

History
-------
    v. Stephen Andrews  - 
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
import pdb
from math import radians, sin, cos, ceil

# =============================================================================
# External Python modules
# =============================================================================
import numpy
import plotly.plotly as py
from plotly.graph_objs import *
# =============================================================================
# Extension modules
# =============================================================================
sys.path.append(os.path.abspath('../python-api'))

# =============================================================================
# 
# =============================================================================

class CarpetPlot:

    def __init__(self, x1, x2, y, ofst = 1.0, ofst2 = 0.0, figure = None, x1_skip = 1, x2_skip = 1, idep2_style = None,
        label1 = '', label2 = '',  label1_loc = 'end', label2_loc = 'end', label1_ofst = (15, 0), label2_ofst = (15, 0), 
        title = '', title_loc = (1.0, 0.9), dep_title = '', x_cheat_out = None):
        # contour_data = None, contour_format = [{}], clabel_format = {},
        '''

        Generates a carpet plot of the data 

        Plots the data in :math:`y` against the 'cheater axis' 

        _math::

            x_{cheat} = x_1 + \mathrm{ofst} \cdot x_2

        This shows the relationship between x1 and x2 with y but destroys information about how y varries with
        x1 and x2 

        **Inputs** 

        - x1 -> (n x 1) numpy array: Vector of first independent values.
        - x2 -> (m x 1) numpy array: Vector of second independent values.
        - y -> (n x m) numpy.array: Matrix of dependant values.
        - ofst -> FLOAT: Offset factor, can be used to change the shape of the plot, *Default 1.0*
                            - ofst = 1 : trend of y with x1 and x2 of similar magnitude
                            - ofst > 1 : trend of y with x2 more pronounced 
                            - ofst < 1 : trend of y with x1 more pronounced
        - ofst2 -> FLOAT: Offset for plotting multiple carpet plots on one axis
        - idep2_style -> STR: Format string for second independent variable lines. None is same as x1 *Default: None*
        - axis -> matplotlib.pyplot.axis: An axis object to plot on
        - x1_skip -> INT: Value n to read every n values. 
        - x2_skip -> INT: Value n to read every n values.
        - label1 -> STR: Labels to append to the curves of x1. *Default: ''* 
        - label2 -> STR: Labels to append to the curves of x2. *Default: ''* 
        - label1_loc -> STR: Location of x1 labels. *Default: 'end'* 
                        - 'end': at the end of the data 
                        - 'start': at the start of the data 
                        - None: do not show labels
        - label2_loc -> STR: Location of x2 labels. *Default: 'end'* 
                        - 'end': at the end of the data 
                        - 'start': at the start of the data 
                        - None: do not show labels
        - label1_ofst -> 2-TUPPLE: X and Y offset, in pixels, from the selected vertex 
        - label2_ofst -> 2-TUPPLE: X and Y offset, in pixels, from the selected vertex
        - title -> STR: String to place above the carpet plot
        - title_loc -> 2-TUPPLE: X and Y modifiers for the title location 
                - [0] modifier to the midpoint of the x range 
                - [1] modifier to the max y point
        - dep_title -> STR: Title to append to the dependent axis
        - x_cheat_out -> LIST: IO variable for cheater axis values


        **Depricated**
        - contour_data - > LIST of (n x m) numpy.array: List of  matrices of dependent values to plot as a contour. *Default: None*
        - contour_format -> LIST of DICT: List of Dictionaries of contour formating inputs 
        - cabel_format -> LIST DICT: List of Dictionaries of contour label formating inputs 

        '''

        # Input checks and conditioning
        y = numpy.array(y)

        for var in [y]: 
            if var.shape == (): 
                pass
            elif not (len(x2), len(x1)) == var.shape:
                raise Exception('Shape of input does not agree %s != (%d x %d)'%(var.shape, len(x2), len(x1)))
            #end
        #end

        def label_map(label_loc):     
            if label_loc == None : return None
            elif label_loc.lower()[0] == 's': return 0
            elif label_loc.lower()[0] == 'e': return -1
            else: raise Exception('Invalid data label location')
        #end
        
        label1_loc, label2_loc = map(label_map, [label1_loc, label2_loc])

        xx1, xx2 = numpy.meshgrid(x1, x2)

        x_cheat = ofst2 + (xx1 + ofst * xx2)
        x_cheat_out = x_cheat
        
        data = []
        annotations = []
        for i in xrange(0,len(x1),x1_skip):
            data.append(Scatter(x = x_cheat[:,i], y = y[:,i], line = Line(color = 'black', dash = 'solid')))
            if not label1_loc == None:            
                annotations.append(Annotation(text = '{:}={:3.2f}'.format(label1, x1[i]),  x = x_cheat[label1_loc,i], y =  y[label1_loc,i], ax = label1_ofst[0], ay = label1_ofst[1], xanchor = 'x1', yanchor = 'y1', arrowcolor = 'grey', showarrow = True))
            #end
        #end

        for i in xrange(0,len(x2),x2_skip):
            data.append(Scatter(x = x_cheat[i,:], y = y[i,:], line = Line(color = 'black', dash = 'solid')))
            if not label2_loc == None:
                annotations.append(Annotation(text = '{:}={:3.2f}'.format(label2, x2[i]), x = x_cheat[i,label2_loc], ax = label2_ofst[0], y = y[i,label2_loc], ay = label2_ofst[1], xanchor = 'x1', yanchor = 'y1', arrowcolor = 'grey', showarrow = True))
            #end
        #end

        #>>>Depricated contour plot
        #>>>Depricated contour plot
        annotations = Annotations(annotations)
        self.layout = Layout(title = title, showlegend = False, xaxis = XAxis(showticklabels = False), yaxis = YAxis(title = dep_title), annotations = annotations)
        self.data = Data(data)

        return 
    #end


if __name__ == '__main__':
    f = lambda x1 ,x2: x1**2+x2**2-2*x1-2*x2+2
    f2 = lambda x1 ,x2: (x1*x2)**0.5

    x1 = numpy.linspace(2,5,4)
    x2 = numpy.linspace(1,3,3)

    fobj = []
    contour = []
    for i in xrange(len(x1)):
        tmp = []
        tmp2 = []
        for j in xrange(len(x2)):
            tmp.append(f(x1[i], x2[j]))
            tmp2.append(f2(x1[i], x2[j]))
        #end
        fobj.append(tmp)
        contour.append(tmp2)
    #end

    fobj = numpy.array(fobj)
    contour = numpy.array(contour)

    # pdb.set_trace()
    cplot = CarpetPlot(x1,x2,fobj.T, ofst = 3, label1 = 'x1', label2 = 'x2', label1_loc = 'end', label1_ofst = (40,1), label2_ofst = (1,-30), dep_title = 'Dependant Variable')
    figure = Figure(data = cplot.data, layout = cplot.layout)
    py.plot(figure, filename = 'carpet plot test', overwrite = True)
