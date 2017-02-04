"""
Name : Mohd. Kashif
Roll No. MT15035
Question No. 3
"""

from stemming.porter2 import stem
from nltk.corpus import stopwords
import string
import csv

def remove_nonascii(text):
	ans = ""
	text.lower()
	for x in text:
		if (ord(x)>=97 or ord(x)<=122) and (ord(x)<48 or ord(x)>57) and ord(x)<128:
			ans+=x
	return ans

def remove_stopwords(text):
	stops = stopwords.words("english")
	text = ' '.join([word for word in text.split() if word not in stops])
	return text

def remove_punt(text):
	return text.translate(string.maketrans("",""), string.punctuation)

def create_invIndex(doc_name,index,doc_id):
	doc = open(doc_name,"r")
	lines = doc.readlines()
	inp=""
	line = ""
	pos={}
	lno = 1
	for inp in lines:
		inp = str(inp)
		inp = inp.lower()
		inp= remove_punt(inp)
		inp = remove_nonascii(inp)
		inp = remove_stopwords(inp)
		"""
		pos[x]=list , here "list" contains all line numbers where  'x' appears in a document .
		"""
		for x in inp.split(' '):
			if x in pos.keys():
				pos[x].append(lno)
			else:
				pos[x]=[lno]
		lno+=1
		line+=str(inp)+" "
	
	"""
	inp = stem(inp)
	"""
	"""
	Store the line numbers based on the document ids .
	"""
	for x in line.split(' '):
		if x in index.keys():
			tlist = {}
			tlist[doc_id]=pos[x]
			if doc_id not in index[x].keys():
				index[x][doc_id]=pos[x]

		else:
			tlist = {}
			tlist[doc_id]=pos[x]
			index[x]=tlist
		
	return index
	

def main():
	index ={}
	max_line = 0
	for x in range(1,2):
		print "Reading document "+str(x)+ " please wait ."
		index = create_invIndex("text"+str(x)+".txt",index,x)
		max_line = len(open("text"+str(x)+".txt","r").readlines())
		"""
		print index
		"""
	index.pop('', None)
	w = csv.writer(open("inv_index.csv", "w"))
	for key, val in index.items():
		w.writerow([key, val])
	print "\nInverted index created succesfully and stored in inv_index.csv\n"
	

	print "Enter phrase to be searched "
	phrase = raw_input()
	phrase = phrase.lower()
	"""
	Create individual sets for each word in the phrase
	Individual is dictionary where key = word to be searched and value = doc_id where key appears
	"""
	individual ={}
	for x in phrase.split(' '):
		if x not in index.keys():
			print "\n\""+ x +"\" is not found in inverted index .\n Exiting the program"
			return
		individual[x]=index[x]
	individual_docs =[1,2,3,4,5]
	for x in individual.keys():
		individual_docs= set(individual_docs).intersection(set(individual[x]))
	
	"""
	Perform intersection of all the results.
	"""
	lines = list(range(1, max_line)) 
	for x in individual_docs:
		for y in phrase.split(' '):
			lines = set(lines).intersection(index[y][x])
		if len(lines)==0:
			continue

		print "\n\nPhrase found in Document: "+ str(x) + " Line Number : ",
		for ans in lines:
			print ans,

if __name__ == '__main__':
	main()





