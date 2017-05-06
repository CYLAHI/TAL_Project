#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import Analyze as an


def runTraining(folderName) :
        trainingFiles=[] #Liste des fichiers d'entrainement
        trainingData=[] #données étudiées
        pos=0
        neg=0
        
        
        for dir in os.walk(folderName):
                dir=dir[1] #get directory list
                for i,f in enumerate(dir):
                        actualFolder=os.path.join(folderName,f)
                        for files in os.walk(actualFolder):#Parcourir liste dossier dans training
                                trainingFiles.append(files[2]) 
                                for j, tf in enumerate (files[2]): #Parcourir liste des fichiers dans *star
                                        tempP,tempN=( an.analyzeFile( os.path.join(actualFolder,tf) ) )
                                        pos=(pos+tempP)/2
                                        neg=(neg+tempN)/2
                                trainingData.append([pos,neg])
        return trainingData

