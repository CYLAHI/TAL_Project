#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import TrainingData as td

if __name__ == "__main__":
	argparser = argparse.ArgumentParser()
	argparser.add_argument("-l","--language", help="Language used. en for English")
	argparser.add_argument("-fo","--folderName", help="Folder with training examples")
	argparser.add_argument("-fi","--fileName", help="File to analyze")
	args=argparser.parse_args()

	print("Analyzing training files")
	td.runTraining(args.folderName,args.language)
	if args.fileName:
		print("Analyzing unknown file")
		#To-DO
		
		
	

