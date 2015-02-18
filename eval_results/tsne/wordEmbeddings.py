#!/usr/bin/python

# # This script calculate word coordinate in a vector space of given word embedding files and print the coordinates into a csv table named coordinate.csv under current folder.
#  VERSION 1.0
#  Liyuan ZHOU, NICTA CRL, 2015
#
# Usage: 
# 	wordEmbeddings.py [-u <updateWordEmbeddingFiles>] [-n <notUpdateWordEmbeddingFile>] [-w <wordListFile>]
# 	
# 	-u <updateWordEmbeddingFile1,updateWordEmbeddingFile2,...>: files seperated by , without space.
# 	-n <notUpdateWordEmbeddingFile>: not update word embedding file.
# 	-w <wordListFile>: a txt file that list words
# 	
# Example: 
# 	./wordEmbeddings.py -u uptest1.txt,uptest2.txt -n nouptest.txt -w wordList.txt
# 					

from tsne import tsne
import numpy as Math
import sys, getopt
import matplotlib.pyplot as plt
import os
# import render
length = 0

def readArgs(argv):
   updatefile = ''
   noupdatefile = ''
   wordList = ''
   out = ''
   try:
      opts, args = getopt.getopt(argv, "hu:n:w:o:", ["updatefile=", "noupdatefile=", "wordList=", "outputFile="])
   except getopt.GetoptError:
      print 'wordEmbeddings.py -u <updatefile> -n <noupdatefile> -w <wordList> -o <outputFile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'wordEmbeddings.py -u <updatefile> -n <noupdatefile> -w <wordList> -o <outputFile>'
         sys.exit()
      elif opt in ("-u", "--updatefile"):
         updatefile = arg
      elif opt in ("-n", "--noupdatefile"):
         noupdatefile = arg
      elif opt in ("-w", "--wordList"):
         wordList = arg
      elif opt in ("-o", "--outputFile"):
         out = arg
   return updatefile, noupdatefile, wordList, out

def loadData(txt):
	print "Loading data for %s" % txt
	f = open(txt, 'r')

	result = {}
	for row in f:
		listedline = row.strip().split(' ')
		key = listedline[0]	
		if key in result:
			pass
		result[key] = [float(x) for x in listedline[1:]]
		length = len(listedline) - 1

	return result

def getArray(dic, wordListfile):
	print "Building arrays..."
	f = open(wordListfile, 'r')
	labels = []
	for row in f:
		listedline = row.strip().split('\n')
		if listedline[0]: 
			labels.append(listedline[0])

	array = []
	for word in labels:
		if dic.get(word): 
			array.append(dic.get(word))
		else:
 			empty = [float(0.0) for i in range(0,length)]
 			print type(empty)
 			array.append(empty)
			
	return Math.array(array), labels

def reserved(string):
	if string == "'":
		string = "S_quote"
	if string == '"':
		string = "D_quote"
	return string


def norm1(array, margin, W, H):
	print "Normalizing array..."
	normalized = []

	minx = 0
    	maxx = 0
    	miny = 0
    	maxy = 0
	minu = 0
    	maxu = 0
    	minv = 0
    	maxv = 0
    	for (x, y, u, v) in array:
   	     if minx > x: minx = x
    	     if maxx < x: maxx = x
    	     if miny > y: miny = y
     	     if maxy < y: maxy = y
   	     if minu > u: minu = u
    	     if maxu < u: maxu = u
    	     if minv > v: minv = v
     	     if maxv < v: maxv = v

   	dx = maxx - minx
    	dy = maxy - miny
   	du = maxu - minu
    	dv = maxv - minv
    	assert dx > 0
    	assert dy > 0
    	assert du > 0
    	assert dv > 0
    	minx -= dx * margin
    	miny -= dy * margin
    	maxx += dx * margin
    	maxy += dy * margin
    	minu -= du * margin
    	minv -= dv * margin
    	maxu += du * margin
    	maxv += dv * margin

	for (x, y, u, v) in array:	
		x = (x - minx) / (maxx - minx) * W
        	y = (y - miny) / (maxy - miny) * H
		u = (u - minu) / (maxu - minu) * W
        	v = (v - minv) / (maxv - minv) * H
		normalized.append([x, y, u, v])
	
	return normalized, minx, miny, maxx, maxy

