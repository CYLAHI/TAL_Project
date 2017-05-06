#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import nltk.data

def getParagraphs(filename):
        paragraphs = []
        myFile = open(filename, "r")  #Opening
        with myFile as filepointer:
                for line in filepointer.readlines():
                        if line.strip()=="": continue # ignore blank paragraphs
                        paragraphs.append(line.strip()) # remove whitespace with strip()
        return paragraphs
		
        
def getSentences(paragraph):
    cannot_precede = ["M", "Prof", "Sgt", "Lt", "Ltd", "co", "etc", "[A-Z]", "[Ii].e", "[eE].g"] # non-exhaustive list
    regex_cannot_precede = "(?:(?<!"+")(?<!".join(cannot_precede)+"))"
    
    if "\n" in paragraph: 
                exit("Error in paragraph: paragraph contains \n.")       
    newline_separated = re.sub(regex_cannot_precede+"([\.\!\?]+([\'\’\"\)]*( |$)| [\'\’\"\) ]*))", r"\1\n", paragraph)
    sentences = newline_separated.strip().split("\n")
    for i, s in enumerate(sentences):
        sentences[i] = s.strip()
    return sentences    

#Chunk désigne un morceau de phrase. Ici déterminés par la présence ou non de ponctuation 	
def getChunk(sentence):
        chunks=[]
        chunks=re.split(',|;|:',sentence) #liste exhaustive
        return chunks
        
		
def countWords(filename):
        temp=[]
        sent=[]
        res=0
        
        par=getParagraphs(filename)
        for p in par:
                sent=getSentences(p)
                for s in sent:
                        temp=re.split(" ",s)
                        res=res+len(temp)
        return res
                        
        
def tagFile(filename):
        par=[]
        sent=[]
        tokFile=[]
        taggedFile=[]
        
        par=getParagraphs(filename)
        for i,par in enumerate(par):
                sent=getSentences(par)
                for j,s in enumerate(sent):
                        tokFile.append(nltk.tokenize.word_tokenize(s))
        for i, tok in enumerate(tokFile):
                taggedFile.append(nltk.pos_tag(tok))

        return taggedFile
