#Removing all punctuation marks from tweets

import re
inFile= open('filtered2.txt','r')
outFile= open('filtering.txt','a')

for line in inFile:
    #clean = re.sub(r"[.,''[]!]+", '', line,0, flags=re.MULTILINE)
    clean = re.sub(r'[^\w\s]',' ',line)
    #clean=line.split()
    print(str(clean))
    outFile.write(str(clean))
    #outFile.write('\n')
    
inFile.close()
outFile.close()
