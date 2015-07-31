##PYTHON SCRIPT TO PREPROCESS ENGLISH TEXT FILES FOR TEXT ANALYSIS##
##Author: Shom Mazumder##
##Date: 07/29/2015##
##Required Python Modules: nltk, langdetect##
##to do: nltk import statements not working correctly, isEnglish not catching cyrillic

#############################################################################################################################
import os
import nltk
import sys
#nltk.download() # if you dont have the following packages installed already, install them. else, comment this line out
from string import punctuation
from nltk import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from cStringIO import StringIO
from langdetect import *

#############################################################################################################################

##DEFINE FUNCTIONS##

#function that takes in a raw text file and then returns boolean whether text is english
def isEnglish(file):
    if (detect(file)=='en'):
        return True
    else:
        return False

#function that takes in a string of text and preprocesses it for text analysis
#return type: str
#to do: stem words using nltk's PorterStemmer ie processed = PorterStemmer().stem_word(processed), need to tokenize by sentence first. then stem. then string the tokens back together
def preprocess(text):
    punct = [',','.',':',';','\'','\"','(',')']
    articles = ['the','a','an','this','that','these','those','my','your','his','her','its','our','their','few','much','many','lot','most','some','any','enough','all','both','half','either','neither','each','every','other','another','such','what','rather','quite']
    prep1 = ['aboard','about','above', 'across','after','against','along','amid','among','anti']
    prep2 = ['around','as','at','before','behind','below','beneath','beside','besides','between']
    prep3 = ['beyond','but','by','concerning','considering','despite','down','during','except']
    prep4 = ['excepting','excluding','following','for','from','in','inside','into','like','minus']
    prep5 = ['near','of','off','on','onto','opposite','outside','over','past','per','plus']
    prep6 = ['regarding','round','save','since','than','through','to','toward','towards','under']
    prep7 = ['underneath','unlike','until','up','upon','versus','via','with','within','without']
    misc = ['or','and','if','else','e','u','de','l']
    num = ['0','00','1','2','3','4','5','6','7','8','9','10','125','90','11','12','13','14','15','16','17','18','19','20']
    stop =  articles + prep1 + prep2 + prep3 + prep4 + prep5 + prep6 + prep7 + num + misc

    #stop = stopwords.words('english')
    #stop = stop + punct

    processed = []
    #convert to lower-case and remove punctuation
    temp = text.lower()
    for p in punct:
        temp = temp.replace(p,"")

    #remove stop words
    processed = ' '.join([word for word in temp.split() if word not in stop])

    return processed


pwd = "" #insert present working directory
targetDir = "" #insert target directory where files will be saved

##CHANGE DIRECTORY TO WHERE THE RAW BIT TEXTS ARE LOCATED##
os.chdir(pwd)

##nltk has a method that tokenizes each sentence. look into using the nltk methods to preprocess text

##process english BITs
for raw_bit in range(1, 3461):
    bit_num = "BIT_"+str(raw_bit)+".txt"
    try:
        with open(pwd+bit_num,"r") as raw:
            raw_bit_text = raw.read()
            raw_bit_unicode = unicode(raw_bit_text,errors='ignore')
            if (isEnglish(raw_bit_unicode)):
                processed_bit = preprocess(raw_bit_text)
            ##write to new
                with open(targetDir+bit_num, "w") as processed:
                    processed.write(processed_bit)
    except Exception, e:
        print bit_num
