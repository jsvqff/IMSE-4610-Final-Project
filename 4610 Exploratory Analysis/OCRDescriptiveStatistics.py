#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 22:37:05 2021

@author: Sharan
"""

#Counts the number of sentences and words in each review
def SentWordCount(review):
    import nltk
#    nltk.download('punkt')
    from nltk.tokenize import sent_tokenize    
    sent_per_review = len(sent_tokenize(review)) #total sentences per review
    wordcount_review = 0
    for sentence in (sent_tokenize(review)): #for each sentece in a review
        words = sentence.split() #splits sentence into words
        wordcount_review =  wordcount_review + len(words) # computes the number of words in each review
    
    return(sent_per_review, wordcount_review)


#Descriptive Statistics - Returns the mean, median, range, and readability scrores of ALL review sentences
def DS_Sentences(Review_Text): #input is all reviews
    import nltk
    from nltk.tokenize import sent_tokenize 
    import numpy as np
    import statistics

    SentTokenized_Text = []
    

    #Breaks reviews into sentences and also applies lowercasing
    for review in Review_Text:
        SentTokenized_Text.append(nltk.sent_tokenize(review.lower()))
    
    sent_per_review = []
    words_per_sent = []
    words_per_review = []
    for review in range(0,len(SentTokenized_Text)): #for each review 
        sent_per_review.append(len(SentTokenized_Text[review])) #total sentences per review
        wordcount_review = 0
        for sentence in SentTokenized_Text[review]: #for each sentece in a review
            words = sentence.split() #splits sentence into words
            
            wordcount_review =  wordcount_review + len(words) # computes the number of words in each review
            words_per_sent.append(len(words)) #computes sum of words per sentence
        words_per_review.append(wordcount_review) #computes total words per review
        
    #Sentence-level averages
    AvgSentencesPerReview = statistics.mean(sent_per_review) #average sentence count across all reviews
    
    SDSentencesPerReview = statistics.stdev(sent_per_review)
    
    MinSentencesPerReview = min(sent_per_review) #average sentence count across all reviews
    
    MaxSentencesPerReview = max(sent_per_review) #average sentence count across all reviews    
    
    Q1SentencesPerReview = np.percentile(sent_per_review, 25)

    Q3SentencesPerReview = np.percentile(sent_per_review, 75)  
    
    return(MinSentencesPerReview, Q1SentencesPerReview, AvgSentencesPerReview, SDSentencesPerReview, Q3SentencesPerReview, MaxSentencesPerReview)

def DS_Words(Review_Text): #input is all reviews
    import nltk
    import numpy as np
    import statistics

    SentTokenized_Text = []
    

    #Breaks reviews into sentences and also applies lowercasing
    for review in Review_Text:
        SentTokenized_Text.append(nltk.sent_tokenize(review.lower()))
    
    sent_per_review = []
    words_per_sent = []
    words_per_review = []
    for review in range(0,len(SentTokenized_Text)): #for each review 
        sent_per_review.append(len(SentTokenized_Text[review])) #total sentences per review
        wordcount_review = 0
        for sentence in SentTokenized_Text[review]: #for each sentece in a review
            words = sentence.split() #splits sentence into words
            
            wordcount_review =  wordcount_review + len(words) # computes the number of words in each review
            words_per_sent.append(len(words)) #computes sum of words per sentence
        words_per_review.append(wordcount_review) #computes total words per review
    
    #Word-level averages across all sentences
    AvgWordsPerReview = statistics.mean(words_per_review) #overall average word count across all reviews
   
    SDWordsPerReview = statistics.stdev(words_per_review)
    
    MinWordsPerReview = min(words_per_review)
    
    MaxWordsPerReview = max(words_per_review)
    
    Q1SentencesPerReview = np.percentile(words_per_review, 25)

    Q3SentencesPerReview = np.percentile(words_per_review, 75)  
   
    return(MinWordsPerReview, Q1SentencesPerReview, AvgWordsPerReview, SDWordsPerReview, Q3SentencesPerReview, MaxWordsPerReview)    

     
def ReadabilityScore(review): #input is each review
    import syllapy
    import nltk
    sylcount_review = 0;
    for sentence in (nltk.sent_tokenize(review)): #for each sentece in a review
        sylcount_sentence = 0 #initlize syllble count to 0 for this sentence in this review
        words = sentence.split() #splits sentence into words
        for word in words: #for each word in the sentence
            sylcount_sentence =  sylcount_sentence + syllapy.count(word) # compute the number of syllables in each word of that sentence and sum it
        sylcount_review = sylcount_review + sylcount_sentence
        
    sent_per_review,  words_per_review = SentWordCount(review)
    readabilityScore = 206.835 - 1.015*(words_per_review/sent_per_review) - 84.6*(sylcount_review/words_per_review)
    return(readabilityScore)

