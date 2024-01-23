# -*- coding: utf-8 -*-
"""
Created on Sun May  7 18:34:18 2023

@author: jimv5
"""



import pandas as pd
# Load first sheet of excel file to a data frame called df
df = pd.ExcelFile('ConsolidatedData_CarRental.xlsx').parse('Sheet1')
df = df.drop_duplicates()
#Preview Loaded file

#filters reviews with 4 and 5 stars
CarRental_Data_Pos = df.loc[(df['Rating']>=4)]
#adds reviews with 4 stars or more to list PosReviews
PosReviews = CarRental_Data_Pos['Review'].tolist()
#filters data from excel for reviews with 2 star or below
CarRental_Data_Neg = df.loc[(df['Rating']<=2)]
#adds reviews with 2 stars or less to list NegReviews
NegReviews = CarRental_Data_Neg['Review'].tolist()

#filters reviews with 4 and 5 stars in the year 2019
CarRental_Data_Pos2019 = df.loc[(df['Rating'] >= 4) & (df['Date'] >= '2019-01-01') & (df['Date']<= '2019-12-31')]
#adds reviews with 4 stars or more and in year 2019 to list PosReviews2019
PosReviews2019 = CarRental_Data_Pos2019['Review'].tolist()
#filters data from excel for reviews with 2 stars or less and in the year 2019
CarRental_Data_Neg2019 = df.loc[(df['Rating'] <= 2) & (df['Date'] >= '2019-01-01') & (df['Date']<= '2019-12-31')]
#adds reviews with 2 stars or less and in year 2019 to list NegReviews2019
NegReviews2019 = CarRental_Data_Neg2019['Review'].tolist()

#filters reviews with 4 and 5 stars in the year 2020
CarRental_Data_Pos2020 = df.loc[(df['Rating'] >= 4) & (df['Date'] >= '2020-01-01') & (df['Date']<= '2020-12-31')]
#adds reviews with 4 and 5 stars in year 2020 to list PosReviews2020
PosReviews2020 = CarRental_Data_Pos2020['Review'].tolist()
#filters data from excel for reviews with 1 or 2 stars in 2020
CarRental_Data_Neg2020 = df.loc[(df['Rating'] <= 2) & (df['Date'] >= '2020-01-01') & (df['Date']<= '2020-12-31')]
#adds reviews with 2 stars or less and in year 2020 to list NegReviews2020
NegReviews2020 = CarRental_Data_Neg2020['Review'].tolist()


#Creates a list of the lists of unprocessed data
Review_lists = [PosReviews, NegReviews, PosReviews2019, NegReviews2019, PosReviews2020, NegReviews2020]
#iterates through Review_lists to take the spaces out of all the lists within it
for x in Review_lists:
    i = 0;
    for review in x:
        if str(review) == 'nan':
            #print(i, review)
            del x[i]
        i = i+1
       
        i = 0;
        for review in x:
            if str(review) == 'nan':
                #print(i, review)
                del x[i]
            i = i+1


import OCRPreProcess
from OCRPreProcess import GroupPreProcess

import random
from random import sample
Sample_ReviewText = sample(Review_lists,10)
#our custom stopwords
custom_stpwd = ['said','would','avis','and','ask','put','els','one','budget','enterprise','enterpris','company',
                'hertz','car','need','get','go','vehicl','rent','compani','rental','vehicle',
                'us','even' 'though','one','therefor','around','avi','spoke','appear','through','my','airport']

#lists of processed text for each category
Process_Text_PosReviews = GroupPreProcess(PosReviews, custom_stpwd)
Process_Text_NegReviews = GroupPreProcess(NegReviews, custom_stpwd)
Process_Text_PosReviews2019 = GroupPreProcess(PosReviews2019, custom_stpwd)
Process_Text_NegReviews2019 = GroupPreProcess(NegReviews2019, custom_stpwd)
Process_Text_PosReviews2020 = GroupPreProcess(PosReviews2020, custom_stpwd)
Process_Text_NegReviews2020 = GroupPreProcess(NegReviews2020, custom_stpwd)

import pickle

reviews = [
    (PosReviews, 'Process_Text_PosReviews.pkl'),
    (NegReviews, 'Process_Text_NegReviews.pkl'),
    (PosReviews2019, 'Process_Text_PosReviews2019.pkl'),
    (NegReviews2019, 'Process_Text_NegReviews2019.pkl'),
    (PosReviews2020, 'Process_Text_PosReviews2020.pkl'),
    (NegReviews2020, 'Process_Text_NegReviews2020.pkl'),]

# performs text preprocssing on each item in list and stores it as a pickle file
for review, filename in reviews:
    processed_review = GroupPreProcess(review, custom_stpwd)
    with open(filename, 'wb') as f:
        pickle.dump(processed_review, f)

filenames = [
    'Process_Text_PosReviews.pkl',
    'Process_Text_NegReviews.pkl',
    'Process_Text_PosReviews2019.pkl',
    'Process_Text_NegReviews2019.pkl',
    'Process_Text_PosReviews2020.pkl',
    'Process_Text_NegReviews2020.pkl',]

processed_reviews = []
#loads each pickle file into a list processed_reviews
for filename in filenames:
    with open(filename, 'rb') as f:
        processed_review = pickle.load(f)
        processed_reviews.append(processed_review)


#Term Frequency
import OCRTermFrequency

#Plots the unigrams established using the aforementioned criteria
import seaborn as sns #imports data visualization library
import matplotlib.pyplot as plt

