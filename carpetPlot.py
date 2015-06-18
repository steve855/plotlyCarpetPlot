#!/usr/local/bin/python
"""

    carpetPlot.py 

Plotly class for generating carpet plot 

Copyright (c) 2014 by Stephen Andrews
All rights reserved.
Revision: Stephen Andrews - $Date: 18/06/2014$


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

class CarpetPlot:

    def __init__(self, x1, x2, y, ofst = 1.0, ofst2 = 0.0, figure = None, x1_skip = 1, x2_skip = 1, idep2_style = None,
        label1 = '', label2 = '',  label1_loc = 'end', label2_loc = 'end', label1_ofst = (15, 0), label2_ofst = (15, 0), 
        title = '', dep_title = ''):
        # contour_data = None, contour_format = [{}], clabel_format = {},
        '''

        Generates a carpet plot of the data 

        Plots the data in :math:`y` against the 'cheater axis' 

        _math::

            x_{cheat} = x_1 + \mathrm{ofst} \cdot x_2

        This shows the relationship between x1 and x2 with y but destroys information about how y varries with
        x1 and x2 

        **Inputs** 

        - x1          -> (n x 1) numpy array: Vector of first independent values.
        - x2          -> (m x 1) numpy array: Vector of second independent values.
        - y           -> (n x m) numpy.array: Matrix of dependant values.
        - ofst        -> FLOAT: Offset factor, can be used to change the shape of the plot, *Default 1.0*
                            - ofst = 1 : trend of y with x1 and x2 of similar magnitude
                            - ofst > 1 : trend of y with x2 more pronounced 
                            - ofst < 1 : trend of y with x1 more pronounced
        - ofst2       -> FLOAT: Offset for plotting multiple carpet plots on one axis
        - idep2_style -> STR: Format string for second independent variable lines. None is same as x1 *Default: None*
        - axis        -> matplotlib.pyplot.axis: An axis object to plot on
        - x1_skip     -> INT: Value n to read every n values.
        - x2_skip     -> INT: Value n to read every n values.
        - label1      -> STR: Labels to append to the curves of x1. *Default: ''*
        - label2      -> STR: Labels to append to the curves of x2. *Default: ''*
        - label1_loc  -> STR: Location of x1 labels. *Default: 'end'*
                            - 'end': at the end of the data 
                            - 'start': at the start of the data 
                            - None: do not show labels
        - label2_loc  -> STR: Location of x2 labels. *Default: 'end'*
                            - 'end': at the end of the data 
                            - 'start': at the start of the data 
                            - None: do not show labels
        - label1_ofst -> 2-TUPPLE: X and Y offset, in pixels, from the selected vertex
        - label2_ofst -> 2-TUPPLE: X and Y offset, in pixels, from the selected vertex
        - title       -> STR: String to place above the carpet plot
        - dep_title   -> STR: Title to append to the dependent axis

        '''

        # Input checks and conditioning
        y = numpy.array(y)

        for str_check in [title, dep_title, label1, label2]:
            if isinstance(str_check, str):
                pass 
            else:
                try:
                    str_check = str(str_check)
                except:
                    raise Exception('Could not convert {} to string'.format(str_check))
                #end
            #end 
        #end

        if not (len(x2), len(x1)) == y.shape:
            raise Exception('Shape of input does not agree {:} != ({:d} x {:d})'.format(y.shape, len(x2), len(x1)))
        #end

        def label_map(label_loc):
            try:     
                if label_loc == None : return None
                elif label_loc.lower()[0] == 's': return 0
                elif label_loc.lower()[0] == 'e': return -1
                else: raise Exception()
            except:
                raise Exception("Invalid data label location, valid options are 'start', 'end' and None")
            #end
        #end
        
        label1_loc, label2_loc = map(label_map, [label1_loc, label2_loc])

        xx1, xx2 = numpy.meshgrid(x1, x2)

        x_cheat = ofst2 + (xx1 + ofst * xx2)
        x_cheat_out = x_cheat
        
        data = []
        annotations = []
        for i in xrange(0,len(x1),x1_skip):
            text = []
            for j in xrange(len(y[:,i])):
                text.append("{:} = {:3.2f}, {:} = {:3.2f}".format(label1, x1[i], label2, x2[j]))
            #end
            data.append(dict(type = 'scatter', x = x_cheat[:,i], y = y[:,i], text = text, name = '', line = Line(color = 'black', dash = 'solid')))#, hoverinfo='none'))
            if not label1_loc == None:            
                annotations.append(Annotation(text = '{:}={:3.2f}'.format(label1, x1[i]),  x = x_cheat[label1_loc,i], y =  y[label1_loc,i], ax = label1_ofst[0], ay = label1_ofst[1], xanchor = 'x1', yanchor = 'y1', arrowcolor = 'grey', showarrow = True))
            #end
        #end

        for i in xrange(0,len(x2),x2_skip):
            data.append(dict(type = 'scatter', x = x_cheat[i,:], y = y[i,:], text = ['']*len(y[i,:]), name = '', line = Line(color = 'black', dash = 'solid')))#, hoverinfo='none'))
            if not label2_loc == None:
                annotations.append(Annotation(text = '{:}={:3.2f}'.format(label2, x2[i]), x = x_cheat[i,label2_loc], ax = label2_ofst[0], y = y[i,label2_loc], ay = label2_ofst[1], xanchor = 'x1', yanchor = 'y1', arrowcolor = 'grey', showarrow = True))
            #end
        #end

        #>>>Depricated contour plot
        #>>>Depricated contour plot
        annotations = Annotations(annotations)
        self.layout = Layout(title = title, showlegend = False, xaxis = XAxis(showticklabels = False), yaxis = YAxis(title = dep_title), hovermode = 'y', annotations = annotations)
        self.data = Data(data)

        return 
    #end



