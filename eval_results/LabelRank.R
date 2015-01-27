#!/usr/bin/Rscript
## LabelRank.R is a R script to compare the differences of each individual evaluation metrics between two result files and rank them. It goes through each evaluation metric, computes the average absolute differences between the same metrics from the two files, and rank them in ascending order
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
