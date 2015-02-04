#!/bin/sh


# PLOTING COMMANDS

############################
# BEST RESULTS FOR EACH METHOD
############################

# - POS
#python bestPOS.py -i ../POS -o bestPOS.pdf
python bestPOS.py -i ../eval_results/results/POS -o bestPOS.pdf

#- Chunking
#python bestChunk.py -i ../chunking -o bestChunking.pdf
python bestChunk.py -i ../eval_results/results/chunking -o bestChunking.pdf 

#- NER
#python bestNER.py -i ../NER -o bestNER.pdf
python bestNER.py -i ../eval_results/results/NER -o bestNER.pdf

#- MWE 
#python bestMWE.py -i ../MWEs -o bestMWE.pdf
python bestMWE.py -i ../eval_results/results/MWE -o bestMWE.pdf

# * there are no results for chukning unigram!!

############################
#OUT OF VOCABULARY ACCURACY
############################

#- POS
python POS-OOV-IN.py -i ../eval_results/results/POS -o POS-OOV-IN.pdf
python POS-OOV-OUT.py -i ../eval_results/results/POS -o POS-OOV-OUT.pdf

#- Chunking
python ChunkingOOV.py -i ../eval_results/results/chunking -o Chunking-OOV.pdf

#- NER
python NER-OOV-IN.py -i ../eval_results/results/NER -o NER-OOV-IN.pdf
python NER-OOV-OUT.py -i ../eval_results/results/NER -o NER-OOV-OUT.pdf

#- MWE 
python MWE-OOV.py -i ../eval_results/results/MWE -o MWE-OOV.pdf


############################
#MANUAL vs. INCREMENTAL 
############################

#python POSmanual-incre.py -i ../POS -o POSmanual-incre.pdf

#python CHUmanual-incre.py -i ../chunking -o CHUmanual-incre.pdf

#python NERmanual-incre.py -i ../NER -o NERmanual-incre.pdf

#python MWEmanual-incre.py -i ../MWEs -o MWEmanual-incre.pdf


echo 'I finished :)'




