
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

empy = ""

pos = Data([
	Heatmap(
		# best 
		z = [[float(0.9432),float(0.9419),float(0.9236),float(0.9537),float(0.9516),float(0.9577),float(0.9543),float(0.9592),float(0.9379),float(0.9563)],[float(0.9413),float(0.9417),float(0.9208),float(0.95),float(0.9494),float(0.9541),float(0.9521),float(0.956),float(0.9357),float(0.9526)],[float(0.9382),float(0.941),float(0.9173),float(0.9458),float(0.9468),float(0.9498),float(0.9489),float(0.952),float(0.9321),float(0.9474)],[float(0.933),float(0.9405),float(0.9129),float(0.9404),float(0.9439),float(0.9444),float(0.9465),float(0.9486),float(0.9266),float(0.9435)]
,[float(0.9215),float(0.9391),float(0.9048),float(0.9341),float(0.938),float(0.9392),float(0.9403),float(0.9437),float(0.9178),float(0.9366)],[float(0.9039),float(0.9346),float(0.8933),float(0.9243),float(0.9293),float(0.9303),float(0.9321),float(0.9344),float(0.9059),float(0.9253)],[float(0.8721),float(0.9249),float(0.8755),float(0.9076),float(0.9162),float(0.9159),float(0.9185),float(0.921),float(0.8869),float(0.9071)],[float(0.8208),float(0.9019),float(0.8468),float(0.8818),float(0.8896),float(0.8877),float(0.8921),float(0.8953),float(0.8503),float(0.8737)]
,[float(0.7387),float(0.8527),float(0.8009),float(0.8266),float(0.8446),float(0.8386),float(0.8501),float(0.8482),float(0.793),float(0.8178)],[float(0.6293),float(0.7687),float(0.7267),float(0.742),float(0.7543),float(0.7457),float(0.7547),float(0.7486),float(0.6861),float(0.7172)]],

	#	z = [[float(0.6293),float(0.7687),float(0.7267),float(0.742),float(0.7543),float(0.7457),float(0.7547),float(0.7486),float(0.6861),float(0.7172)],[float(0.7387),float(0.8527),float(0.8009),float(0.8266),float(0.8446),float(0.8386),float(0.8501),float(0.8482),float(0.793),float(0.8178)],[float(0.8208),float(0.9019),float(0.8468),float(0.8818),float(0.8896),float(0.8877),float(0.8921),float(0.8953),float(0.8503),float(0.8737)],[float(0.8721),float(0.9249),float(0.8755),float(0.9076),float(0.9162),float(0.9159),float(0.9185),float(0.921),float(0.8869),float(0.9071)],[float(0.9039),float(0.9346),float(0.8933),float(0.9243),float(0.9293),float(0.9303),float(0.9321),float(0.9344),float(0.9059),float(0.9253)],[float(0.9215),float(0.9391),float(0.9048),float(0.9341),float(0.938),float(0.9392),float(0.9403),float(0.9437),float(0.9178),float(0.9366)],[float(0.933),float(0.9405),float(0.9129),float(0.9404),float(0.9439),float(0.9444),float(0.9465),float(0.9486),float(0.9266),float(0.9435)],[float(0.9382),float(0.941),float(0.9173),float(0.9458),float(0.9468),float(0.9498),float(0.9489),float(0.952),float(0.9321),float(0.9474)],[float(0.9413),float(0.9417),float(0.9208),float(0.95),float(0.9494),float(0.9541),float(0.9521),float(0.956),float(0.9357),float(0.9526)],[float(0.9432),float(0.9419),float(0.9236),float(0.9537),float(0.9516),float(0.9577),float(0.9543),float(0.9592),float(0.9379),float(0.9563)]],
		x = ['unigram','brown','cw+noup','cw+up','cbow+negs+noup','cbow+negsam+up','skip+negsam+noup','skip+negsam+up','glove+noup','glove+up'],#		
		# y = ['[38]','[113]','[262]','[561]','[1159]','[2354]','[4745]','[9527]','[19091]','[38219]'],
		y = ['[38219]','[19091]','[9527]','[4745]','[2354]','[1159]','[561]','[262]','[113]','[38]'],
		zauto=False,		# (!) overwrite Plotly's default color levels
		zmin=0.6293,    	# (!) set value of min color level
		zmax=0.9592,    	# (!) set value of max color level		
		colorscale=scl_sns,	# (!) custom color scales list of lists		
		# colorscale = 'Greys',
		reversescale=True,	# inverse colormap order
		#ytype = 'scaled',
		line=Line(
		        smoothing=1.5,    # (!) contour smmothing, default is 1
			color='#999999',  # light grey contour lines, default is black
		        width=4           # default is 0.5 
    		),
 	)
])
      
