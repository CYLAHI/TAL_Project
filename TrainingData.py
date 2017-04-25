#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os #allows to get all directories, files... in a folder 
import Preprocess as pp


def runTraining(folderName,language) :
	trainingFiles=[]
	ppData=[]
	trainingData={}
	
	for dir in os.walk(folderName):
		dir=dir[1] #get directory list
		for i,f in enumerate(dir):
			actualFolder=os.path.join(folderName,f)
			for files in os.walk(actualFolder):
				trainingFiles.append(files[2]) #appen files list to trainingFiles
				for i,tf in enumerate(files[2]):
					ppData.append(pp.preprocessFile( os.path.join(actualFolder,tf) ,language))   #Methode de preprocess du prof
					trainingData=pp.analyzeFile( os.path.join(actualFolder,tf) ,language)
	
	# print("Training files loaded :")
	# print(trainingFiles)
	print("Training data preprocessed")
	print(ppData)
	print("Training files analyzed")
	print(trainingData)
		
	return trainingData