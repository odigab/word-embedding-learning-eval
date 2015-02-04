#!/usr/bin/Rscript
## This R script prints out a table of a given evaluation method that lists all given word embedding methods. 
#  VERSION 1.0
#  Liyuan ZHOU, NICTA CRL, 2015
#
# Usage: 
#	MeasureTable.R eval files output
#	
#	task: optional; NER, Chunking, POS, and MWEs
#	eval: evaluation method
#		Chunking: ADJP_F1Measure	ADJP_Precision	ADJP_Recall	ADVP_F1Measure	ADVP_Precision	ADVP_Recall	Accuracy	CONJP_F1Measure	CONJP_Precision	CONJP_Recall	INTJ_F1Measure	INTJ_Precision	INTJ_Recall	LST_F1Measure	LST_Precision	LST_Recall	NP_F1Measure	NP_Precision	NP_Recall	PP_F1Measure	PP_Precision	PP_Recall	PRT_F1Measure	PRT_Precision	PRT_Recall	SBAR_F1Measure	SBAR_Precision	SBAR_Recall	VP_F1Measure	VP_Precision	VP_Recall	chunks_F1Measure	chunks_Precision	chunks_Recall	macro_F1Measure	macro_Precision	macro_Recall	micro_F1Measure	micro_Precision	micro_Recall
#		NER: Accuracy	CONLL_out.of.vocabulary_Accuracy	LOC_F1Measure	LOC_Precision	LOC_Recall	MISC_F1Measure	MISC_Precision	MISC_Recall	MUC7_Accuracy	MUC7_LOC_F1Measure	MUC7_LOC_Precision	MUC7_LOC_Recall	MUC7_ORG_F1Measure	MUC7_ORG_Precision	MUC7_ORG_Recall	MUC7_PER_F1Measure	MUC7_PER_Precision	MUC7_PER_Recall	MUC7_chunks_F1Measure	MUC7_chunks_Precision	MUC7_chunks_Recall	MUC7_macro_F1Measure	MUC7_macro_Precision	MUC7_macro_Recall	MUC7_micro_F1Measure	MUC7_micro_Precision	MUC7_micro_Recall	MUC7_out.of.vocabulary_Accuracy	ORG_F1Measure	ORG_Precision	ORG_Recall	PER_F1Measure	PER_Precision	PER_Recall	chunks_F1Measure	chunks_Precision	chunks_Recall	macro_F1Measure	macro_Precision	macro_Recall	micro_F1Measure	micro_Precision	micro_Recall
#		POS: #_F1Measure	#_Precision	#_Recall	$_F1Measure	$_Precision	$_Recall	''_F1Measure	''_Precision	''_Recall	,_F1Measure	,_Precision	,_Recall	.LRB._F1Measure	.LRB._Precision	.LRB._Recall	.RRB._F1Measure	.RRB._Precision	.RRB._Recall	._F1Measure	._Precision	._Recall	:_F1Measure	:_Precision	:_Recall	Accuracy	CC_F1Measure	CC_Precision	CC_Recall	CD_F1Measure	CD_Precision	CD_Recall	DT_F1Measure	DT_Precision	DT_Recall	EX_F1Measure	EX_Precision	EX_Recall	EngWebTreebank_$_F1Measure	EngWebTreebank_$_Precision	EngWebTreebank_$_Recall	EngWebTreebank_''_F1Measure	EngWebTreebank_''_Precision	EngWebTreebank_''_Recall	EngWebTreebank_,_F1Measure	EngWebTreebank_,_Precision	EngWebTreebank_,_Recall	EngWebTreebank_.LRB._F1Measure	EngWebTreebank_.LRB._Precision	EngWebTreebank_.LRB._Recall	EngWebTreebank_.RRB._F1Measure	EngWebTreebank_.RRB._Precision	EngWebTreebank_.RRB._Recall	EngWebTreebank_._F1Measure	EngWebTreebank_._Precision	EngWebTreebank_._Recall	EngWebTreebank_:_F1Measure	EngWebTreebank_:_Precision	EngWebTreebank_:_Recall	EngWebTreebank_Accuracy	EngWebTreebank_CC_F1Measure	EngWebTreebank_CC_Precision	EngWebTreebank_CC_Recall	EngWebTreebank_CD_F1Measure	EngWebTreebank_CD_Precision	EngWebTreebank_CD_Recall	EngWebTreebank_DT_F1Measure	EngWebTreebank_DT_Precision	EngWebTreebank_DT_Recall	EngWebTreebank_EX_F1Measure	EngWebTreebank_EX_Precision	EngWebTreebank_EX_Recall	EngWebTreebank_FW_F1Measure	EngWebTreebank_FW_Precision	EngWebTreebank_FW_Recall	EngWebTreebank_IN_F1Measure	EngWebTreebank_IN_Precision	EngWebTreebank_IN_Recall	EngWebTreebank_JJR_F1Measure	EngWebTreebank_JJR_Precision	EngWebTreebank_JJR_Recall	EngWebTreebank_JJS_F1Measure	EngWebTreebank_JJS_Precision	EngWebTreebank_JJS_Recall	EngWebTreebank_JJ_F1Measure	EngWebTreebank_JJ_Precision	EngWebTreebank_JJ_Recall	EngWebTreebank_LS_F1Measure	EngWebTreebank_LS_Precision	EngWebTreebank_LS_Recall	EngWebTreebank_MD_F1Measure	EngWebTreebank_MD_Precision	EngWebTreebank_MD_Recall	EngWebTreebank_NNPS_F1Measure	EngWebTreebank_NNPS_Precision	EngWebTreebank_NNPS_Recall	EngWebTreebank_NNP_F1Measure	EngWebTreebank_NNP_Precision	EngWebTreebank_NNP_Recall	EngWebTreebank_NNS_F1Measure	EngWebTreebank_NNS_Precision	EngWebTreebank_NNS_Recall	EngWebTreebank_NN_F1Measure	EngWebTreebank_NN_Precision	EngWebTreebank_NN_Recall	EngWebTreebank_PDT_F1Measure	EngWebTreebank_PDT_Precision	EngWebTreebank_PDT_Recall	EngWebTreebank_POS_F1Measure	EngWebTreebank_POS_Precision	EngWebTreebank_POS_Recall	EngWebTreebank_PRP$_F1Measure	EngWebTreebank_PRP$_Precision	EngWebTreebank_PRP$_Recall	EngWebTreebank_PRP_F1Measure	EngWebTreebank_PRP_Precision	EngWebTreebank_PRP_Recall	EngWebTreebank_RBR_F1Measure	EngWebTreebank_RBR_Precision	EngWebTreebank_RBR_Recall	EngWebTreebank_RBS_F1Measure	EngWebTreebank_RBS_Precision	EngWebTreebank_RBS_Recall	EngWebTreebank_RB_F1Measure	EngWebTreebank_RB_Precision	EngWebTreebank_RB_Recall	EngWebTreebank_RP_F1Measure	EngWebTreebank_RP_Precision	EngWebTreebank_RP_Recall	EngWebTreebank_SYM_F1Measure	EngWebTreebank_SYM_Precision	EngWebTreebank_SYM_Recall	EngWebTreebank_TO_F1Measure	EngWebTreebank_TO_Precision	EngWebTreebank_TO_Recall	EngWebTreebank_UH_F1Measure	EngWebTreebank_UH_Precision	EngWebTreebank_UH_Recall	EngWebTreebank_VBD_F1Measure	EngWebTreebank_VBD_Precision	EngWebTreebank_VBD_Recall	EngWebTreebank_VBG_F1Measure	EngWebTreebank_VBG_Precision	EngWebTreebank_VBG_Recall	EngWebTreebank_VBN_F1Measure	EngWebTreebank_VBN_Precision	EngWebTreebank_VBN_Recall	EngWebTreebank_VBP_F1Measure	EngWebTreebank_VBP_Precision	EngWebTreebank_VBP_Recall	EngWebTreebank_VBZ_F1Measure	EngWebTreebank_VBZ_Precision	EngWebTreebank_VBZ_Recall	EngWebTreebank_VB_F1Measure	EngWebTreebank_VB_Precision	EngWebTreebank_VB_Recall	EngWebTreebank_WDT_F1Measure	EngWebTreebank_WDT_Precision	EngWebTreebank_WDT_Recall	EngWebTreebank_WP$_F1Measure	EngWebTreebank_WP$_Precision	EngWebTreebank_WP$_Recall	EngWebTreebank_WP_F1Measure	EngWebTreebank_WP_Precision	EngWebTreebank_WP_Recall	EngWebTreebank_WRB_F1Measure	EngWebTreebank_WRB_Precision	EngWebTreebank_WRB_Recall	EngWebTreebank_``_F1Measure	EngWebTreebank_``_Precision	EngWebTreebank_``_Recall	EngWebTreebank_macro_F1Measure	EngWebTreebank_macro_Precision	EngWebTreebank_macro_Recall	EngWebTreebank_micro_F1Measure	EngWebTreebank_micro_Precision	EngWebTreebank_micro_Recall	EngWebTreebank_out.of.vocabulary_Accuracy	FW_F1Measure	FW_Precision	FW_Recall	IN_F1Measure	IN_Precision	IN_Recall	JJR_F1Measure	JJR_Precision	JJR_Recall	JJS_F1Measure	JJS_Precision	JJS_Recall	JJ_F1Measure	JJ_Precision	JJ_Recall	LS_F1Measure	LS_Precision	LS_Recall	MD_F1Measure	MD_Precision	MD_Recall	NNPS_F1Measure	NNPS_Precision	NNPS_Recall	NNP_F1Measure	NNP_Precision	NNP_Recall	NNS_F1Measure	NNS_Precision	NNS_Recall	NN_F1Measure	NN_Precision	NN_Recall	PDT_F1Measure	PDT_Precision	PDT_Recall	POS_F1Measure	POS_Precision	POS_Recall	PRP$_F1Measure	PRP$_Precision	PRP$_Recall	PRP_F1Measure	PRP_Precision	PRP_Recall	RBR_F1Measure	RBR_Precision	RBR_Recall	RBS_F1Measure	Rchunks_F1MeasureBS_Precision	RBS_Recall	RB_F1Measure	RB_Precision	RB_Recall	RP_F1Measure	RP_Precision	RP_Recall	SYM_F1Measure	SYM_Precision	SYM_Recall	TO_F1Measure	TO_Precision	TO_Recall	UH_F1Measure	UH_Precision	UH_Recall	VBD_F1Measure	VBD_Precision	VBD_Recall	VBG_F1Measure	VBG_Precision	VBG_Recall	VBN_F1Measure	VBN_Precision	VBN_Recall	VBP_F1Measure	VBP_Precision	VBP_Recall	VBZ_F1Measure	VBZ_Precision	VBZ_Recall	VB_F1Measure	VB_Precision	VB_Recall	WDT_F1Measure	WDT_Precision	WDT_Recall	WP$_F1Measure	WP$_Precision	WP$_Recall	WP_F1Measure	WP_Precision	WP_Recall	WRB_F1Measure	WRB_Precision	WRB_Recall	WSJ_out.of.vocabulary_Accuracy	``_F1Measure	``_Precision	``_Recall	macro_F1Measure	macro_Precision	macro_Recall	micro_F1Measure	micro_Precision	micro_Recall
#		MWEs: Accuracy	B_F1Measure	B_Precision	B_Recall	O_F1Measure	O_Precision	O_Recall	b_F1Measure	b_Precision	b_Recall	macro_F1Measure	macro_Precision	macro_Recall	micro_F1Measure	micro_Precision	micro_Recall	mwe_F1Measure	mwe_Precision	mwe_Recall	o_F1Measure	o_Precision	o_Recall	out.of.vocabulary_Accuracy	Ĩ_F1Measure	Ĩ_Precision	Ĩ_Recall	Ī_F1Measure	Ī_Precision	Ī_Recall	ī_F1Measure	ī_Precision	ī_Recall
#	files: files to listed in the table, seperated by commas.
#	output: output file name
#	
# Example: 
#	./MeasureTable.R --eval=chunks_F1Measure --files=/media/data3tb1/SequenceTaggingEvaluation/chunking/Brown/brown_cluster_v2000_best.txt,/media/data3tb1/SequenceTaggingEvaluation/chunking/cbow_noupdated/cbow_negsam_noupdated_best.txt,/media/data3tb1/SequenceTaggingEvaluation/chunking/cbow_updated/cbow_negsam_updated_best.txt --output="output.csv"
#						

