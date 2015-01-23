#!/usr/bin/python
from pylab import *
import re
import os
import glob
import array
import fnmatch
import natsort
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


def returnold(folder):
    matches = []
    for root, dirnames, filenames in os.walk(folder):
        for filename in fnmatch.filter(filenames, '*.*'):
            matches.append(os.path.join(root, filename))
    return min(matches, key=os.path.getmtime)

files = sortedWalk(inputfolder)



for root, subdirs, files in os.walk(walk_dir):
	#print('--\nroot = ' + root)
	for subdir in sorted(subdirs):
		print('\t- subdirectory ' + subdir)			
	sortfiles = sorted(files)  
	for filename in files:  
		if filename in alist_filter: 
			if re.match("unigram_best.txt", filename): label = "unigram"
			elif re.match("glove_noupdated_best.txt", filename): 
				marker = noupMarker
				label = "glove_noup"
			elif re.match("glove_updated_incretuneparam.txt", filename): label = "glove_up"
			elif re.match("cbow_negsam_noupdated_best.txt", filename):
				marker = noupMarker
				label = "cbow_negsam_noup"
			elif re.match("cbow_negsam_updated_incretuneparam.txt", filename): label = "cbow_negsam_up"
			elif re.match("skip_gram_negsam_noupdated_best.txt", filename):
				marker = noupMarker
				label = "skip_gram_negsam_noup"
			elif re.match("skip_gram_negsam_updated_incretuneparam.txt", filename): label = "skip_gram_negsam_up"
			elif re.match("cw_updated_incretuneparam.txt", filename): label = "cw_up"
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
				print('column title:', t[2])		# IN DOMAIN CONLL_out-of-vocabulary_Accuracy
				print('column title 2:', t[29])		# OUT OF DOMAIN MUC_out-of-vocabulary_Accuracy
				# skip the first row with the titles
				for line in lines[1:]: 
					p = line.split()	
					x.append(float(p[0]))				
					y.append(float(p[2]))
				# convert to numpy array
				print('x ', x)						
				print('y ', y)			
#				print('z', z) 
				xv = np.array(x)
				yv = np.array(y)
#				zv = np.array(z)
				plt.plot(xv, yv, label = label + '_' + t[2].replace('_out-of-vocabulary_Accuracy', ''), linestyle=linestyle, 	marker=marker)	
	#				plt.plot(xv, zv, label = label + '_' + t[29].replace('_out-of-vocabulary_Accuracy', ''))		
				x = []
				y = []
				z = []
				xv = []
				yv = []
				zv = []
				label = ''
				marker = ''
		
plt.xlabel('Training size')
plt.ylabel('F1-Measure')

plt.rcParams.update(legParams)
plt.legend(loc='lower right')
savefig(outputfile, bbox_inches='tight')
#plt.show()




