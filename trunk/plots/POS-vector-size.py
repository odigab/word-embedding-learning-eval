#!/usr/bin/python
from pylab import *
from natsort import natsorted
import os
import glob
import array
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

#path = '/home/gferraro/Desktop/POS/BROWN/'
x = [250,500,1000,2000,4000]
y = []

files = glob.glob(os.path.join(inputfolder, '*.txt')) 
for filename in natsorted(files):
	if filename.endswith(".txt"):	
		print(filename)
		readFile = open(filename, 'r')
		lines = readFile.readlines()
		readFile.close
		
		# get the last row: all training data	
		# get Fmeasure at column 5th
		row = lines[len(lines)-1]
		p = row.split()
		print p[4]
		y.append(float(p[4]))

	
# convert to numpy array
xv = np.array(x)
yv = np.array(y)

#plt.title('POS Tagging using Brown cluster features ')
plt.xlabel('Vector size')
plt.ylabel('F-measure')

# finally, plot and save the graph:
plt.plot(xv, yv)
savefig(outputfile, bbox_inches='tight')
plt.show()








