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
import matplotlib.gridspec as gridspec


x = []
y = []
z = []
xv = []
yv = []
label = ''
marker = ''
color = 'r'
linestyle = '-'
noupMarker = 's'
walkDirPos = sys.argv[1]
walkDirNer = sys.argv[2]
walkDirChu = sys.argv[3]
walkDirMwe = sys.argv[4]

# set the size of the figure that will contained the subplots
fig = plt.figure(figsize=(12,20))

alist_filter = ['brown_cluster_v2000_best.txt', 
	'brown_cluster_v4000_best.txt',
	'cbow_updated_best.txt', 
	'cbow_noupdated_best.txt', 
	'cbow_negsam_noupdated_best.txt', 
	'cbow_negsam_updated_incretuneparam.txt', 
	'cw_updated_best.txt', 
	'cw_noupdated_best.txt', 
	'cw_updated_incretuneparam.txt', 
	'unigram_best.txt', 
	'glove_updated_best.txt',  
	'glove_noupdated_best.txt', 
	'glove_updated_incretuneparam.txt', 
	'skipgram_noupdated_best.txt', 
	'skipgram_updated_best.txt',
	'skip_gram_negsam_noupdated_best.txt', 
	'skip_gram_negsam_updated_incretuneparam.txt']

# Walk into directories in filesystem
# Ripped from os module and slightly modified
# for alphabetical sorting
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

# POS OOV in domain
for root, subdirs, files in sortedWalk(walkDirPos):
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
			if re.match("glove_updated_incretuneparam.txt", filename):					
				color='b'
				label = "glove_up"
			elif re.match("cbow_negsam_noupdated_best.txt", filename):
				color='g'
				marker = noupMarker
				label = "cbow_negsam_noup"
			elif re.match("cbow_negsam_updated_incretuneparam.txt", filename): 
				color='g'
				label = "cbow_negsam_up"
			elif re.match("skip_gram_negsam_noupdated_best.txt", filename):
				color='y'
				marker = noupMarker
				label = "skip_gram_negsam_noup"
			elif re.match("skip_gram_negsam_updated_incretuneparam.txt", filename): 
				color='y'
				label = "skip_gram_negsam_up"
			elif re.match("cw_updated_incretuneparam.txt", filename): 
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
				print('column title 2:', t[274])	# in domain WSJ_out-of-vocabulary_Accuracy
				fig.add_subplot(6, 2, 1)
				fig.subplots_adjust(hspace=1.5)
				# skip the first row with the titles
				for line in lines[1:]: 
					p = line.split()	
					x.append(float(p[0]))				
					z.append(float(p[274]))
				# convert to numpy array
				print('x ', x)						
				print('z', z) 
				xv = np.array(x)
				zv = np.array(z)
				plt.plot(xv, zv, label = label + '_' + t[274].replace('_out-of-vocabulary_Accuracy', ''), linestyle=linestyle, marker=marker, color=color)	
				plt.ylim([.5,1])
				plt.xlabel('Training size')
				plt.title('POS accuracy for in-domain OOV')
				x = []
				y = []
				z = []
				xv = []
				zv = []
				label = ''
				marker = ''
	
# POS OVV out of domain
for root, subdirs, files in sortedWalk(walkDirPos):
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
			if re.match("glove_updated_incretuneparam.txt", filename):					
				color='b'
				label = "glove_up"
			elif re.match("cbow_negsam_noupdated_best.txt", filename):
				color='g'
				marker = noupMarker
				label = "cbow_negsam_noup"
			elif re.match("cbow_negsam_updated_incretuneparam.txt", filename): 
				color='g'
				label = "cbow_negsam_up"
			elif re.match("skip_gram_negsam_noupdated_best.txt", filename):
				color='y'
				marker = noupMarker
				label = "skip_gram_negsam_noup"
			elif re.match("skip_gram_negsam_updated_incretuneparam.txt", filename): 
				color='y'
				label = "skip_gram_negsam_up"
			elif re.match("cw_updated_incretuneparam.txt", filename): 
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
				print('column title:', t[177])	# out-of-domain EngWebTreebank_out-of-vocabulary_Accuracy
				fig.add_subplot(6, 2, 2)
				fig.subplots_adjust(hspace=1.5)
				# skip the first row with the titles
				for line in lines[1:]: 
					p = line.split()	
					x.append(float(p[0]))				
					y.append(float(p[177]))
				# convert to numpy array
				print('x ', x)						
				print('y ', y)			
				xv = np.array(x)
				yv = np.array(y)
				plt.plot(xv, yv, label = label + '_' + t[177].replace('_out-of-vocabulary_Accuracy', ''), linestyle=linestyle, marker=marker, color=color)  
				plt.ylim([.5,1])
				plt.xlabel('Training size')
				plt.title('POS accuracy for out-of-domain OOV')
				x = []
				y = []
				z = []
				xv = []
				yv = []				
				label = ''
				marker = ''

