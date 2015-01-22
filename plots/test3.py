#!/usr/bin/python
from pylab import *
from natsort import natsorted
import os
import glob
import array
import fnmatch
import numpy as np
import sys, getopt
import matplotlib.pyplot as plt

try:
	opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["ifolder=","ofile="])
except getopt.GetoptError:
	print 'script.py -i <inputfolder> -o <outputfile>'
	sys.exit(2)
for opt, arg in opts:
	if opt == '-h':
		print 'test.py -i <inputfolder> -o <outputfile>'
		sys.exit()
	elif opt in ("-i", "--ifolder"):
		inputfolder = arg
	elif opt in ("-o", "--ofile"):
        	outputfile = arg
print 'Input folder is "', inputfolder
print 'Output file is "', outputfile

# POS best results from all methods, varying training size
 
x = []
y = []
xv = []
yv = []

alist_filter = ['brown_cluster_v4000_best.txt', 'd_best.txt']
ignore_list = ['*.ser']

walk_dir = inputfolder
for root, subdirs, files in os.walk(walk_dir):
	#print('--\nroot = ' + root)
	for subdir in subdirs:
		print('\t- subdirectory ' + subdir)			
	for filename in files:  		
		if filename in alist_filter or filename[-10:] in alist_filter:
			label = filename.replace("_best.txt", "")		
			filePath = os.path.join(root, filename)
			print('\t- file %s (full path: %s)' % (filename, filePath))
			with open(filePath, 'rb') as f:
			        lines = f.readlines()
				f.close			
				# skip the first row with the titles
				for line in lines[1:]: 
					p = line.split()	
					x.append(float(p[0]))				
					y.append(float(p[25]))
				# convert to numpy array
				print('x ', x)						
				print('y ', y)			
				xv = np.array(x)
				yv = np.array(y)
				plt.plot(xv, yv, label=label)	
				x = []
				y = []
				xv = []
				yv = []
	
plt.title('POS best results from all methods')
plt.xlabel('Training size')
plt.ylabel('Accuracy')

plt.legend(loc='best')
savefig(outputfile, bbox_inches='tight')
#plt.show()




