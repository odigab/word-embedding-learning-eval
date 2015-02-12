Each subfolder of each task is named after its model name and experimental setup. 
     noupdated: no update of word embeddings
     updated: update word embeddings
     updated_incretuneparam: update word embeddings with incremental hyperparameter tuning

CHUNKING
	key evaluation metrics: chunks_F1Measure chunks_Precision chunks_Recall
        out of vocabulary metric: Accuracy 

NER
	key evaluation metrics: chunks_F1Measure chunks_Precision chunks_Recall
        out of domain : MUC7_chunks_F1Measure MUC7_chunks_Precision MUC7_chunks_Recall
        out of vocabulary metric: CONLL_out.of.vocabulary_Accuracy  MUC7_out.of.vocabulary_Accuracy 

MWE
	key evaluation metrics: mwe_F1Measure mwe_Precision mwe_Recall
        out of vocabulary metric: out.of.vocabulary_Accuracy  

POS
	key evaluation metric: Accuracy
        out of domain : EngWebTreebank_Accuracy
	out of vocabulary metrics: WSJ_out.of.vocabulary_Accuracy EngWebTreebank_out.of.vocabulary_Accuracy

LabelRank.R
LabelRank.R is a R script to compare the differences of each individual evaluation metrics between two result files and rank them. It goes through each evaluation metric, computes the average absolute differences between the same metrics from the two files, and rank them in ascending order.
Usage: LabelRank.R file_1 file_2

MeasereTable.R
MeasereTable.R is a R script that prints out a given evaluation method of different methods in a single table.
MeasureTable.R --eval=evaluation_method --files=file1,file2,file3... --output=outputfile.csv

/tsne/wordEmbeddings.py

wordEmbeddings.py is a python script to calculate word coordinate in a vector space of given word embedding files and print the coordinates into a csv table named coordinate.csv under current folder. 
wordEmbeddings.py -u <updateFile1,updateFile2,...> -n <notUpdateFile> -w <wordList>
