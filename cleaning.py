#Cleaning the tweet text to remove useless symbols

import sys
import os
import re
import string

def clean(inputDir, outputFile):

    # print("Cleaning "+path)

    WRITE_HANDLER = open(outputFile, 'wb')
    tweets = dict()
    for line in open(inputDir + './myTweetsFile.json','rb'):
        # print "Before" + line
        line = re.sub(r'[.,"!]+', '', line, flags=re.MULTILINE)  # removes the characters specified
        line = re.sub(r'^RT[\s]+', '', line, flags=re.MULTILINE)  # removes RT
        line = re.sub(r'https?:\/\/.*[\r\n]*', '', line, flags=re.MULTILINE)  # remove link
        line = re.sub(r'[:]+', '', line, flags=re.MULTILINE)
        line = filter(lambda x: x in string.printable, line)  # filter non-ascii characers

        new_line = ''
        for i in line.split():  # remove @ and #words, punctuataion
            if not i.startswith('@') and not i.startswith('#') and i not in string.punctuation:
                new_line += i + ' '
        line = new_line

        # # Do sentence correction

        if new_line in tweets:
            continue
        else:
            tweets[new_line] = 1
        if len(new_line.strip()) > 0:
            #print  "Writing new line"
            WRITE_HANDLER.write(new_line + '''''')
    return outputFile


DATA_FOLDER = sys.argv[1]
CLEANED_DATA = sys.argv[2]
clean(DATA_FOLDER, CLEANED_DATA)
