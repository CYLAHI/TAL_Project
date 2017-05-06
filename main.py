#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import nltk
import nltk.data
import re
import TrainingData as td
import Analyze as an

if __name__ == "__main__":
        argparser = argparse.ArgumentParser()
        argparser.add_argument("-d","--directoryName", help="Folder with training examples")
        argparser.add_argument("-f","--fileName", help="File to analyze")
        args=argparser.parse_args()
        
        print("Analyzing training files... Please wait ... ")
        data=td.runTraining(args.directoryName) #Analyse des fichiers de test
        
        if args.fileName:
			print("You chose to analyze a new file to determine how many stars it should have.")
			print("Analyzing "+str(args.fileName)+ ". Please wait...")
			filename=os.path.join("tests",args.fileName) #le fichier que l'on veut analyser doit se trouver dans le dossier "tests"
			pos,neg=an.analyzeFile(filename) #Analyse du fichier
			
			print("RESULTS :")
			if(max(pos,neg)==pos): 
					print("This review is more positive than negative")
			else :
					print("This review is more negative than positive")
			
			# METHODE 1 - Non Concluante (Précision à ~0,6 étoiles)
			# res=an.getBestMatch1(data,pos,neg)
			# print("Method 1 : This review should have "+str(res)+" star(s)")
			
			#METHODE 2 - MEILLEURE (Précision à ~0,5 étoiles)
			res=an.getBestMatch2(data,pos,neg)
			print("This review should have "+str(res)+" star(s)")
			# print("Method 2 : This review should have "+str(res)+" star(s)")
			
			#METHODE 3 - Résultats identiques à la méthode 2 (Précision à ~0,5 étoiles)
				# donc aucune influence de la méthode de calcule sur les résultats
			# res=an.getBestMatch3(data,pos,neg)
			# print("Method 3 : This review should have "+str(res)+" star(s)")	