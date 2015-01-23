#!/usr/bin/Rscript
## This R script ranks labels according to the sum of absolute dif between each label of given two files.
#  VERSION 1.0
#  Liyuan ZHOU, NICTA CRL, 2015
#
# Usage: 
#	LabelRank.R resultA resultB
#	
#	resultA: path to resultA
#	resultB: path to resultB
#	
# Example: 
#	./LabelRank.R /media/data3tb1/SequenceTaggingEvaluation/chunking/cbow_updated/cbow_negsam_updated_incretuneparam.txt /media/data3tb1/SequenceTaggingEvaluation/chunking/cbow_noupdated/cbow_negsam_noupdated_best.txt
#						

args<-commandArgs(TRUE)

resultA = data.matrix(read.table(file = args[1], header = TRUE, sep = "\t"))

row = nrow(resultA)
columns = ncol(resultA)

resultB = data.matrix(read.table(file = args[2], header = TRUE, sep = "\t"))

diff <- abs(resultA - resultB)

x2 <- colSums(diff)
sort(x2)