# NER OOV in domain
for root, subdirs, files in sortedWalk(walkDirNer):
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
			if re.match("glove_updated_incretuneparam.txt", filename):					
				color='b'
				label = "glove_up"
			elif re.match("cbow_negsam_noupdated_best.txt", filename):
				color='g'
				marker = noupMarker
				label = "cbow_negsam_noup"
			elif re.match("cbow_negsam_updated_incretuneparam.txt", filename): 
				color='g'
				label = "cbow_negsam_up"
			elif re.match("skip_gram_negsam_noupdated_best.txt", filename):
				color='y'
				marker = noupMarker
				label = "skip_gram_negsam_noup"
			elif re.match("skip_gram_negsam_updated_incretuneparam.txt", filename): 
				color='y'
				label = "skip_gram_negsam_up"
			elif re.match("cw_updated_incretuneparam.txt", filename): 
				color='k'
				label =  "cw_up"
			elif re.match("cw_noupdated_best.txt", filename):
				color='k'
				marker = noupMarker
				label = "cw_noup"
			elif re.match("brown_cluster_v2000_best.txt", filename): 
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
				print('column title 2:', t[2])		# in domain out-of-vocabulary_Accuracy: as Accuracy 'H'
				fig.add_subplot(6, 2, 3)
				fig.subplots_adjust(hspace=1.5)
				# skip the first row with the titles
				for line in lines[1:]: 
					p = line.split()	
					x.append(float(p[0]))				
					z.append(float(p[2]))
				# convert to numpy array
				print('x ', x)			
				print('z', z) 
				xv = np.array(x)
				zv = np.array(z)
				plt.plot(xv, zv, label = label + '_' + t[28].replace('_out-of-vocabulary_Accuracy', ''), linestyle=linestyle, marker=marker, color=color)
				plt.ylim([.5,1])
				plt.xlabel('Training size')
				plt.title('NER accuracy for in-domain OOV')
				x = []
				z = []
				xv = []
				zv = []
				label = ''
				marker = ''	

# NER OOV out domain
for root, subdirs, files in sortedWalk(walkDirNer):
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
			if re.match("glove_updated_incretuneparam.txt", filename):					
				color='b'
				label = "glove_up"
			elif re.match("cbow_negsam_noupdated_best.txt", filename):
				color='g'
				marker = noupMarker
				label = "cbow_negsam_noup"
			elif re.match("cbow_negsam_updated_incretuneparam.txt", filename): 
				color='g'
				label = "cbow_negsam_up"
			elif re.match("skip_gram_negsam_noupdated_best.txt", filename):
				color='y'
				marker = noupMarker
				label = "skip_gram_negsam_noup"
			elif re.match("skip_gram_negsam_updated_incretuneparam.txt", filename): 
				color='y'
				label = "skip_gram_negsam_up"
			elif re.match("cw_updated_incretuneparam.txt", filename): 
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
				print('column title 2:', t[28])		# OUT OF DOMAIN MUC_out-of-vocabulary_Accuracy
				fig.add_subplot(6, 2, 4)
				fig.subplots_adjust(hspace=1.5)
				# skip the first row with the titles
				for line in lines[1:]: 
					p = line.split()	
					x.append(float(p[0]))				
					z.append(float(p[28]))
				# convert to numpy array
				print('x ', x)			
				print('z', z) 
				xv = np.array(x)
				zv = np.array(z)
				plt.plot(xv, zv , label = label + '_' + t[28].replace('_out-of-vocabulary_Accuracy', ''), linestyle=linestyle, marker=marker, color=color)
				plt.ylim([.5,1])	
				plt.xlabel('Training size')
				plt.title('NER accuracy for out-of-domain OOV')		
				x = []
				z = []
				xv = []
				zv = []
				label = ''
				marker = ''	

# Chunking
for root, subdirs, files in sortedWalk(walkDirChu):
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
			if re.match("glove_updated_incretuneparam.txt", filename):					
				color='b'
				label = "glove_up"
			elif re.match("cbow_negsam_noupdated_best.txt", filename):
				color='g'
				marker = noupMarker
				label = "cbow_negsam_noup"
			elif re.match("cbow_negsam_updated_incretuneparam.txt", filename): 
				color='g'
				label = "cbow_negsam_up"
			elif re.match("skip_gram_negsam_noupdated_best.txt", filename):
				color='y'
				marker = noupMarker
				label = "skip_gram_negsam_noup"
			elif re.match("skip_gram_negsam_updated_incretuneparam.txt", filename): 
				color='y'
				label = "skip_gram_negsam_up"
			elif re.match("cw_updated_incretuneparam.txt", filename): 
				color='k'
				label =  "cw_up"
			elif re.match("cw_noupdated_best.txt", filename):
				color='k'
				marker = noupMarker
				label = "cw_noup"
			elif re.match("brown_cluster_v2000_best.txt", filename): 
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
				print('column title 2:', t[7])		# in domain out-of-vocabulary_Accuracy: as Accuracy 'H'
				fig.add_subplot(6, 2, 5)
				fig.subplots_adjust(hspace=1.5)
				# skip the first row with the titles
				for line in lines[1:]: 
					p = line.split()	
					x.append(float(p[0]))				
					z.append(float(p[7]))
				# convert to numpy array
				print('x ', x)			
				print('z', z) 
				xv = np.array(x)
				zv = np.array(z)
				plt.plot(xv, zv, label = label + '_' + t[28].replace('_out-of-vocabulary_Accuracy', ''), linestyle=linestyle, marker=marker, color=color)	
				plt.ylim([.5,1])
				plt.xlabel('Training size')
				plt.title('Chunking accuracy for in-domain OOV')
				x = []
				z = []
				xv = []
				zv = []
				label = ''
				marker = ''	

# MWEs
for root, subdirs, files in sortedWalk(walkDirMwe):
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
				fig.add_subplot(6, 2, 6)
				fig.subplots_adjust(hspace=1.5)
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
				plt.ylim([.5,1])	
				plt.xlabel('Training size')
				plt.title('MWE accuracy for in-domain OOV')
				x = []
				y = []
				xv = []
				yv = []
				label = ''	
				marker = ''

legParams = {'legend.fontsize': 10}
plt.rcParams.update(legParams)
#plt.legend(loc="best")
plt.legend(loc='upper center', bbox_to_anchor=(0, -0.2),fancybox=True, shadow=True, ncol=5)

fig.tight_layout()
savefig(sys.argv[5], bbox_inches='tight')

























