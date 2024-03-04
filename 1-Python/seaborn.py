# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 15:10:29 2023

@author: Vishwajeet
"""

#How to use seaborn for data visualization
#pip install seaborn
import seaborn as sns
import pandas
import matplotlib.pyplot as plt
#Seaborn has 18 in-built datasets
#that can be found using the following command
sns.get_dataset_names()
df=sns.load_dataset('titanic')
df.head
#count plot
'''
count plot is helpful when dealing with
categorical values. It is used to plot the frequency
of the diff categories.
The col sex contains categorical data in the title data 
i.e, male and female
'''
sns.countplot(x='sex',data=df)
#x-the name of the col
#data=name of the dataframe

sns.countplot(x='sex',hue='survived',data=df,palette='Set1')
sns.countplot(x='sex',hue='survived',data=df,palette='Set2')
sns.countplot(x='sex',hue='survived',data=df,palette='Set3')

#hue-The name of the cateorical column to split the bars.
#Palette-The color palatte to be used
#KDE plot 
'''
The kernel density Estimate (KDE) plot is used
to plot the distribution of continuois data
'''

sns.kdeplot(x='age',data=df,color='black')
#x-name of the column
#data-the dataframe
#color the color of the graph

'''
DISTRIBUTION GRAPH
'''
sns.displot(x='age',kde=True,bins=6,data=df)
#kde-It is set to false by default. However
#bins-The numbers of bins/bars.
#The lower the no ,wider the bars and wider the integers
sns.displot(x='age',kde=True,bins=5,
            hue=df['survived'],palette='Set1',
            data=df)



########################################
df=sns.load_dataset('iris')
df.head
#Scatter plot help understand co-relation between data'

sns.scatterplot(x='sepal_length',y='petal_length',
                data=df,hue='species')

##############################################
'''
join plot
A join plot is also used to plot the coordination 
between data
'''
sns.jointplot(x='sepal_lenth',y='petal_length',data=df,kind='reg')
sns.jointplot(x='sepal_lenth',y='petal_length',data=df,kind='hist')

sns.jointplot(x='sepal_lenth',y='petal_length',data=df,kind='kde')



'''
kind- the kind of the plot to be plotted 
It can be one of the following
'''
#Pair plots
sns.pairplot(df)
#heat map can be use to visualize confused matrix
corr=df.corr()
sns.heatmap(corr)