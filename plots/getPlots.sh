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
python POS-OOV-IN.py -i ../eval_results/results/POS -o POS-OOV-IN.png
python POS-OOV-OUT.py -i ../eval_results/results/POS -o POS-OOV-OUT.png

#- Chunking
python ChunkingOOV.py -i ../eval_results/results/chunking -o Chunking-OOV.png

#- NER
python NER-OOV-IN.py -i ../eval_results/results/NER -o NER-OOV-IN.png
python NER-OOV-OUT.py -i ../eval_results/results/NER -o NER-OOV-OUT.png

#- MWE 
python MWE-OOV.py -i ../eval_results/results/MWE -o MWE-OOV.png


############################
#MANUAL vs. INCREMENTAL 
############################

#python POSmanual-incre.py -i ../POS -o POSmanual-incre.png

#python CHUmanual-incre.py -i ../chunking -o CHUmanual-incre.png

#python NERmanual-incre.py -i ../NER -o NERmanual-incre.png

#python MWEmanual-incre.py -i ../MWEs -o MWEmanual-incre.png


echo 'I finished :)'




