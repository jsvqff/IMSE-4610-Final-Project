# -*- coding: utf-8 -*-
"""
Created on Sun May  7 20:48:27 2023

@author: jimv5
"""
import pandas as pd
# Load first sheet of excel file to a data frame called df
df = pd.ExcelFile('ConsolidatedData_CarRental.xlsx').parse('Sheet1')
df = df.drop_duplicates()

Review_Text = df['Review'].tolist()

i = 0;
for review in Review_Text:
    if str(review) == 'nan':
        del Review_Text[i]
        
        i = i+1
        
    i = 0;
    for review in Review_Text:
        if str(review) == 'nan':
            del Review_Text[i]
            
            i = i+1
        
import OCRPreProcess
from OCRPreProcess import GroupPreProcess
        
custom_stpwd = ['said','would','avis','and','ask','put','els','one','budget','enterprise','enterpris','company',
                'hertz','car','need','get','go','vehicl','rent','compani','rental','vehicle',
                'us','even' 'though','one','therefor','around','avi','spoke','appear','through','my','airport']

Processed_Text = GroupPreProcess(Review_Text, custom_stpwd)

import random
from random import sample

import OCRTermFrequency

#computes the unigrams with a frequency >=10
UnigramFrequency = OCRTermFrequency.WordFrequency(Processed_Text,20)

print(UnigramFrequency[0:5])

#plots the unigrams established using aformentaioned criteria
import seaborn as sns #imports data visualization library
import matplotlib.pyplot as plt
g1 = sns.barplot(x="Word", y="Frequency", data=UnigramFrequency[0:10], edgecolor="black", linewidth=1.5,color='red')
g1.set(xlabel="Unigram", ylabel="Frequency") #Labels x and y axis
g1.set_xticklabels(g1.get_xticklabels(), rotation=90) #sets the x-labels to the words and rotates it


#computes the bigrams with a frequency >=10
BiGramFrequency, BiGramLR=OCRTermFrequency.BiGramFrequency(Processed_Text,10)

print(BiGramFrequency[0:5]) #prints the top 5 bigram based on frequency

#plots the bigrams established using aformentaioned criteria
import seaborn as sns #imports data visualization library
import matplotlib.pyplot as plt
g2 = sns.barplot(x="bigram", y="freq", data=BiGramFrequency[0:10], edgecolor="black", linewidth=1.5,color='red')
g2.set(xlabel="Bigram", ylabel="Frequency") #Labels x and y axis
g2.set_xticklabels(g2.get_xticklabels(), rotation=90) #sets the x-labels to the words and rotates it

#computes the trigrams with a frequency of >= 3
TriGramFrequency, TriGramLR = OCRTermFrequency.TriGramFrequency(Processed_Text,3)

print(TriGramFrequency[0:5]) #print the top 5 trigrams based on frequency

#plots the trigrams established using aformentaioned criteria
import seaborn as sns #imports data visualization library
import matplotlib.pyplot as plt
g3 = sns.barplot(x="trigram", y="freq", data=TriGramFrequency[0:10], edgecolor="black", linewidth=1.5,color='red')
g3.set(xlabel="Trigram", ylabel="Frequency") #Labels x and y axis
g3.set_xticklabels(g3.get_xticklabels(), rotation=90) #sets the x-labels to the words and rotates it