def norm2(array, margin, W, H):
	print "Normalizing array..."
	normalized = []

	minx = 0
    	maxx = 0
    	miny = 0
    	maxy = 0
    	for (x, y, u, v) in array:
   	     if minx > x: minx = x
    	     if maxx < x: maxx = x
    	     if miny > y: miny = y
     	     if maxy < y: maxy = y

   	     if minx > u: minx = u
    	     if maxx < u: maxx = u
    	     if miny > v: miny = v
     	     if maxy < v: maxy = v

   	dx = maxx - minx
    	dy = maxy - miny

#    	assert dx > 0
#    	assert dy > 0

    	minx -= dx * margin
    	miny -= dy * margin
    	maxx += dx * margin
    	maxy += dy * margin

	for (x, y, u, v) in array:	
		x = (x - minx) / (maxx - minx) * W
        	y = (y - miny) / (maxy - miny) * H
		u = (u - minx) / (maxx - minx) * W
        	v = (v - miny) / (maxy - miny) * H
		normalized.append([x, y, u, v])
	
	return normalized, minx, miny, maxx, maxy


if __name__ == "__main__":

	vecField = []
	updatefiles, noupdatefile, wordList, out = readArgs(sys.argv[1:])
	coordinate = open(out, 'w')
	noupdateData = loadData(noupdatefile)
	noup_array, labels = getArray(noupdateData, wordList)
	noupdateData.clear()

	vecField.append(noup_array)

	out_noup = tsne(noup_array, no_dims=2, perplexity=30, initial_dims=30)

	coordinate.write("word\tx_noup\ty_noup")

	updatefileList = updatefiles.strip().split(",")

	out_up = []
	for updatefile in updatefileList:
# 		filename = ('.').join(updatefile.split('.')[:-1])
		filename = os.path.splitext(os.path.basename(updatefile))[0]
		coordinate.write("\tx_{0}\ty_{1}".format(filename, filename))
		updateData = loadData(updatefile)
		up_array, labels = getArray(updateData, wordList)
		updateData.clear()
		out_up.append(tsne(up_array, no_dims=2, perplexity=30, initial_dims=30))
	
	coordinate.write("\n")

	margin = 0.05
	width = 3000
	height = 1800
	plt.figure()
# 	RGB = [0,0,0]
# 	print '#{:02X}{:02X}{:02X}'.format(*RGB)
    
	rgb = 0
#    print "length of labels: %s" % len(labels)
	for i in range(0, len(labels)):
		array = []
		coordinate.write("{0}\t{1}\t{2}".format(reserved(labels[i]), out_noup[i][0], out_noup[i][1]))
		print "{0}\t{1}\t{2}".format(labels[i], out_noup[i][0], out_noup[i][1])
        
		for up in out_up:
			coordinate.write("\t{0}\t{1}".format(up[i][0], up[i][1]))
			array.append([out_noup[i][0], out_noup[i][1], up[i][0], up[i][1]])
			print "\t{0}\t{1}".format(up[i][0], up[i][1])
		coordinate.write("\n")
		
		array, minx, miny, maxx, maxy = norm2(array, margin, width, height)
		X, Y, U, V = zip(*array)
	
		ax = plt.gca()
		colorCode = '#{:06X}'.format(rgb)
		ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=20, color=colorCode, width=0.001, headwidth=3)
		plt.text(X[0], Y[0], labels[i], color=colorCode)
		rgb = rgb + 2500

# 		ax.set_xlim([minx,maxx])
# 		ax.set_ylim([miny,maxy])
		plt.draw()

	plt.show()
		
		

	# render.render([(labels, point[0], point[1]) for labels, point in zip(labels, out_up)], "test-output.rendered.png", width=3000, height=1800)



# This is the end of script
#try:
#	x = int(raw_input("Please enter a number: "))
#	break
#except ValueError:
#	print "Oops!  That was no valid number.  Try again..."
