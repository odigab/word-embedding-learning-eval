#!/usr/bin/python

import sys, getopt
import matplotlib.pyplot as plt
from numpy import genfromtxt
import csv
import operator as op
import requests
import numpy

# normalization 
# (Xo - Xmin) / (Xmax - Xmin)
 
table = numpy.genfromtxt(sys.argv[1],dtype='float',delimiter =',',skip_header=1, skip_footer=0,usemask=True, usecols=(1,2,3,4,5,6,7,8,9,10))
print table.max() 
print table.min() 
print '\n\n'


denominator = table.max() - table.min()	
print denominator
print '\n'

newRow = []
newTable = []

for row in table:
	for cel in row:
		print cel		
		nominator = cel - table.min() 
		newValue = nominator/denominator 
		print newValue
		newRow.append(newValue)	
	newTable.append(newRow)
	newRow = []

ofile  = open(sys.argv[2], "wb")

writer = csv.writer(ofile, delimiter=',')
writer.writerows(newTable)
ofile.close()


						















































