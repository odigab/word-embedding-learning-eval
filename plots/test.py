#!/usr/bin/python
from natsort import natsorted
import os
import glob
import array
import numpy as np
import matplotlib.pyplot as plt


path = '/home/gferraro/Desktop/POS/BROWN/'

x = [250,500,1000,2000,4000]
y = []

files = glob.glob(os.path.join(path, '*.txt')) 
for filename in natsorted(files):
	if filename.endswith(".txt"):	
		print(filename)
		readFile = open(filename, 'r')
		lines = readFile.readlines()
		readFile.close
			
		size = len(lines)
		
		# get Fmeasure
		row = lines[size-1]
		p = row.split()
		print p[4]
		y.append(float(p[4]))



	
#plt.gca().set_color_cycle(['red', 'green', 'blue'])
num_plots = 9
colormap = plt.cm.gist_ncar
plt.gca().set_color_cycle([colormap(i) for i in np.linspace(0, 0.9, num_plots)])

# convert to numpy array
xv = np.array(x)
yv = np.array(y)

plt.title('POS Tagging using Brown cluster features ')
plt.xlabel('Vector size')
plt.ylabel('F-measure')

# now, plot the data:
plt.plot(xv, yv)
plt.show()







