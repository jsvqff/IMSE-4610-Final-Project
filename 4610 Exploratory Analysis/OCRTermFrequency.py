#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 14:19:58 2021

@author: Sharan
"""

def WordFrequency(Processed_Text, N):
    import pandas as pd
    from collections import Counter
    import itertools
    word_list = list(itertools.chain.from_iterable(Processed_Text)) #Converts pre-processed list
    word_frequency = Counter(word_list) #Computes the frequency of the words
    top_words = pd.DataFrame(word_frequency.most_common(N),columns=['Word','Frequency']);
    return(top_words)

def BiGramFrequency(Processed_Text, Filter):
    import nltk
    import pandas as pd
    import itertools
    
    word_list = list(itertools.chain.from_iterable(Processed_Text)) #Converts pre-processed list

    bigram_measures = nltk.collocations.BigramAssocMeasures() #imports collection of measures for bigram association
    
    #Finds bigram from the sequence of words in word_list
    bigramFinder = nltk.collocations.BigramCollocationFinder.from_words(word_list) 
    
    #Applies a fiter to find bigrams with frequency >= Filter
    bigramFinder.apply_freq_filter(Filter)
    
    #Computes the frequency of each bigram
    bigram_freq = bigramFinder.ngram_fd.items()
    
    #creates a bigram frequency data as a pandas data frame
    bigramFreqTable = pd.DataFrame(list(bigram_freq), columns=['bigram','freq']).sort_values(by='freq', ascending=False)
    
    bigramPMITable = pd.DataFrame(list(bigramFinder.score_ngrams(bigram_measures.likelihood_ratio)), columns=['bigram','LR']).sort_values(by='LR', ascending=False)
   
   
    return(bigramFreqTable, bigramPMITable)

def TriGramFrequency(Processed_Text, Filter):
    import nltk
    import pandas as pd
    import itertools
    
    word_list = list(itertools.chain.from_iterable(Processed_Text)) #Converts pre-processed list

    trigram_measures = nltk.collocations.TrigramAssocMeasures() #imports collection of measures for bigram association

    #Finds trigram from the sequence of words in word_list
    trigramFinder = nltk.collocations.TrigramCollocationFinder.from_words(word_list) 
    
    #Applies a fiter to find trigrams with frequency >= 2
    trigramFinder.apply_freq_filter(Filter)
    
    #Computes the frequency of each trigram
    trigram_freq = trigramFinder.ngram_fd.items()
    
    
    trigramFreqTable = pd.DataFrame(list(trigram_freq), columns=['trigram','freq']).sort_values(by='freq', ascending=False)
    
    trigramPMITable = pd.DataFrame(list(trigramFinder.score_ngrams(trigram_measures.likelihood_ratio)), columns=['trigram','LR']).sort_values(by='LR', ascending=False)
   
   
    return(trigramFreqTable, trigramPMITable)