## Collect arguments
args<-commandArgs(TRUE)

## Default setting when no arguments passed
if(length(args) < 1) {
  args <- c("--help")
}
 
## Help section
if("--help" %in% args) {
  cat("
      The R Script
 
      Arguments:
      --eval=chunks_F1Measure          - evaluation method
      --files=file1,file2,file3...     - files to be listed
      --output=output.csv              - output file name
      --help                           - print this text
 
      Example:
      ./MeasureTable.R --eval=chunks_F1Measure --files=/media/data3tb1/SequenceTaggingEvaluation/chunking/Brown/brown_cluster_v2000_best.txt,/media/data3tb1/SequenceTaggingEvaluation/chunking/cbow_noupdated/cbow_negsam_noupdated_best.txt,/media/data3tb1/SequenceTaggingEvaluation/chunking/cbow_updated/cbow_negsam_updated_best.txt --output=output.csv \n\n")
 
  q(save="no")
}

parseArgs <- function(x) strsplit(sub("^--", "", x), "=")
argsDF <- as.data.frame(do.call("rbind", parseArgs(args)))
argsL <- as.list(as.character(argsDF$V2))
names(argsL) <- argsDF$V1


files <- strsplit(argsL$files,",")[[1]]

eval=toString(argsL$eval)

temp = data.matrix(read.delim(file = files[1], header = TRUE, sep = "\t"))
out <- as.data.frame(temp[,"numSens"])

colnames(out)[1] <- "label"
decimal <- function(x, k) format(round(x, k), nsmall=k)

for(f in 1:length(files)){

	temp = data.matrix(read.delim(file = files[f], header = TRUE, sep = "\t"))
	out <- cbind(out,as.data.frame(decimal(as.numeric(temp[,eval]),4)))
#	out <- cbind(out,as.data.frame(as.numeric(temp[,eval])))

	fileName <- basename(files[f])
	fileName <- gsub("_","+",fileName)
	print(fileName)
	colnames(out)[f+1] <- substr(fileName, 0, regexpr("+[^+]*$", fileName)-2)
}
write.csv(out, file = argsL$output, eol = "\n", quote=FALSE, row.names = FALSE)



