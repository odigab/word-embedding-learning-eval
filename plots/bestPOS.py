#!/usr/bin/python
from pylab import *
from natsort import natsorted
import os
import re
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
	for filename in natsorted(files):  		
		if filename in alist_filter: 
			if re.match("unigram_best.txt", filename):
				label = filename.replace("unigram_best.txt", "unigram")
			if re.match("glove_noupdated_best.txt", filename):
				marker = noupMarker
				label = filename.replace("glove_noupdated_best.txt", "glove_noup")
			if re.match("glove_updated_incretuneparam.txt", filename):					
				label = filename.replace("glove_updated_incretuneparam.txt", "glove_up")
			elif re.match("cbow_negsam_noupdated_best.txt", filename):
				marker = noupMarker
				label = filename.replace("cbow_negsam_noupdated_best.txt", "cbow_negsam_noup")
			elif re.match("cbow_negsam_updated_incretuneparam.txt", filename):
				label = filename.replace("cbow_negsam_updated_incretuneparam.txt", "cbow_negsam_up") 
			elif re.match("skip_gram_negsam_noupdated_best.txt", filename):
				marker = noupMarker
				label = filename.replace("skip_gram_negsam_noupdated_best.txt", "skip_gram_negsam_noup")
			elif re.match("skip_gram_negsam_updated_incretuneparam.txt", filename):
				label = filename.replace("skip_gram_negsam_updated_incretuneparam.txt", "skip_gram_negsam_up")
			elif re.match("cw_updated_incretuneparam.txt", filename):
				marker = noupMarker
				label = filename.replace("cw_updated_incretuneparam.txt", "cw_up")
			elif re.match("cw_noupdated_best.txt", filename):
				marker = noupMarker
				label = filename.replace("cw_noupdated_best.txt", "cw_noup")		
			elif re.match("brown_cluster_v4000_best.txt", filename):
				label = filename.replace("brown_cluster_v4000_best.txt", "brown_cluster")				
			filePath = os.path.join(root, filename)
			print('\t- file %s (full path: %s)' % (filename, filePath))
			with open(filePath, 'rb') as f:
			        lines = f.readlines()
				f.close	
				# check the column title
				titleLine = lines[0]
				t = titleLine.split()				
				print('column title', t[25] )		
				# skip the first row with the titles
				for line in lines[1:]: 
					p = line.split()	
					x.append(float(p[0]))				
					y.append(float(p[25]))
				# convert to numpy array
				#print('x ', x)						
				#print('y ', y)			
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
plt.ylabel('Accuracy')

plt.rcParams.update(legParams)
plt.legend(loc='lower right')
savefig(outputfile, bbox_inches='tight')
#plt.show()