chunking = Data([
	Heatmap(
		z = [[float(0.9365),float(0.9386),float(0.935),float(0.9348),float(0.9362),float(0.9319),float(0.9378),float(0.9359),float(0.9347),float(0.933)],[float(0.9281),float(0.9326),float(0.931),float(0.9303),float(0.9292),float(0.9268),float(0.9316),float(0.9326),float(0.9279),float(0.9294)],[float(0.9203),float(0.9253),float(0.9221),float(0.9251),float(0.9221),float(0.9214),float(0.9227),float(0.9269),float(0.9184),float(0.9231)],[float(0.9101),float(0.9139),float(0.913),float(0.9161),float(0.9134),float(0.9151),float(0.9125),float(0.9178),float(0.9077),float(0.9145)]
,[float(0.8951),float(0.8992),float(0.8987),float(0.9015),float(0.9009),float(0.901),float(0.8955),float(0.9024),float(0.8927),float(0.9019)],[float(0.8791),float(0.879),float(0.8818),float(0.885),float(0.8826),float(0.8834),float(0.876),float(0.8818),float(0.8715),float(0.8806)],[float(0.8519),float(0.8492),float(0.8506),float(0.851),float(0.8538),float(0.8518),float(0.8442),float(0.8496),float(0.8392),float(0.8459)],[float(0.8148),float(0.8001),float(0.8065),float(0.8051),float(0.8088),float(0.8061),float(0.7961),float(0.8012),float(0.7961),float(0.7971)],[float(0.764),float(0.7424),float(0.7442),float(0.7376),float(0.744),float(0.7375),float(0.7325),float(0.7317),float(0.7306),float(0.726)],[float(0.6386),float(0.6108),float(0.6123),float(0.6006),float(0.6247),float(0.6247),float(0.5778),float(0.5832),float(0.5963),float(0.5952)]],

#		z=[[float(0.6386),float(0.6108),float(0.6123),float(0.6006),float(0.6247),float(0.6247),float(0.5778),float(0.5832),float(0.5963),float(0.5952)],[float(0.764),float(0.7424),float(0.7442),float(0.7376),float(0.744),float(0.7375),float(0.7325),float(0.7317),float(0.7306),float(0.726)],[float(0.8148),float(0.8001),float(0.8065),float(0.8051),float(0.8088),float(0.8061),float(0.7961),float(0.8012),float(0.7961),float(0.7971)],[float(0.8519),float(0.8492),float(0.8506),float(0.851),float(0.8538),float(0.8518),float(0.8442),float(0.8496),float(0.8392),float(0.8459)],[float(0.8791),float(0.879),float(0.8818),float(0.885),float(0.8826),float(0.8834),float(0.876),float(0.8818),float(0.8715),float(0.8806)],[float(0.8951),float(0.8992),float(0.8987),float(0.9015),float(0.9009),float(0.901),float(0.8955),float(0.9024),float(0.8927),float(0.9019)],[float(0.9101),float(0.9139),float(0.913),float(0.9161),float(0.9134),float(0.9151),float(0.9125),float(0.9178),float(0.9077),float(0.9145)],[float(0.9203),float(0.9253),float(0.9221),float(0.9251),float(0.9221),float(0.9214),float(0.9227),float(0.9269),float(0.9184),float(0.9231)],[float(0.9281),float(0.9326),float(0.931),float(0.9303),float(0.9292),float(0.9268),float(0.9316),float(0.9326),float(0.9279),float(0.9294)],[float(0.9365),float(0.9386),float(0.935),float(0.9348),float(0.9362),float(0.9319),float(0.9378),float(0.9359),float(0.9347),float(0.933)]],
		x = ['unigram','brown','cw+noup','cw+up','cbow+negs+noup','cbow+negsam+up','skip+negsam+noup','skip+negsam+up','glove+noup','glove+up'],
		# y = ['[10]','[29]','[68]','[145]','[298]','[606]','[1221]','[2451]','[4910]','[9829]'],
		y = ['[9829]','[4910]','[2451]','[1221]','[606]','[298]','[145]','[68]','[29]','[10]'],
		zauto=False, 		# (!) overwrite Plotly's default color levels
		zmin=0.5778,    	# (!) set value of min color level
		zmax=0.9378,    	# (!) set value of max color level
		 colorscale=scl_sns,	# (!) custom color scales list of lists
		# colorscale = 'Greys',	
		reversescale=True,	# inverse colormap order
		ytype = 'scaled'
 	)
])
      