#print the top 20 common words in the review
PT_list = [Process_Text_PosReviews,Process_Text_PosReviews2019,Process_Text_PosReviews2020,Process_Text_NegReviews, Process_Text_NegReviews2019, Process_Text_NegReviews2020]
for item in processed_reviews:
    print(OCRTermFrequency.WordFrequency(item,20))
    print(OCRTermFrequency.BiGramFrequency(item,60))
    print(OCRTermFrequency.TriGramFrequency(item,3))


UnigramFrequency1 = OCRTermFrequency.WordFrequency(processed_reviews[4],20)
g1 = sns.barplot(x="Word", y="Frequency", data=UnigramFrequency1,edgecolor="black",linewidth=1.5,color='red')
g1.set(xlabel='Unigram', ylabel='Frequency') #labels x and y axis
g1.set_xticklabels(g1.get_xticklabels(), rotation=90) #sets the x-labels to the words and rotates it 90 degrees

UnigramFrequency2 = OCRTermFrequency.WordFrequency(Process_Text_PosReviews2019,20)
g1 = sns.barplot(x="Word", y="Frequency", data=UnigramFrequency2,edgecolor="black",linewidth=1.5,color='red')
g1.set(xlabel='Unigram', ylabel='Frequency') #labels x and y axis
g1.set_xticklabels(g1.get_xticklabels(), rotation=90) #sets the x-labels to the words and rotates it 90 degrees

UnigramFrequency3 = OCRTermFrequency.WordFrequency(Process_Text_PosReviews2020,20)
g1 = sns.barplot(x="Word", y="Frequency", data=UnigramFrequency2,edgecolor="black",linewidth=1.5,color='red')
g1.set(xlabel='Unigram', ylabel='Frequency') #labels x and y axis
g1.set_xticklabels(g1.get_xticklabels(), rotation=90) #sets the x-labels to the words and rotates it 90 degrees

UnigramFrequency4 = OCRTermFrequency.WordFrequency(Process_Text_NegReviews,20)
g1 = sns.barplot(x="Word", y="Frequency", data=UnigramFrequency2,edgecolor="black",linewidth=1.5,color='red')
g1.set(xlabel='Unigram', ylabel='Frequency') #labels x and y axis
g1.set_xticklabels(g1.get_xticklabels(), rotation=90) #sets the x-labels to the words and rotates it 90 degrees

UnigramFrequency5 = OCRTermFrequency.WordFrequency(Process_Text_NegReviews2019,20)
g1 = sns.barplot(x="Word", y="Frequency", data=UnigramFrequency2,edgecolor="black",linewidth=1.5,color='red')
g1.set(xlabel='Unigram', ylabel='Frequency') #labels x and y axis
g1.set_xticklabels(g1.get_xticklabels(), rotation=90) #sets the x-labels to the words and rotates it 90 degrees

UnigramFrequency6 = OCRTermFrequency.WordFrequency(Process_Text_NegReviews2020,20)
g1 = sns.barplot(x="Word", y="Frequency", data=UnigramFrequency2,edgecolor="black",linewidth=1.5,color='red')
g1.set(xlabel='Unigram', ylabel='Frequency') #labels x and y axis
g1.set_xticklabels(g1.get_xticklabels(), rotation=90) #sets the x-labels to the words and rotates it 90 degrees

#computes the unigrams with a frequency >=10
UnigramFrequency = OCRTermFrequency.WordFrequency(Process_Text_NegReviews2020,20)

print(UnigramFrequency[0:5])

#plots the unigrams established using aformentaioned criteria
import seaborn as sns #imports data visualization library
import matplotlib.pyplot as plt
g1 = sns.barplot(x="Word", y="Frequency", data=UnigramFrequency[0:10], edgecolor="black", linewidth=1.5,color='red')
g1.set(xlabel="Unigram", ylabel="Frequency") #Labels x and y axis
g1.set_xticklabels(g1.get_xticklabels(), rotation=90) #sets the x-labels to the words and rotates it


#computes the bigrams with a frequency >=10
BiGramFrequency, BiGramLR=OCRTermFrequency.BiGramFrequency(Process_Text_PosReviews2019,10)

print(BiGramFrequency[0:5]) #prints the top 5 bigram based on frequency

#plots the bigrams established using aformentaioned criteria
import seaborn as sns #imports data visualization library
import matplotlib.pyplot as plt
g2 = sns.barplot(x="bigram", y="freq", data=BiGramFrequency[0:10], edgecolor="black", linewidth=1.5,color='red')
g2.set(xlabel="Bigram", ylabel="Frequency") #Labels x and y axis
g2.set_xticklabels(g2.get_xticklabels(), rotation=90) #sets the x-labels to the words and rotates it

#computes the trigrams with a frequency of >= 3
TriGramFrequency, TriGramLR = OCRTermFrequency.TriGramFrequency(Process_Text_PosReviews2020,3)

print(TriGramFrequency[0:5]) #print the top 5 trigrams based on frequency

#plots the trigrams established using aformentaioned criteria
import seaborn as sns #imports data visualization library
import matplotlib.pyplot as plt
g3 = sns.barplot(x="trigram", y="freq", data=TriGramFrequency[0:10], edgecolor="black", linewidth=1.5,color='red')
g3.set(xlabel="Trigram", ylabel="Frequency") #Labels x and y axis
g3.set_xticklabels(g3.get_xticklabels(), rotation=90) #sets the x-labels to the words and rotates it