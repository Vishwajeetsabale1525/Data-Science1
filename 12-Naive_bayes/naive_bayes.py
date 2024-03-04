# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 09:19:19 2024

@author: Vishwajeet
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer


## Loading Data
email_data = pd.read_csv("C:/Data Science/datasets/sms_raw_NB.csv", encoding="ISO-8859-1")

## Cleaning Data

import re


def cleaning_text(i):
    w=[]
    i = re.sub("[A-Za-z""]+"," ", i).lower()
    for word in i.split(" "):
        if len(word) > 3:
            w.append(word)
    return (" ".join(w))

## Testing above function with some test text ##
cleaning_text("Hope you are having good week.just checking")
cleaning_text("hope i can understand your fellings 121323224.23232.hi how are you")
cleaning_text("hi how are you, I am sad")

email_data.text = email_data.text.apply(cleaning_text)
email_data = email_data.loc[email_data.text !="",:]

from sklearn.model_selection import train_test_split
email_train,email_test = train_test_split(email_data,test_size=0.2)

## Creating matix of token counts for entire text document

def split_into_words(i):
    return[word for word in i.split(" ")]

email_bow = CountVectorizer(analyzer=split_into_words).fit(email_data.text)
all_emails_matirx = email_bow.transform(email_data.text)

## For training messages
train_emails_matirx = email_bow.transform(email_train.text)

## For testing messages
test_emails_matrix = email_bow.transform(email_test.text)


## Learning term weigtaging and normaling on entire emails

tfidf_transformer = TfidfTransformer().fit(all_emails_matirx)

## Preparing TFIDF for train emails
train_tfidf = tfidf_transformer.transform(train_emails_matirx)

## Preparing TFIDF for test emails
test_tfidf = tfidf_transformer.transform(test_emails_matrix)
test_tfidf.shape

## Now let us apply this to Naive Bayes

from sklearn.naive_bayes import MultinomialNB as MB
classifier_mb = MB()
classifier_mb.fit(train_tfidf,email_train.type)


##Evaluation on Test Data

test_pred_m = classifier_mb.predict(test_tfidf)
accuracy_test_m = np.mean(test_pred_m == email_test.type)
accuracy_test_m

# 0.9438202247191011 Here we can say model accuracy is 94%