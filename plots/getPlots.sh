#!/bin/sh


# PLOTING COMMANDS

############################
# BEST RESULTS FOR EACH METHOD
############################

# - POS
#python bestPOS.py -i ../POS -o bestPOS.png
python bestPOS.py -i ../eval_results/results/POS -o bestPOS.png

#- Chunking
#python bestChunk.py -i ../chunking -o bestChunking.png
python bestChunk.py -i ../eval_results/results/chunking -o bestChunking.png 

#- NER
#python bestNER.py -i ../NER -o bestNER.png
python bestNER.py -i ../eval_results/results/NER -o bestNER.png

#- MWE 
#python bestMWE.py -i ../MWEs -o bestMWE.png
python bestMWE.py -i ../eval_results/results/MWE -o bestMWE.png

# * there are no results for chukning unigram!!

############################
#OUT OF VOCABULARY ACCURACY
############################

#- POS
#python POSoutOfVocIN.py -i ../POS -o POSoutOfVocIN.png
python POSoutOfVocIN.py -i ../eval_results/results/POS -o POSoutOfVocIN.png

#python POSoutOfVocOUT.py -i ../POS -o POSoutOfVocOUT.png
python POSoutOfVocOUT.py -i ../eval_results/results/POS -o POSoutOfVocOUT.png

#- NER
#python NERoutOfVocIN.py -i ../NER -o NERoutOfVocIN.png
python NERoutOfVocIN.py -i ../eval_results/results/NER -o NERoutOfVocIN.png

#python NERoutOfVocOUT.py -i ../NER -o NERoutOfVocOUT.png
python NERoutOfVocOUT.py -i ../eval_results/results/NER -o NERoutOfVocOUT.png

#- MWE 
#python MWEoutOfVoc.py -i ../MWEs -o MWEoutOfVoc.png
python MWEoutOfVoc.py -i ../eval_results/results/MWE -o MWEoutOfVoc.png

# * there are no experiment for chunking with out of voc words!


############################
#MANUAL vs. INCREMENTAL 
############################

#python POSmanual-incre.py -i ../POS -o POSmanual-incre.png

#python CHUmanual-incre.py -i ../chunking -o CHUmanual-incre.png

#python NERmanual-incre.py -i ../NER -o NERmanual-incre.png

#python MWEmanual-incre.py -i ../MWEs -o MWEmanual-incre.png


echo 'I finished :)'




