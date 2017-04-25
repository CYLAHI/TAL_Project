#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def getParagraphs(filename):
	paragraphs = []
	myFile = open(filename, "r")  #Ouverture
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

	
def normaliseEn(sent):
	sent = re.sub("\'\'", '"', sent) # two single quotes = double quotes
	sent = re.sub("[`â€˜â€™]+", r"'", sent) # normalise apostrophes/single quotes
	sent = re.sub("[â‰ªâ‰«â€œâ€]", '"', sent) # normalise double quotes
	sent = re.sub("([a-z]{3,})or", r"\1our", sent) # replace -or words with -our words (American versus British)
	sent = re.sub("([a-z]{2,})iz([eai])", r"\1is\2", sent) # replace ize with ise (-ise, -isation, -ising)
    
	return sent


def normalise(sentence, language):
	if language=="en":
		return normaliseEn(sentence)
	else:
		exit("Lang: "+str(lang)+" not recognised for tokenisation.\n")
		
		
def tokeniseEn(sentence):
    # deal with apostrophes
    sentence = re.sub("([^ ])\'", r"\1 '", sentence) #no space to left
    sentence = re.sub(" \'", r" ' ", sentence) #left space

    # separate on punctuation by first adding a space before punctuation that should not be stuck to
    # the previous word and then splitting on whitespace everywhere
    cannot_precede = ["M", "Prof", "Sgt", "Lt", "Ltd", "co", "etc", "[A-Z]", "[Ii].e", "[eE].g"] #non-exhaustive list
                                        
    # creates a regex of the form (?:(?<!M)(?<!Prof)(?<!Sgt)...), i.e. whatever follows cannot be
    # preceded by one of these words (all punctuation that is not preceded by these words is to be
    # replaced by a space plus itself
    regex_cannot_precede = "(?:(?<!"+")(?<!".join(cannot_precede)+"))" 
    
    sentence = re.sub(regex_cannot_precede+"([\.\,\;\:\)\(\"\?\!]( |$))", r" \1", sentence)

    # then restick several consecutive fullstops ... or several ?? or !! by removing the space
    # inbetween them
    sentence = re.sub("((^| )[\.\?\!]) ([\.\?\!]( |$))", r"\1\2", sentence) 

    sentence = sentence.split() # split on whitespace
    return sentence

	
def tokenise(sentence, language):
    if language=="en":
        return tokeniseEn(sentence)
    else:
        exit("Lang: "+str(lang)+" not recognised for tokenisation.\n")

def getToken(paras):
    Tokens = {}
    for para in paras:
        for sent in para:
            for tok in sent:
                if tok not in Tokens: Tokens[tok] = 0
                Tokens[tok] += 1

    return Tokens
	
	
def countToken(tokens):
	occTok = {}
	for tok in tokens:
		if tokens[tok] not in occTok: 
			occTok[tokens[tok]] = 0
		occTok[tokens[tok]] += 1
	return occTok
	
	
def preprocessFile(fileName, language):
	ppResult=[]
	filePar=getParagraphs(fileName)
	for i, par in enumerate(filePar):
		ppSentences=[]
		fileSent=getSentences(par)
		for sent in fileSent:
			sent=normalise(sent, language)
			sent=tokenise(sent, language)
			ppSentences.append(sent)
		ppResult.append(ppSentences)
	# print(ppResult)
	return(ppResult)
	
def analyzeFile(fileName, language):
	temp={}
	analyzedRes=[]
	filePara=getParagraphs(fileName)
	for i, par in enumerate(filePara):
		temp=getToken(par)
		analyzedRes.append(countToken(temp))
	# print("token")
	# print(temp)
	# print("occ token")
	# print(analyzedRes)
	return analyzedRes