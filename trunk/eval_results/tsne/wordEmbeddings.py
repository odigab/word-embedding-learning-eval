#!/usr/bin/python

from tsne import tsne
import numpy as Math
import sys, getopt
#import render

def readArgs(argv):
   updatefile = ''
   noupdatefile = ''
   wordList = ''
   try:
      opts, args = getopt.getopt(argv,"hu:n:w:",["updatefile=","noupdatefile=","wordList="])
   except getopt.GetoptError:
      print 'wordEmbeddings.py -u <updatefile> -n <noupdatefile> -w <wordList>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'wordEmbeddings.py -u <updatefile> -n <noupdatefile> -w <wordList>'
         sys.exit()
      elif opt in ("-u", "--updatefile"):
         updatefile = arg
      elif opt in ("-n", "--noupdatefile"):
         noupdatefile = arg
      elif opt in ("-w", "--wordList"):
         wordList = arg
#   print 'update word embedding file is: \t', updatefile
#   print 'no update word embedding file is: \t', noupdatefile
#   print 'word List file is: \t', wordList
   return updatefile, noupdatefile, wordList

def loadData(txt):
	f = open(txt, 'r')

	result = {}
	for row in f:
		listedline = row.strip().split(' ')
		key = listedline[0]	
		if key in result:
			pass
		result[key] = [float(x) for x in listedline[1:]]

	return result

def getArray(noup = dict, wordListfile = str):
	f = open(wordListfile, 'r')
	wordList = []
	for row in f:
		listedline = row.strip().split('\n')
		if listedline[0]: wordList.append(listedline[0])

	array = []
	labels = []
	for word in wordList:
		if noup.get(word): 
			array.append(noup.get(word))
			labels.append(word)
			
	
	return Math.array(array), labels




if __name__ == "__main__":

	coordinate = open("coordinate.csv", 'w')

	updatefiles, noupdatefile, wordList = readArgs(sys.argv[1:])
	
	noupdateData = loadData(noupdatefile)
	noup_array, labels = getArray(noupdateData, wordList)
	out_noup = tsne(noup_array, no_dims=2, perplexity=30, initial_dims=30)

	coordinate.write("word\tx_noup\ty_noup")

	updatefileList = updatefiles.strip().split(",")

	out_up = []
	for updatefile in updatefileList:
		filename = ('.').join(updatefile.split('.')[:-1])
		coordinate.write("\tx_{0}\ty_{1}".format(filename, filename))
		updateData = loadData(updatefile)
		up_array, labels = getArray(updateData, wordList)
		out_up.append(tsne(up_array, no_dims=2, perplexity=30, initial_dims=30))
	
	coordinate.write("\n")
	

#	coordinate.write("word,x_noup,x_up,y_noup,y_up\n")
	for i in range(0,len(labels)):
		coordinate.write("{0}\t{1}\t{2}".format(labels[i], out_noup[i][0], out_noup[i][1]))
		for up in out_up:
			coordinate.write("\t{0}\t{1}".format(up[i][0], up[i][1]))
		coordinate.write("\n")
		

	#render.render([(labels, point[0], point[1]) for labels, point in zip(labels, out_up)], "test-output.rendered.png", width=3000, height=1800)



# This is the end of script
