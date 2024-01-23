"""
This code will preprocess online review data.

The function PreProcess has 2 input parameters: Reviews and stopword list.

The preprocesser will do the following:
    For each review sentence:
        lowercasing
        spelling correction
        remove stop words
        remove punctuation
        remove numbers
        stems the words
    returns the preprocessed word list for each review
"""

def GroupPreProcess(Reviews, custom_stpwd, lemmatization = False):
    import nltk
    import itertools
    from nltk.tokenize import RegexpTokenizer
    from textblob import TextBlob 
    import string 
    from nltk.stem.porter import PorterStemmer
    from nltk.stem import WordNetLemmatizer #import lemmatizer
    from nltk.corpus import stopwords
    
    # Initialize tokenizers, stopwords and stemmer
    tokenizer = RegexpTokenizer(r'\w+')
    nltk_stpwd = stopwords.words('english')
    stpwd = [*nltk_stpwd, *custom_stpwd]
    p_stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer() #initialize lemmatizer
    SentTokenized_Text = []

    #intialize  list for processed text
   
    Processed_Review = []

     #Breaks reviews into sentences and also applies lowercasing
    for review in Reviews:
        SentTokenized_Text.append(nltk.sent_tokenize(review.lower()))
    
    for review in range(0,len(SentTokenized_Text)): #for each review
        Processed_Text = []
        for sentence in SentTokenized_Text[review]: #for each sentece in a review
            text = str(sentence)
            correct_sentence = TextBlob(text).correct()
            new_sentence = str(correct_sentence) #correct spelling errors 
            words = tokenizer.tokenize(new_sentence) #splits sentence into words
            stpwd_free_sent = [word for word in words if not word in stpwd] #removes stopwords in each setence
            punc_free_sent = [word for word in stpwd_free_sent if not word in string.punctuation] #removes punctuation in each setence
            num_free_sent = [word for word in punc_free_sent if word.isalpha()] #removes numbers from text
            if lemmatization == False:
                stemmed_sent = [p_stemmer.stem(word) for word in num_free_sent] #stems word in each setence
            if lemmatization == True:
                stemmed_sent = [lemmatizer.lemmatize(word) for word in num_free_sent] #lemmatize word in each sentence
            Processed_Text.append(stemmed_sent)
        Processed_Review.append(list(itertools.chain.from_iterable(Processed_Text)))
            
    return(Processed_Review)

def SentPreProcess(review, custom_stpwd, lemmatization = False):
    import nltk
    from nltk.tokenize import RegexpTokenizer
    from textblob import TextBlob 
    import string 
    from nltk.stem.porter import PorterStemmer
    from nltk.stem import WordNetLemmatizer #import lemmatizer
    from nltk.corpus import stopwords
    
    # Initialize tokenizers, stopwords and stemmer
    tokenizer = RegexpTokenizer(r'\w+')
    nltk_stpwd = stopwords.words('english')
    stpwd = [*nltk_stpwd, *custom_stpwd]
    p_stemmer = PorterStemmer()
    SentTokenized_Text = []
    lemmatizer = WordNetLemmatizer() #initialize lemmatizer
    
        #intialize  list for processed text
    Processed_Text = []
    SentTokenized_Text.append(nltk.sent_tokenize(review.lower()))
    
    for sentence in SentTokenized_Text: #for each sentece in a review
        text = str(sentence)
        correct_sentence = TextBlob(text).correct()
        new_sentence = str(correct_sentence) #correct spelling errors 
        words = tokenizer.tokenize(new_sentence) #splits sentence into words
        stpwd_free_sent = [word for word in words if not word in stpwd] #removes stopwords in each setence
        punc_free_sent = [word for word in stpwd_free_sent if not word in string.punctuation] #removes punctuation in each setence
        num_free_sent = [word for word in punc_free_sent if word.isalpha()] #removes numbers from text
        if lemmatization == False:
            stemmed_sent = [p_stemmer.stem(word) for word in num_free_sent] #stems word in each setence
        if lemmatization == True:
            stemmed_sent = [lemmatizer.lemmatize(word) for word in num_free_sent] #stems word in each setence
        Processed_Text.append(stemmed_sent)
        
    return(Processed_Text)

