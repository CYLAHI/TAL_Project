#~ #!/usr/bin/env python
#~ # -*- coding: utf-8 -*-

import Preprocess as pp
from nltk.corpus import wordnet as wn
import nltk

#Listes exhaustives de mots positifs/négatifs et de négation
posAdj=["impressive","good","terrific","amazing","performing","powerful","efficient","successful","well trained","lightweight","fast","awesome","cool","intuitive","legible","beautiful","productive"]
negAdj=["horrible","bad","noisy","impossible","awkward","defective","stupid","terrible","heavy","despicable","boring","broken","slow","illegible","annoying"]
posVerb=["love","like"]
negVerb=["hate","dislike","suck","annoy","turn off","lag","lagg","die"]
negationList=["not","non"]	
		
#Est-ce que le mot word a un synonyme dans la liste l pour une nature p (ADJ, VERB, ...)
def isSyn(word,l,p): 
	for w in l:
		for synset in wn.synsets(w,pos=p): #recherche des synonymes de w ayant p pour nature
			for lemma in synset.lemmas():
				if(str(word)==str(lemma.name())): #Synonyme trouvé
					return True
				else:
					continue
	return False

# Attribut les points positifs / négatifs pour taggedChunk
def getPosAndNeg(taggedChunk):
	pos=0   #nb de mots considérés positifs
	neg=0   #nb de mots considérés négatifs
	isNeg=False #boolean for negation in chunk

	
	for tag in taggedChunk:
	
		if(tag[1]=='RB'): #On vérifie la présence qu'une négation
			if( isSyn(tag[0],negationList,wn.ADV) ):
				isNeg=True
			else:
				isNeg=False
				continue
		elif(tag[1]=='VERB' or tag[1]=='VBP' or tag[1]=='VBZ' or tag[1]=='VBG' or tag[1]=='VBN'):
			if ( isSyn(tag[0],posVerb,wn.VERB) is True ):
				if(isNeg is False) :
					pos+=1
				else : #isNeg True
					neg+=1
					isNeg=False #on remet  à False car cette négation a été attribuée
			elif ( isSyn(tag[0],negVerb,wn.VERB) is True ):
				if(isNeg is False) :
					neg+=1
				else : #isNeg True
					pos+=1
					isNeg=False#on remet isNeg à False car on vient de l'attribué
			else:
				continue	
		#IDEM pour les ADJ
		elif(tag[1]=='JJ' or tag[1]=='ADJ'):
			if ( isSyn(tag[0],posAdj,wn.ADJ) is True ):
				if(isNeg is False):
					pos+=1
				else : #is Neg True
					isNeg=False
					neg+=1
			elif ( isSyn(tag[0],negAdj,wn.ADJ) is True ):
				if(isNeg is False) :
					neg+=1
				else : #is Neg True
					pos+=1
					isNeg=False
			else:
				continue
		else: #Il ne s'agit pas d'un mot important
			isNeg=False
			continue
	return (pos,neg)
				

def analyzeFile(filename):
	pos=0.0
	neg=0.0
										
	par=pp.getParagraphs(filename) 
	for pa in par: #Pour charque paragraphe du fichier...
		sent=pp.getSentences(pa) 
		for s in sent: #...pour chaque phrase d'un paragraphe...
			chunk=pp.getChunk(s)  
			for k,ch in enumerate(chunk): # ... on tag chaque chunk 
				tokChunk=nltk.tokenize.word_tokenize(ch)
				tagChunk=nltk.pos_tag(tokChunk)
				tempP,tempN=getPosAndNeg(tagChunk) #On récupère les points positifs et négatifs pour chaque chunk
				pos+=tempP   #on fait le compte
				neg+=tempN
	nbWords=pp.countWords(filename) #On récupère le nombre total de mots dans le fichier
	
	#On calcule le pourcentage de mots considérés positifs/négatifs
	pos=pos*100/nbWords
	neg=neg*100/nbWords
	
	return pos,neg

	
	
# def getBestMatch1(data,pos,neg):
	# res=[]
	# for star,dat in enumerate(data) :
		# temp=( max((dat[0],pos)) - min((dat[0],pos) ) + max((dat[1],neg)) - min((dat[1],neg)) )/2
		# res.append(temp)
	# temp = min(float(s) for s in res)
	# for star, dat in enumerate(res):
		# if dat==temp:
			# return star+1

	
def getBestMatch2(data,pos,neg):		
	res=[]
	mid=int( len(data)/2)
	
	for star,dat in enumerate(data) :
		temp=(dat[0]-pos + dat[1]-neg )/2
		res.append(temp)
		
	m=1000000.0
	if(pos>=neg):
		for i in range(mid,len(data)):
			m=min(m,res[i])
		for i in range (mid,len(data)+1):
			if(float(res[i])==float(m)):
				return i+1
		else :
			print("Erreur")
			return 0
			
	if(neg>pos):
		for i in range(0,mid-1):
			m=min(m,res[i])
		for i in range (0,mid-1):
			if(res[i]==m):
				return i+1	
		else :
			print("Erreur")
			return 0

	
# def getBestMatch3(data,pos,neg):		
	# res=[]
	# mid=int( len(data)/2)
	
	# m=1000000.0
	# if(pos>=neg):
		# for star,dat in enumerate(data) :
			# temp=(dat[0]-pos)
			# res.append(temp)
		# for i in range(mid,len(data)-1):
			# m=min(m,res[i])
		# for i in range (mid,len(data)-1):
			# if(res[i]==m):
				# return i+1
		# else :
			# print("Erreur")
			# return 0
			
	# if(neg>pos):
		# for star,dat in enumerate(data) :
			# temp=(dat[1]-neg)
			# res.append(temp)
		# for i in range(0,mid-1):
			# m=min(m,res[i])
		# for i in range (0,mid-1):
			# if(res[i]==m):
				# return i+1
		# else :
			# print("Erreur")
			# return 0

