import csv
from os import remove
import string
from collections import Counter
import re
from typing import Dict
import operator
def read_file():
    while True:
        filename=input('Enter the name of file to open ==> ')
        try:
            with open (filename, "r") as f:
                text=f.read()
                #print(text)
                words=text.split()
                #print(words)
                table=str.maketrans("","", string.punctuation)
                stripped=[w.translate(table) for w in words]
                #print(stripped)
                lettercount={w:len(w) for w in stripped}
                #print(lettercount)
                newdict=dict((k.lower(), v)for k, v in lettercount .items())
                #print(newdict)
        except:
            print('Could not open file',filename, "\nPlease try again")
            continue
        return newdict, stripped

def clean_words(newdict):
    finaldict={}
    for word in newdict: 
            try:
                if newdict[word]>3:
                    wdcount=newdict[word]
                    finaldict[word]=wdcount
                    #print(finaldict)
                    #finaldict=[letcount]
                    #print(finaldict)
            except newdict[word]<3:
                print("except", finaldict)
    return finaldict
        

def word_freq(finaldict,stripped):
    stripped2 = stripped
    finaldict2={}
    #print(stripped2)
    for i in range(len(stripped2)):
        stripped2[i] = stripped2[i].lower()
    #print(stripped2)
    for fd in finaldict:
        try:
            tempcnt=stripped2.count(fd)
            #fdcount=finaldict2[fd]
            #finalcount=(fd, tempcnt)
            finaldict2[fd]=tempcnt
            #print(finaldict2)
        except:
            print("Error in word_freq")
    return finaldict2

def output_freq_words(sorted_dict):
    topcount=0
    print("Most frequently used words")
    print("#        Word                      Freq.")
    print("=============================================")
    for lineword in sorted_dict:
        try:
            if topcount<10:
                topcount=topcount+1
                printfreq=sorted_dict[lineword]
                printfreq2=f"{printfreq:>20}"
                finalcount=(lineword)
                #printke=finaldict2['word']
                #printval=finaldict2[]
                #print(topcount,"    \t", finalcount, "\t\t\t", printfreq2)
                line_new = '{:<6}  {:<12}  {:>10}'.format(topcount, finalcount, printfreq2)
                print(line_new)

            else:
                pass
        except:
            pass
 
def occurs_once(finaldict2):
    onecount=0
    for fd in finaldict2:
        if finaldict2[fd]==1:
            onecount=onecount+1
        else:
            pass
    print("There are", onecount, "words that occur only once.")

def unique_words(finaldict2):
    uniquecount=len(finaldict2)
    print("There are", uniquecount, "unique words in the document.")
    return 
    


if __name__ == "__main__":
    stripped=[]
    newdict,stripped=read_file()
    #print(stripped)
    finaldict=clean_words(newdict)
    finaldict2=word_freq(finaldict, stripped)
    sorted_dict = dict( sorted(finaldict2.items(),
                           key=lambda item: item[1],
                           reverse=True))
    #print(sorted_dict)
    output_freq_words(sorted_dict)
    occurs_once(finaldict2)
    unique_words(finaldict2)
    
