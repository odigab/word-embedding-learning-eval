
#!/usr/bin/python
import plotly.plotly as py
from plotly.graph_objs import *
from pylab import *
from natsort import natsorted, ns
import re
import os
import glob
import array
import locale
import fnmatch
import numpy as np
import sys, getopt
import matplotlib.pyplot as plt
# (*) Useful Python/Plotly tools
import plotly.tools as tls   
# (*) Graph objects to piece together plots
from plotly.graph_objs import *
import csv
import operator as op
import requests
import numpy

layout = Layout(    
    font=Font(
        family="Droid Sans, sans-serif",
    ),
    xaxis=XAxis(
        title='Word Embeddings Methods',	# x-axis title	
    ),
    yaxis=YAxis(
	
        title='Training Instances', 		# y-axis title
        autorange='reversed', 			# (!) reverse tick ordering
    ),
)  

# Custom color scales
scl_sns = [
    [0,"#1E9140"],   # color of minimun level (from 'zmin') dark green #1E9140
    [0.25,"#F9E357"], [0.5,"#F9E357"], [0.75, "#F9E357"],  # in-between purple, pink, fuxia light green: BDF7AF, more light green DCF5D5, light pink F7EBE8
    [1, "#8B0000"]   # color of maximum level (from 'zmax') dark red 
]

# Note that Im skipping columns 2 and 3, where CW results are, since we drop them for the conll 2015 submission
pos = numpy.genfromtxt(sys.argv[1],dtype='float',delimiter =',',skip_header=1, skip_footer=0,usemask=True, usecols=(0 1, 4, 5, 6, 7, 8, 9))
chu = numpy.genfromtxt(sys.argv[2],dtype='float',delimiter =',',skip_header=1, skip_footer=0,usemask=True, usecols=(0 1, 4, 5, 6, 7, 8, 9))
ner = numpy.genfromtxt(sys.argv[3],dtype='float',delimiter =',',skip_header=1, skip_footer=0,usemask=True, usecols=(0 1, 4, 5, 6, 7, 8, 9))
mwe = numpy.genfromtxt(sys.argv[4],dtype='float',delimiter =',',skip_header=1, skip_footer=0,usemask=True, usecols=(0 1, 4, 5, 6, 7, 8, 9))

table = []
for x,y,m,n in zip(pos,chu,ner,mwe):
	table.append(x)
	table.append(y)
	table.append(m)				
	table.append(n)		
	
print table

matrix= Data([
	Heatmap(	
#		dy = 2,	
		z = table,
#		x = ['unigram','brown','cw+noup','cw+up','cbow+negs+noup','cbow+negsam+up','skip+negsam+noup','skip+negsam+up','glove+noup','glove+up'],
		x = ['unigram','brown','cbow+negs+noup','cbow+negsam+up','skip+negsam+noup','skip+negsam+up','glove+noup','glove+up'],
		# y = [38,113,262,561,1159,2354,4745,9527,19091,38219],
		 colorscale=scl_sns,	# (!) custom color scales list of lists		
		reversescale=True,	# inverse colormap order
		ytype = 'scaled',
		line=Line(
		        smoothing=4,    # (!) contour smmothing, default is 1
			color='#999999',  # light grey contour lines, default is black
		        width=4           # default is 0.5 
    		),
		
 	)
])
    

# Make figure object
figpos = Figure(data=matrix, layout=layout)
py.image.save_as(figpos, sys.argv[5])

print 'Done!'
























