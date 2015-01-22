import os
import time
import numpy as np
﻿from numpy import *
import matplotlib.pyplot as plt


path = '/some/path/to/file'

for filename in glob.glob(os.path.join(path, '*.txt')):

	readFile = open(filename, 'r')
	lines = readFile.readlines()
	readFile.close

	x1 = []
	y1 = []
	m1 = []
	n1 = []

	size = len(lines) 	
	print size

	# get Fmeasure
	row = lines[size]
	print lines[size]

	p = row.split()
	y1.append(float(p[4]))

	for line in lines:		
		p = line.split()
		x1.append(float(p[0]))
		y1.append(float(p[1]))
		m1.append(float(p[2]))	
		n1.append(float(p[3]))		

	plt.gca().set_color_cycle(['red', 'green', 'blue'])

	# convert to numpy array
	xv = np.array(x1)
	yv = np.array(y1)
	mv = np.array(m1)
	nv = np.array(n1)

	plt.title('this is a title')
	plt.xlabel('Training size')
	plt.ylabel('y label')

	# now, plot the data:
	plt.plot(xv, yv)
	plt.plot(xv, mv)
	plt.plot(xv, nv)

	plt.legend(['F1Measure', 'Precision', 'Recall'], loc='lower right')

	plt.show()







