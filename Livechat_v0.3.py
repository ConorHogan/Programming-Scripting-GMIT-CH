#Attempt at combined stopword removal and then count of keywords + write to csv


file_name = input('Enter file name to process: ') #select Livechat export file
listostops = input('Enter stopword file name: ') #select list of stops file
outputfile = input('Output file name: ') #select file to send output too
import pandas as pd
xl_workbook = pd.ExcelFile(file_name)  # Load the excel workbook
df = xl_workbook.parse('Sheet1')  # Parse the sheet into a panda dataframe
QList = df['Question'].tolist()  # Select the desired column transform into a python list
Keywordlist = str(QList) #convert list into string

import re # this is importing the regular expression module
Zeropunc = re.sub(r'[^\w\s]','',Keywordlist) #remove punctuation using regex, but converts all ' to 39 which i assume is the unicode or something

cut39 = Zeropunc.replace("39", "") # removes the 39 that had been inserted in place ' above

splitcut = cut39.split() # splits the string to individual string for comparison with stopwords
stopwords = open(listostops, 'r').read().split() # imports my stopword list and splits

cleansedstring = [t for t in splitcut if t.lower() not in stopwords] #compares and removes

from collections import Counter # COUNTER SECTIONS BEGINS

counts = Counter(cleansedstring)

livechat = str (counts)
cleansedchat = livechat.replace("'", "")
print(cleansedchat)

with open(outputfile, 'w') as f: #WRITE SECTION - you need to provide a file
    for line in cleansedchat:
        f.write(line)
