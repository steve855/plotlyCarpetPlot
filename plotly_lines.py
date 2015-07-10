#!/usr/local/bin/python
"""

	plotly_lines.py 

Generates horixontal and vertical named lines for plots 

Copyright (c) 2015 by Stephen Andrews
All rights reserved.
Revision: 1.0 - $Date: 10-06-2015$


Developers:
-----------
- Stephen Andrews (SA) 

History
-------
    v. 1.0  - 
"""

__version__ = '$Revision: $'

"""
To Do:
    - allow the lines to be removed from the hoverinfo
    - automatically get the x range from the layout's x axis
"""

# =============================================================================
# Standard Python modules
# =============================================================================
import os, sys
import unittest
# =============================================================================
# External Python modules
# =============================================================================
import numpy

# =============================================================================
# Extension modules
# =============================================================================
import plotly.plotly as py
from plotly.graph_objs import *

# =============================================================================
# 
# =============================================================================

class AxHline():
	'''

	Draws a horizontal line at a given y value spanning a given x, annotated with text

	'''
	def __init__(self, y, x_data, text = None, textposition = 'top', *args, **kwargs):
		'''

		*Arguments*

		- y -> FLOAT: The constant 'y' value for the horiztonal line.
		- x_d -> FLOAT: The range of x data the line should span.

		*Keyword Arguments*

		- text -> STR: The text to place on the line. *Default None*
		- textposition -> STR: where to locate the text either 'top' or 'bottom'. *Default 'top'*

		'''

		if text == None:
			mode = 'lines'
			text = None
		else:
			mode = 'lines+text'
			text = ['', text, '']
		#end

		if not textposition.lower() in ['top', 'bottom']:
			raise IOError("textposition must be either 'top' or 'bottom'")
		else:
			textposition = textposition.lower()+' center'
		#end

		x = [min(x_data), 0.5 *(min(x_data) + max(x_data)) , max(x_data)]
		y = [y]*3
		line_dict = Scatter(x = x, y = y, mode = mode, text = text, textposition = textposition, showlegend = False) 
		line_dict.update(kwargs)

		self.data = line_dict

		return

class AxVline():
	'''

	Draws a vertical line at a given x value spanning a given y, annotated with text

	'''
	def __init__(self, x, y_data, text = None, textposition = 'right', *args, **kwargs):
		'''

		*Arguments*

		- x -> FLOAT: The constant 'x' value for the horiztonal line.
		- y_data -> FLOAT: The range of y data the line should span.

		*Keyword Arguments*

		- text -> STR: The text to place on the line. *Default None*
		- textposition -> STR: where to locate the text either 'top' or 'bottom'. *Default 'top'*

		'''

		if text == None:
			mode = 'lines'
			text = None
		else:
			mode = 'lines+text'
			text = ['', text, '']
		#end

		if not textposition.lower() in ['left', 'right']:
			raise IOError("textposition must be either 'left' or 'right'")
		else:
			textposition='middle ' + textposition.lower()
		#end

		y = [min(y_data), 0.5 *(min(y_data) + max(y_data)) , max(y_data)]
		x = [x]*3
		line_dict = Scatter(x = x, y = y, mode = mode, text = text, textposition = textposition, showlegend = False) 
		line_dict.update(kwargs)

		self.data = line_dict

		return
# class AxHline():

      # "    pl_data.append(Scatter(x = numpy.array([TOWs.min(),TOWs.mean(),TOWs.max()])/1E3,\n",
      # "                   y = numpy.array([FL]*3)/1E3,\n",
      # "                   mode = 'lines+text',\n",
      # "                   text = ['', label, ''],\n",
      # "                   textposition = 'top center',\n",
      # "                   line = Line(color = 'grey', dash = 'solid'),\n",
      # "                   showlegend = False\n",
      # "                   ))\n",

class Test_AxHline(unittest.TestCase):

	def setUp(self):
		self.xx = numpy.linspace(0,10)
		self.yy1 = 5 + 3*self.xx + self.xx**2
		self.yy2 = 3 - 4*self.xx  +2*self.xx**2

		data = []
		data.append(Scatter(x = self.xx, y = self.yy1))
		data.append(Scatter(x = self.xx, y = self.yy2))

		self.data = data 

	# @unittest.skip('skipped')	
	def test_basic_hline(self):
		self.data.append(AxHline(50, self.xx).data)

		data = Data(self.data)
		figure = Figure(data = data)

		py.plot(figure, filename = 'carpet_plot/axhline_test_1', overwrite = True)
	# @unittest.skip('skipped')
	def test_basic_hline_with_text(self):
		self.data.append(AxHline(50, self.xx, text = "Sample line").data)

		data = Data(self.data)
		figure = Figure(data = data)

		py.plot(figure, filename = 'carpet_plot/axhline_test_2', overwrite = True)
	# @unittest.skip('skipped')
	def test_hline_with_new_linestyle(self):
		self.data.append(AxHline(50, self.xx, text = "Sample line", line = Line(color = 'grey', dash = 'dashed')).data)

		data = Data(self.data)
		figure = Figure(data = data)

		py.plot(figure, filename = 'carpet_plot/axhline_test_3', overwrite = True)

	# @unittest.skip('skipped')
	def test_basic_vline(self):
		self.data.append(AxVline(5, self.yy2).data)

		data = Data(self.data)
		figure = Figure(data = data)

		py.plot(figure, filename = 'carpet_plot/axvline_test_1', overwrite = True)

	# @unittest.skip('skipped')
	def test_vline_text(self):
		self.data.append(AxVline(5, self.yy2, text = 'vertical label').data)

		data = Data(self.data)
		figure = Figure(data = data)

		py.plot(figure, filename = 'carpet_plot/axvline_test_2', overwrite = True)

	def test_combined_lines(self):
		self.data.append(AxHline(25, self.xx, text = 'lower bound on y').data)
		self.data.append(AxHline(75, self.xx, text = 'upper bound on y').data)
		self.data.append(AxVline(1.5, self.yy2, text = 'lower bound on x').data)
		self.data.append(AxVline(6.5, self.yy2, text = 'upper bound on x').data)

		data = Data(self.data)
		figure = Figure(data = data)

		py.plot(figure, filename = 'carpet_plot/combined_test_1', overwrite = True)
if __name__ == '__main__':
	unittest.main()
