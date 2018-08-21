#Stemming using NLTK

import nltk
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize

def get_tokens(line):
	tokens = nltk.word_tokenize(line)
	return tokens

def do_stemming(filtered):
	stemmed = []
	for f in filtered:
		#stemmed.append(PorterStemmer().stem(f))
		#stemmed.append(LancasterStemmer().stem(f))
		stemmed.append(SnowballStemmer('english').stem(f))
	return stemmed

inFile = open('filtering.txt','r')
outFile = open('filtered3.txt','a')
for line in inFile:
    tokens = get_tokens(line)
    stemmed_tokens = do_stemming(tokens)
    #print(temp);
    outFile.write(str(stemmed_tokens));
    outFile.write('\n')
#result = dict(zip(tokens, stemmed_tokens))
#print("{tokens:stemmed} = %s") %(result)
inFile.close()
outFile.close()