ner = Data([
	Heatmap(



		z=[[float(0.8276),float(0.8663),float(0.8306),float(0.832),float(0.8547),float(0.8573),float(0.8686),float(0.8603),float(0.8565),float(0.8631)],[float(0.8084),float(0.854),float(0.8224),float(0.819),float(0.8333),float(0.841),float(0.851),float(0.8481),float(0.8359),float(0.8462)],[float(0.7804),float(0.8369),float(0.8059),float(0.8013),float(0.8174),float(0.8192),float(0.8333),float(0.8237),float(0.8059),float(0.8121)],[float(0.7271),float(0.8068),float(0.7666),float(0.7691),float(0.7736),float(0.7786),float(0.8013),float(0.7954),float(0.7622),float(0.7722)],[float(0.6526),float(0.7557),float(0.6949),float(0.6848),float(0.7104),float(0.7033),float(0.7396),float(0.7198),float(0.6842),float(0.6813)],[float(0.5457),float(0.6983),float(0.606),float(0.58),float(0.6311),float(0.6214),float(0.6752),float(0.6037),float(0.5764),float(0.5694)],[float(0.3469),float(0.5553),float(0.45),float(0.3909),float(0.4886),float(0.4751),float(0.4993),float(0.3852),float(0.3924),float(0.3749)],[float(0.1332),float(0.3023),float(0.2318),float(0.1159),float(0.3003),float(0.2955),float(0.2184),float(0.0774),float(0.1508),float(0.1144)],[float(0.0618),float(0.1441),float(0.1725),float(0.0529),float(0.1378),float(0.13),float(0.0972),float(0.0256),float(0.0702),float(0.0629)],[float(0.0873),float(0.1345),float(0.1933),float(0.0524),float(0.0917),float(0.1424),float(0.0339),float(0.0173),float(0.0543),float(0.0707)]],
		# z=[[float(0.0873),float(0.1345),float(0.1933),float(0.0524),float(0.0917),float(0.1424),float(0.0339),float(0.0173),float(0.0543),float(0.0707)], [float(0.0618),float(0.1441),float(0.1725),float(0.0529),float(0.1378),float(0.13),float(0.0972),float(0.0256),float(0.0702),float(0.0629)],[float(0.1332),float(0.3023),float(0.2318),float(0.1159),float(0.3003),float(0.2955),float(0.2184),float(0.0774),float(0.1508),float(0.1144)],[float(0.3469),float(0.5553),float(0.45),float(0.3909),float(0.4886),float(0.4751),float(0.4993),float(0.3852),float(0.3924),float(0.3749)],[float(0.5457),float(0.6983),float(0.606),float(0.58),float(0.6311),float(0.6214),float(0.6752),float(0.6037),float(0.5764),float(0.5694)],[float(0.6526),float(0.7557),float(0.6949),float(0.6848),float(0.7104),float(0.7033),float(0.7396),float(0.7198),float(0.6842),float(0.6813)],[float(0.7271),float(0.8068),float(0.7666),float(0.7691),float(0.7736),float(0.7786),float(0.8013),float(0.7954),float(0.7622),float(0.7722)],[float(0.7804),float(0.8369),float(0.8059),float(0.8013),float(0.8174),float(0.8192),float(0.8333),float(0.8237),float(0.8059),float(0.8121)],[float(0.8084),float(0.854),float(0.8224),float(0.819),float(0.8333),float(0.841),float(0.851),float(0.8481),float(0.8359),float(0.8462)],[float(0.8276),float(0.8663),float(0.8306),float(0.832),float(0.8547),float(0.8573),float(0.8686),float(0.8603),float(0.8565),float(0.8631)]],
		x = ['unigram','brown','cw+noup','cw+up','cbow+negs+noup','cbow+negsam+up','skip+negsam+noup','skip+negsam+up','glove+noup','glove+up'],
		# y = ['[15]','[44]','[103]','[220]','[455]','[923]','[1861]','[3736]','[7487]','[14987]'],
		y = ['[14987]','[7487]','[3736]','[1861]','[923]','[455]','[220]','[103]','[44]','[15]'],
		zauto=False, 		# (!) overwrite Plotly's default color levels
		zmin=0.0173,    	# (!) set value of min color level
		zmax=0.8686,    	# (!) set value of max color level
		colorscale=scl_sns,	# (!) custom color scales list of lists		
		# colorscale = 'Greys',
		reversescale=True,	# inverse colormap order
		ytype = 'scaled'
 	)
])


