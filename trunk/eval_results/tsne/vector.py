#!/usr/bin/python

import matplotlib.pyplot as plt
import sys, getopt
import csv
from wordEmbeddings import norm2 as norm 
from numpy import genfromtxt

def readArgs(argv):
   csv = ''
   try:
      opts, args = getopt.getopt(argv,"hc:",["csvfile="])
   except getopt.GetoptError:
      print 'vector.py -c <csvFile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'vector.py -c <csvFile>'
         sys.exit()
      elif opt in ("-c", "--csvFile"):
         csv = arg
   return csv

def draw(csvfile):
	coordinate = genfromtxt(csvfile, delimiter="	",dtype=None)
	embeddings, labels = dataSplit(coordinate)

	margin=0.05
	width=3000
	height=1800
	plt.figure()
#	RGB = [0,0,0]
#	print '#{:02X}{:02X}{:02X}'.format(*RGB)
	
	rgb = 0
	for i in range(0,len(labels)):	
#		array, minx, miny, maxx, maxy = norm(array,margin,width,height)
		print embeddings[i]
		array = embeddings[i]
		X,Y,U,V = zip(*array)
	
		ax = plt.gca()
		colorCode = '#{:06X}'.format(rgb)
		ax.quiver(X,Y,U,V,angles='xy',scale_units='xy',scale=10,color=colorCode, width=0.001,  headwidth=3)
		plt.text(X[0],Y[0], labels[i], color=colorCode)
		rgb = rgb + 2500

#		ax.set_xlim([minx,maxx])
#		ax.set_ylim([miny,maxy])
		plt.draw()

	plt.show()

def dataSplit(coordinate):
	embeddings = []
	labels = []
	firstline = True
	for row in coordinate:
		if firstline:
			firstline = False
        		continue
		labels.append(row[0])	
		array = []
		for point in (3,len(row),2):
			if point+1 <= len(row):
				array.append([float(row[1]),float(row[2]),float(row[point]),float(row[point+1])])
		print array
		embeddings.append(array)
			

	return array, labels

if __name__ == "__main__":
	csvfile = readArgs(sys.argv[1:])
	draw(csvfile)
		
	
