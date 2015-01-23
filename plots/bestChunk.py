#!/usr/bin/python
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

try:
	from pathlib import PurePath # PurePath is the base object for Paths.
except ImportError:
	PurePath = object # To avoid NameErrors.
	has_pathlib = False
else:
	has_pathlib = True

try:
	opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["ifolder=","ofile=", "title="])
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
label = ''
marker = ''
linestyle = '-'
noupMarker = 's'
legParams = {'legend.fontsize': 10,
          'legend.linewidth': 0.4}

alist_filter = ['brown_cluster_v4000_best.txt', 
	'cbow_negsam_noupdated_best.txt', 
	'cbow_negsam_updated_incretuneparam.txt', 
	'cw_noupdated_best.txt', 
	'cw_updated_incretuneparam.txt', 
	'unigram_best.txt', 
	'glove_noupdated_best.txt', 
	'glove_updated_incretuneparam.txt', 
	'skip_gram_negsam_noupdated_best.txt', 
	'skip_gram_negsam_updated_incretuneparam.txt']

walk_dir = inputfolder

for root, subdirs, files in os.walk(walk_dir):
	#print('--\nroot = ' + root)
	for subdir in subdirs:
		print('\t- subdirectory ' + subdir)	
	
	sortfiles = natsorted(files, alg=ns.LOCALE)	
	for filename in sortfiles:  		
		if filename in alist_filter:
			if re.match("unigram_best.txt", filename): "unigram" 
			if re.match("glove_noupdated_best.txt", filename):
				marker = noupMarker
				label = "glove_noup"
			if re.match("glove_updated_incretuneparam.txt", filename):					
				label = "glove_up"
			elif re.match("cbow_negsam_noupdated_best.txt", filename):
				marker = noupMarker
				label = "cbow_negsam_noup"
			elif re.match("cbow_negsam_updated_incretuneparam.txt", filename): label = "cbow_negsam_up"
			elif re.match("skip_gram_negsam_noupdated_best.txt", filename):
				marker = noupMarker
				label = "skip_gram_negsam_noup"
			elif re.match("skip_gram_negsam_updated_incretuneparam.txt", filename): label = "skip_gram_negsam_up"
			elif re.match("cw_updated_incretuneparam.txt", filename): label =  "cw_up"
			elif re.match("cw_noupdated_best.txt", filename):
				marker = noupMarker
				label = "cw_noup"
			elif re.match("brown_cluster_v4000_best.txt", filename): label = "brown_cluster"
	
			filePath = os.path.join(root, filename)
			print('\t- file %s (full path: %s)' % (filename, filePath))
			with open(filePath, 'rb') as f:
			        lines = f.readlines()
				f.close			
				# check the column title
				titleLine = lines[0]
				t = titleLine.split()				
				print('column title', t[32] )
				# skip the first row with the titles
				for line in lines[1:]: 
					p = line.split()	
					x.append(float(p[0]))				
					y.append(float(p[32]))   # AG
				# convert to numpy array
				print('x ', x)						
				print('y ', y)			
				xv = np.array(x)
				yv = np.array(y)
				plt.plot(xv, yv, label=label, linestyle=linestyle, marker=marker)	
				x = []
				y = []
				xv = []
				yv = []
				label = ''
				marker = ''

plt.xlabel('Training size')
plt.ylabel('F1-Measure')

plt.rcParams.update(legParams)
plt.legend(loc='lower right')
savefig(outputfile, bbox_inches='tight')
#plt.show()