mwe = Data([
	Heatmap(
		z = [[float(0.6384),float(0.6409),float(0.6077),float(0.6153),float(0.6546),float(0.6459),float(0.645),float(0.6067),float(0.6363),float(0.6434),float(0.619)],[float(0.5695),float(0.6025),float(0.5578),float(0.5602),float(0.5709),float(0.5965),float(0.5845),float(0.5437),float(0.5768),float(0.5836),float(0.5684)],[float(0.4785),float(0.5601),float(0.4929),float(0.493),float(0.493),float(0.5027),float(0.5011),float(0.4762),float(0.4959),float(0.4994),float(0.4955)],[float(0.4054),float(0.4733),float(0.4658),float(0.439),float(0.4424),float(0.3985),float(0.4287),float(0.4358),float(0.3975),float(0.4312),float(0.4363)],[float(0.2933),float(0.311),float(0.3036),float(0.3173),float(0.3204),float(0.2921),float(0.2926),float(0.2926),float(0.2644),float(0.3156),float(0.3234)],[float(0.1412),float(0.1494),float(0.1785),float(0.2121),float(0.192),float(0.1752),float(0.173),float(0.1723),float(0.1743),float(0.2021),float(0.2245)],[float(0.1354),float(0.1241),float(0.1623),float(0.1782),float(0.1825),float(0.1437),float(0.1573),float(0.1314),float(0.1544),float(0.1751),float(0.1782)],[float(0.0505),float(0.0375),float(0.054),float(0.0564),float(0.0603),float(0.0505),float(0.0373),float(0.0374),float(0.0507),float(0.0374),float(0.0599)],[float(0.0306),float(0.024),float(0.0239),float(0.0103),float(0.0172),float(0.0205),float(0.0206),float(0.0137),float(0.0206),float(0.0138),float(0.0068)],[float(0.0241),float(0.0255),float(0.0232),float(0.0146),float(0.0082),float(0.0122),float(0.0138),float(0.0084),float(0),float(0.0034),float(0.0111)]],

#		z=[[float(0.0241),float(0.0255),float(0.0232),float(0.0146),float(0.0082),float(0.0122),float(0.0138),float(0.0084),float(0),float(0.0034),float(0.0111)],[float(0.0306),float(0.024),float(0.0239),float(0.0103),float(0.0172),float(0.0205),float(0.0206),float(0.0137),float(0.0206),float(0.0138),float(0.0068)],[float(0.0505),float(0.0375),float(0.054),float(0.0564),float(0.0603),float(0.0505),float(0.0373),float(0.0374),float(0.0507),float(0.0374),float(0.0599)],[float(0.1354),float(0.1241),float(0.1623),float(0.1782),float(0.1825),float(0.1437),float(0.1573),float(0.1314),float(0.1544),float(0.1751),float(0.1782)],[float(0.1412),float(0.1494),float(0.1785),float(0.2121),float(0.192),float(0.1752),float(0.173),float(0.1723),float(0.1743),float(0.2021),float(0.2245)],[float(0.2933),float(0.311),float(0.3036),float(0.3173),float(0.3204),float(0.2921),float(0.2926),float(0.2926),float(0.2644),float(0.3156),float(0.3234)],[float(0.4054),float(0.4733),float(0.4658),float(0.439),float(0.4424),float(0.3985),float(0.4287),float(0.4358),float(0.3975),float(0.4312),float(0.4363)],[float(0.4785),float(0.5601),float(0.4929),float(0.493),float(0.493),float(0.5027),float(0.5011),float(0.4762),float(0.4959),float(0.4994),float(0.4955)],[float(0.5695),float(0.6025),float(0.5578),float(0.5602),float(0.5709),float(0.5965),float(0.5845),float(0.5437),float(0.5768),float(0.5836),float(0.5684)],[float(0.6384),float(0.6409),float(0.6077),float(0.6153),float(0.6546),float(0.6459),float(0.645),float(0.6067),float(0.6363),float(0.6434),float(0.619)]],
		x = ['unigram','brown','cw+noup','cw+up','cbow+negs+noup','cbow+negsam+up','skip+negsam+noup','skip+negsam+up','glove+noup','glove+up'],
		# y = ['[4]','[10]','[23]','[49]','[101]','[204]','[412]','[826]','[1655]','[3312]'],
		y = ['[3312]','[1655]','[826]','[412]','[204]','[101]','[49]','[23]','[10]','[4]'], 
		zauto=False, 		# (!) overwrite Plotly's default color levels
		zmin=0,    	# (!) set value of min color level
		zmax=0.6546,    	# (!) set value of max color level
		colorscale=scl_sns,	# (!) custom color scales list of lists		
		# colorscale = 'Greys',
		reversescale=True,	# inverse colormap order
		ytype = 'scaled'
 	)
])

# Make figure object
figpos = Figure(data=pos, layout=layout)
figchunk = Figure(data=chunking, layout=layout)
figner = Figure(data=ner, layout=layout)
figmwe = Figure(data=mwe, layout=layout)

#plot_url = py.plot(figpos, filename='pos-heatmap')
#plot_url = py.plot(figchunk, filename='chunking-heatmap')
#plot_url = py.plot(figner, filename='ner-heatmap')
#plot_url = py.plot(figmwe, filename='mwe-heatmap')

py.image.save_as(figpos, 'map-pos-color-invert.pdf')
py.image.save_as(figchunk, 'map-chunk-color-invert.pdf')
py.image.save_as(figner, 'map-ner-color-invert.pdf')
py.image.save_as(figmwe, 'map-mwe-color-invert.pdf')

print 'Done!'


























