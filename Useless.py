from nltk.corpus import wordnet

posAdj=["impressive","good","terrific","amazing","performing","powerful","efficient","successful","well trained"]
negAdj=["horrible","bad","noisy","impossible","awkward","defective","stupid","terrible"]

#~ def getMinimalList(adjList):
        #~ for i,adj in enumerate(adjList):
                #~ if (synset(adj) in adjList) :
                        #~ adjList.remove(adj)
        #~ return adjList
        

#~ def getAllSynForList(wordList):
        #~ res=wordList
        #~ for word in (wordlist):
                #~ for synset in wn.synsets(word):
                        #~ for lemma in synset.lemmas():
                                #~ if(lemma.name() not in wordList):
                                        #~ wordList.append(lemma.name())
                                                                
        #~ return wordList
                        

# def getSynFromWord(word,p):
	# print("WORD",word)
	# res=[]
	# for synset in wn.synsets(word,pos=p):
		# for lemma in synset.lemmas():
			# print("SYN :",lemma.name())
			# if(lemma.name() in res is False):
				# res.append( lemma.name())
			# else:
				# continue
	# return res

# def getSynFromList(l,p):
	# res=l
	# for i in l:
		# temp=getSynFromWord(i,p)
		# for j in temp:
			# res.append(j)
	# return res
	
DEF GETpOSaNDnEG

	# for j in adj: #for all got adj
		# for z,v in enumerate(adv): 
			# if( wordInList(v, negList) is True ):
				# isNeg=True
				# print("ADV",v)
				# adv.remove(v)
		# for y,p in enumerate(posAdj): #on compare la liste des adj à celle des adjPos qu'on a créée
			# # if(wordInList(j,getSynFromList(p,wn.ADJ)) is True and isNeg is False):
			# print("Pos",j)
				# pos=pos+1
			# #~ if(j in getSynFromList(p) and isNeg is True): #S'il y a un adv negatif avec l'adj pos, on compte comme neg
			# if(wordInList(j,getSynFromList(p,wn.ADJ)) is True and isNeg is False):
				# print("neg",j)
				# neg=neg+1
				# isNeg=False
		# for x, n in enumerate(negAdj): #Idem avec les adj negatifs
			# #~ if(j in getSynFromList(n) and isNeg is False):
			# if(wordInList(j,getSynFromList(n,wn.ADJ)) is True and isNeg is False):
				# print("neg",j)
				# neg=neg++1
			# #~ if(j in getSynFromList(n) and isNeg is True):
			# if(wordInList(j,getSynFromList(n,wn.ADJ)) is True and isNeg is False):
				# print("pos",j)
				# pos=pos+1
				# isNeg=False
	# for j in verb:  
		# for y,p in enumerate(posVerb): #on compare la liste des adj à celle des adjPos qu'on a créée
			# #~ if(j in getSynFromList(p) and isNeg is False): #s'il n'y a pas de négation avec l'adj, il est bien positif
			# if(wordInList(j,getSynFromList(p,wn.VERB)) is True and isNeg is False):
				# print("pos",j)
				# pos=pos+1
			# #~ if(j in getSynFromList(p) and isNeg is True): #S'il y a un adv negatif avec l'adj pos, on compte comme neg
			# if(wordInList(j,getSynFromList(p,wn.VERB)) is True and isNeg is False):
				# print("neg",j)
				# neg=neg+1
				# isNeg=False
		# for x, n in enumerate(negVerb): #Idem avec les adj negatifs
			# #~ if(j in getSynFromList(n) and isNeg is False):
			# if(wordInList(j,getSynFromList(n,wn.VERB)) is True and isNeg is False):
				# print("neg",j)
				# neg=neg++1
			# #~ if(j in getSynFromList(n) and isNeg is True):
			# if(wordInList(j,getSynFromList(n,wn.VERB)) is True and isNeg is False):
				# print("pos",j)
				# pos=pos+1
				# isNeg=False

				

# def getBestMatch3(data,pos,neg):		
	# res=[]
	# mid=int( len(data)/2)
	# for star,dat in enumerate(data) :
		# temp=(dat[0]-pos + dat[1]-neg )/2
		# res.append(temp)
	# m=100000
	# if(pos>=neg):
		# for i in range(mid,len(data)-1):
			# m=min(m,res[i])
	# if(neg>pos):
		# for i in range(0,mid-1):
			# m=min(m,res[i])
	# for star, dat in enumerate(res):
		# if(dat==m):	
			# temp=star+1
	# print(" STAR :",temp)
	# return temp
	
# def getBestMatch5(data,pos,neg):		
	# res=[]
	# mid=int( len(data)/2)
	
	# if(pos>=neg):
		# for star,dat in enumerate(data) :
			# temp=dat[0]-pos
			# res.append(temp)
		# temp = min(float(s) for s in res)
		# for star, dat in enumerate(res):
			# if dat==temp:
				# return star+1
		# return temp		
		
	# if(neg>pos):
		# for star,dat in enumerate(data) :
			# temp=dat[1]-neg
			# res.append(temp)
		# temp = min(float(s) for s in res)
		# for star, dat in enumerate(res):
			# if dat==temp:
				# return star+1
		# return temp


		
# def getAdj(taggedList):
        # adjs=[]
        # for tag in taggedList:
                # if(tag[1]=='JJ'):
                        # adjs.append(tag[0])
        # return adjs

# def getVerb(taggedList):
        # verbs=[]
        # for tag in taggedList:
                # if(tag[1]=='VERB'):
                        # verbs.append(tag[0])
        # return verbs
        
# def getAdv(taggedList):
        # advs=[]
        # for i, tag in enumerate(taggedList):
                # if(tag[1]=='RB'):
                        # advs.append(tag[0])
        # return advs

	
# def getMinimalList(l):
	# res=[]
	# for word in l:
		# if word in res:
			# continue
		# else:
			# res+=word
	# return res
		
		
# def wordInList(word,li):
	# for w in li :
		# if word==str(w):
			# return True
		# else:
			# return False