#!/usr/bin/python
from pylab import *
from natsort import natsorted
import re
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
		print 'XX.py -i <inputfolder> -o <outputfile>'
		sys.exit()
	elif opt in ("-i", "--ifolder"):
		inputfolder = arg
	elif opt in ("-o", "--ofile"):
        	outputfile = arg
#	elif opt in ("-t", "--otitle"):
#        	title = arg

print 'Input folder is:', inputfolder
print 'Output file is:', outputfile
#print 'Graph title:', title

x = []
y = []
xv = []
yv = []
label = ''
marker = ''
color = 'r'
linestyle = '-'
noupMarker = 's'
walk_dir = inputfolder
legParams = {'legend.fontsize': 10,
          'legend.linewidth': 0.4}

alist_filter = ['brown_cluster_v4000_best.txt', 
#	'cbow_negsam_noupdated_best.txt', 
	'cbow_updated_best.txt', 
	'cbow_noupdated_best.txt', 
	'cw_noupdated_best.txt', 
	'cw_updated_best.txt', 
	'unigram_best.txt', 
	'glove_noupdated_best.txt', 
#	'glove_updated_incretuneparam.txt',
	'glove_updated_best.txt',  
#	'skip_gram_negsam_noupdated_best.txt', 
#	'skip_gram_negsam_updated_incretuneparam.txt']
	'skipgram_noupdated_best.txt', 
	'skipgram_updated_best.txt']


# Walk into directories in filesystem
# Ripped from os module and slightly modified
# for alphabetical sorting
#
def sortedWalk(top, topdown=True, onerror=None):
    from os.path import join, isdir, islink
 
    names = os.listdir(top)
    names.sort()
    dirs, nondirs = [], []
 
    for name in names:
        if isdir(os.path.join(top, name)):
            dirs.append(name)
        else:
            nondirs.append(name)
 
    if topdown:
        yield top, dirs, nondirs
    for name in dirs:
        path = join(top, name)
        if not os.path.islink(path):
            for x in sortedWalk(path, topdown, onerror):
                yield x
    if not topdown:
        yield top, dirs, nondirs

for root, subdirs, files in sortedWalk(walk_dir):
	#print('--\nroot = ' + root)
	for subdir in sorted(subdirs):
		print('\t- subdirectory ' + subdir)		
	for filename in files:  		  		
		if filename in alist_filter:
			if re.match("unigram_best.txt", filename): 
				color='r'
				label = "unigram" 
			if re.match("glove_noupdated_best.txt", filename):
				color='b'
				marker = noupMarker
				label = "glove_noup"
			if re.match("glove_updated_best.txt", filename):					
				color='b'
				label = "glove_up"
			elif re.match("cbow_noupdated_best.txt", filename):
				color='g'
				marker = noupMarker
				label = "cbow_noup"
			elif re.match("cbow_updated_best.txt", filename): 
				color='g'
				label = "cbow_up"
			elif re.match("skipgram_noupdated_best.txt", filename):
				color='y'
				marker = noupMarker
				label = "skip_gram_negsam_noup"
			elif re.match("skipgram_updated_best.txt", filename): 
				color='y'
				label = "skip_gram_negsam_up"
			elif re.match("cw_updated_best.txt", filename): 
				color='k'
				label =  "cw_up"
			elif re.match("cw_noupdated_best.txt", filename):
				color='k'
				marker = noupMarker
				label = "cw_noup"
			elif re.match("brown_cluster_v4000_best.txt", filename): 
				color='m'
				label = "brown_cluster"
			filePath = os.path.join(root, filename)
			print('\t- file %s (full path: %s)' % (filename, filePath))
			with open(filePath, 'rb') as f:
			        lines = f.readlines()
				f.close	
				# check the column title
				titleLine = lines[0]
				t = titleLine.split()				
				print('column title:', t[23])		# out-of-vocabulary_Accuracy
				# skip the first row with the titles
				for line in lines[1:]: 
					p = line.split()	
					x.append(float(p[0]))				
					y.append(float(p[23]))				
				# convert to numpy array
				print('x ', x)						
				print('y ', y)			
				xv = np.array(x)
				yv = np.array(y)
				plt.plot(xv, yv, label = label, linestyle=linestyle, marker=marker, color=color)	
				x = []
				y = []
				xv = []
				yv = []
				label = ''	
				marker = ''

plt.title('Out of vocabulary words')
plt.xlabel('Training size')
plt.ylabel('Accuracy')

plt.legend(loc='best')
savefig(outputfile, bbox_inches='tight')
#plt.show()




