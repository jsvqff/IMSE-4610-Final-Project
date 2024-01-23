# -*- coding: utf-8 -*-
"""
Created on Sun May  7 21:09:21 2023

@author: jimv5
"""

CarRental_Data_Pos = df.loc[(df['Rating']>=4)]
PosReviews = CarRental_Data_Pos['Review'].tolist()

CarRental_Data_Neg = df.loc[(df['Rating']<=2)]
NegReviews = CarRental_Data_Neg['Review'].tolist()

#Filter 4 and 5 star reviews from 2019
CarRental_Data_Pos2019 = df.loc[(df['Rating'] >= 4) & (df['Date'] >= '2019-01-01') & (df['Date'] <= '2019-12-31')]
PosReviews2019 = CarRental_Data_Pos2019['Review'].tolist()

#Filter 1 and 2 star reviews from 2019
CarRental_Data_Neg2019 = df.loc[(df['Rating'] <= 2) & (df['Date'] >= '2019-01-01') & (df['Date'] <= '2019-12-31')]
NegReviews2019 = CarRental_Data_Neg2019['Review'].tolist()

#Filter 4 and 5 star reviews from 2020
CarRental_Data_Pos2020 = df.loc[(df['Rating'] >= 4) & (df['Date'] >= '2020-01-01') & (df['Date'] <= '2020-12-31')]
PosReviews2019 = CarRental_Data_Pos2020['Review'].tolist()

#Filter 1 and 2 star reviews from 2020
CarRental_Data_Neg2020 = df.loc[(df['Rating'] <= 2) & (df['Date'] >= '2020-01-01') & (df['Date'] <= '2020-12-31')]
NegReviews2019 = CarRental_Data_Neg2020['Review'].tolist()



UnigramFrequency = OCRTermFrequency.WordFrequency(Processed_Text,20)

print(UnigramFrequency)

#plots the unigrams established using aformentaioned criteria
import seaborn as sns #imports data visualization library
import matplotlib.pyplot as plt
g1 = sns.barplot(x="Word", y="Frequency", data=UnigramFrequency, edgecolor="black", linewidth=1.5,color='red')
g1.set(xlabel="Unigram", ylabel="Frequency") #Labels x and y axis
g1.set_xticklabels(g1.get_xticklabels(), rotation=90) #sets the x-labels to the words and rotates it


#computes the bigrams with a frequency >=10
BiGramFrequency, BiGramLR=OCRTermFrequency.BiGramFrequency(Processed_Text,10)

print(BiGramFrequency[0:5]) #prints the top 5 bigram based on frequency 

print(BiGramLR[0:5])

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
g3.set_xticklabels(g3.get_xticklabels(), rotation=90) #sets the x-labels to the words and r it