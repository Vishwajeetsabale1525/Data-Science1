# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 08:19:35 2023

@author: Vishwajeet
"""

import re

# Define a sentence
sentence5 = "sharat twitted ,Wittnessing 70th republic day India from Rajpath,new Delhi ,Mesmorizing performance by Indian Army!"

# Remove special characters using regex and split the sentence into a list of words
words = re.sub(r'/([^\s\w]|_)+', '', sentence5).split()

# Print the resulting list of words
print(words)

# Import the ngrams function from NLTK library
from nltk import ngrams

# Extract bigrams using NLTK's ngrams function
bigrams = list(ngrams("The cute littile boy is playing with kitten".split(), 2))

# Print the list of bigrams
print(bigrams)

# Extract trigrams using NLTK's ngrams function
trigrams = list(ngrams("The cute littile boy is playing with kitten".split(), 3))

# Print the list of trigrams
print(trigrams)

##############################################
from nltk import ngrams
# Import the ngrams function from NLTK library

list(ngrams("The cute littile boy is playing with kitten".split(),2))
# Extract bigrams (2-grams) from the given sentence and convert the result to a list

list(ngrams("The cute littile boy is playing with kitten".split(),3))
# Extract trigrams (3-grams) from the given sentence and convert the result to a list


#########################################################3
from textblob import TextBlob
# Import the TextBlob class from the textblob library

blob=TextBlob("The cute littile boy is playing with kitten. ")
# Create a TextBlob object with the given sentence

blob.ngrams(n=2)
# Extract bigrams (2-grams) from the TextBlob object

blob.ngrams(n=3)
# Extract trigrams (3-grams) from the TextBlob object


###Toknization using keras
sentence5
# Print the value of the variable 'sentence5'

from keras.preprocessing.text import text_to_word_sequence
# Import the text_to_word_sequence function from the keras library

text_to_word_sequence(sentence5)
# Tokenize the given sentence using the text_to_word_sequence function

##############################################################
# Tokenization using TextBlob
from textblob import TextBlob
# Import the TextBlob class from the textblob library

blob=TextBlob(sentence5)
# Create a TextBlob object with the given sentence

blob.words
# Tokenize the sentence into words using TextBlob


################################################################
# Tweet Tokenizer
from nltk.tokenize import TweetTokenizer
# Import the TweetTokenizer class from the nltk.tokenize library

tweet_tokenizer=TweetTokenizer()
# Create a TweetTokenizer object

tweet_tokenizer.tokenize(sentence5)
# Tokenize the sentence using the TweetTokenizer


#################################################################
# MultiWord Expression
from nltk.tokenize import MWETokenizer
# Import the MWETokenizer class from the nltk.tokenize library

sentence5
# Print the value of the variable 'sentence5'

mwe_tokenizer=MWETokenizer([('republic','day')])
# Create a MWETokenizer object with multi-word expressions

mwe_tokenizer.tokenize(sentence5.split())
# Tokenize the sentence using the MWETokenizer


##################################################################3
# Regular Expression tokenizer
from nltk.tokenize import RegexpTokenizer
# Import the RegexpTokenizer class from the nltk.tokenize library

reg_tokenizer=RegexpTokenizer('/\w+|\$[\d\.]+|\S+')
# Create a RegexpTokenizer object to tokenize based on regular expression

reg_tokenizer.tokenize(sentence5)
# Tokenize the sentence using the RegexpTokenizer


##################################################################
# White space tokenizer
from nltk.tokenize import WhitespaceTokenizer
# Import the WhitespaceTokenizer class from the nltk.tokenize library

wh_tokenizer=WhitespaceTokenizer()
# Create a WhitespaceTokenizer object

wh_tokenizer.tokenize(sentence5)
# Tokenize the sentence using the WhitespaceTokenizer


#################################################################
from nltk.tokenize import WordPunctTokenizer
# Import the WordPunctTokenizer class from the nltk.tokenize library

wp_tokenizer=WordPunctTokenizer()
# Create a WordPunctTokenizer object

wp_tokenizer.tokenize(sentence5)
# Tokenize the sentence using the WordPunctTokenizer


##################################################################
# Stemmer
# It will remove the ing,ed from the word and give the main word
sentence6="I Love playing cricket player practices hard in their inning"
# Define a sentence

from nltk.stem import RegexpStemmer
# Import the RegexpStemmer class from the nltk.stem library

regex_stemmer=RegexpStemmer('ing$')
# Create a RegexpStemmer object to perform stemming based on regular expression

' '.join(regex_stemmer.stem(wd) for wd in sentence6.split())
# Apply stemming to each word in the sentence


####################################################################
# Porter Stemmer
# It will remove the er from the sentence and will give the original word
sentence7="Before eating, it would be nice to sanitize your hands with a sanitizer"
# Define a sentence

from nltk.stem.porter import PorterStemmer
# Import the PorterStemmer class from the nltk.stem library

ps_stemmer=PorterStemmer()
# Create a PorterStemmer object

words=sentence7.split()
# Split the sentence into words

" ".join([ps_stemmer.stem(wd) for wd in words])
# Apply stemming to each word in the sentence


##################################################################
# Lemmatization
# It will search the original form of word in the dictionary
import nltk 
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
# Import the necessary libraries

nltk.download('wordnet')
# Download the WordNet resource

lemmatization=WordNetLemmatizer()
# Create a WordNetLemmatizer object

sentence8="Those codes executed today are far better than what we execute generally"
# Define a sentence

words=word_tokenize(sentence8)
# Tokenize the sentence into words

" ".join([lemmatization.lemmatize(word) for word in words])
# Apply lemmatization to each word in the sentence


##############################################################
# Singularize and pluralization
from textblob import TextBlob
# Import the TextBlob class from the textblob library

sentence9=TextBlob("She sells seashells on the seashore")
# Create a TextBlob object with the given sentence

words=sentence9.words
# Get the words from the TextBlob object

# We want to make word[2] that is seashells in singular form
sentence9.words[2].singularize()

# We want word 5 that is seashore in plural form
sentence9.words[5].pluralize()


##################################################################
# Language translation from Spanish to English
from textblob import TextBlob
# Import the TextBlob class from the textblob library

en_blob=TextBlob(u'muy bien')
# Create a TextBlob object with the given Spanish sentence

en_blob.translate(from_lang='es',to='en')
# Translate the Spanish sentence to English


######################################################################
# Custom stopwords removal
from nltk import word_tokenize
# Import the word_tokenize function from the nltk library

sentence9="She sells seashells on the seashore"
# Define a sentence

custom_stop_word_list=['she','on','the','am','is']
# Define a list of custom stopwords

words=word_tokenize(sentence9)
# Tokenize the sentence into words

" ".join([word for word in words if word.lower() not in custom_stop_word_list])
# Select words which are not in the defined list of custom stopwords

######################################################
#############################25/11/2023
"""extracting genreal features from raw text number of words
detect presence of wh word polarity,subjectivity,
langague identification"""
#To identify the number of words
import pandas as pd
# Import the pandas library with alias pd

df=pd.DataFrame([['The vaccine for covid-19 will be announced on 1st Auguse'],
                 ['Do you know how much expectations the world population is having from this research?'],
                 ['The risk of the virus will come to an end on 31st July']])
# Create a DataFrame 'df' with a single column 'text' containing three sentences

df.columns=['text']
# Rename the column to 'text'

df
# Display the DataFrame 'df'


# Now let us measure the number of words
from textblob import TextBlob
# Import the TextBlob class from the textblob library

df['number_of_words']=df['text'].apply(lambda x:len(TextBlob(x).words))
# Calculate the number of words in each sentence and store it in a new column 'number_of_words'

df['number_of_words']
# Display the 'number_of_words' column


# Detect whether wh words are present in the text or not
wh_words=set(['why','what','who','how','where','when'])
# Define a set of wh words

df['wh_words']=df['text'].apply(lambda x:True if len(set(TextBlob(str(x)).words).intersection (wh_words))>0 else False)
# Check if any wh words are present in each sentence and store the result in a new column 'wh_words'

df['wh_words']
# Display the 'wh_words' column


# Finding out the polarity of the sentence
df['polarity']=df['text'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
# Calculate the polarity of each sentence and store it in a new column 'polarity'

df['polarity']
# Display the 'polarity' column


sentence10="I like this example  very much"
# Define a sentence

pol=TextBlob(sentence10).sentiment.polarity
# Calculate the polarity of the sentence

pol
# Display the polarity


sentence10="This is fantastic example and I like it very much"
# Define another sentence

pol=TextBlob(sentence10).sentiment.polarity
# Calculate the polarity of the sentence

pol
# Display the polarity


sentence10="This was helpful example but I would have prefer another one "
# Define another sentence

pol=TextBlob(sentence10).sentiment.polarity
# Calculate the polarity of the sentence

pol
# Display the polarity


sentence10="THis is my personal opinion that it was  helpful example but I would prefer another one"
# Define another sentence

pol=TextBlob(sentence10).sentiment.polarity
# Calculate the polarity of the sentence

pol
# Display the polarity


sentence10="That example was not very useful to me"
# Define another sentence

pol=TextBlob(sentence10).sentiment.polarity
# Calculate the polarity of the sentence

pol
# Display the polarity


# Subjectivity of the dataframe df and check whether there is 
df['subjectivity']=df['text'].apply(lambda x:TextBlob(str(x)).sentiment.subjectivity)
# Calculate the subjectivity of each sentence and store it in a new column 'subjectivity'

df['subjectivity']
# Display the 'subjectivity' column


# To find language of the sentence
# This part of the code will get an HTTP error
df['Language']=df['text'].apply(lambda x:TextBlob(str(x)).detect_language()())
# Detect the language of each sentence and store it in a new column 'Language'

#################################################################
# Bag of words
# This is BoW (Bag of Words) to convert unstructured data to structured forms
import pandas as pd
# Re-import the pandas library

from sklearn.feature_extraction.text import CountVectorizer
# Import the CountVectorizer class from the sklearn.feature_extraction.text library

corpus=['At least seven Indian pharma companies are working to develop a vaccine against the coronavirus.',
        'The deadly virus has already infected more than 14 million people globally.',
        'Bharat Biotech is among the leading pharma firms working on the coronavirus vaccine in India.']
# Define a list of sentences

bag_of_word_model=CountVectorizer()
# Create a CountVectorizer object

print(bag_of_word_model.fit_transform(corpus).todense())
# Fit the CountVectorizer on the corpus and print the bag of words representation

bag_of_word_df=pd.DataFrame(bag_of_word_model.fit_transform(corpus).todense())
# Convert the bag of words representation to a DataFrame

bag_of_word_df.columns=sorted(bag_of_word_model.vocabulary_)
# Rename the columns of the DataFrame with the vocabulary

bag_of_word_df.head()
# Display the first few rows of the DataFrame


bag_of_words_small=CountVectorizer(max_features=5)
# Create a CountVectorizer object with a maximum of 5 features

bag_of_word_df=pd.DataFrame(bag_of_words_small.fit_transform(corpus).todense())
# Convert the bag of words representation to a DataFrame

bag_of_word_df.columns=sorted(bag_of_words_small.vocabulary_)
# Rename the columns of the DataFrame with the vocabulary

bag_of_word_df.head()
# Display the first few rows of the DataFrame
