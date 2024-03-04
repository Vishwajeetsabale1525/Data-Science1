# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 15:49:33 2023

@author: Vishwajeet
"""

import pandas as pd
import matplotlib.pylab as plt
#Now import file from data set and create a dataframe
Univ1=pd.read_excel("C:/datasets/University_Clustering.xlsx")
a=Univ1.describe()
#We hava one column "State" which really not useful we will drop it
Univ=Univ1.drop(["State"],axis=1)
'''
we know that there is a scale difference among the columns,
which we have to remove either by using normalization or standardization
wheneve there is mixed data aplly normalization
'''
def norm_fun(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

'''
Now apply this normalization function to Univ dataframe
for all the rows and columns from 1 until end
since 0 the column has universityy name henced skipped
'''
df_norm=norm_fun(Univ.iloc[:,1:])
'''
You can check the df_norm dataframe which is scaled between values
from 0 to 1. You can apply describe function to new dataframe
'''
b=df_norm.describe()
'''
before you apply clustering, you need to plot dendogram
first now to create dendogram we need to measure distance, we have to import
linkage
'''
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch

z=linkage(df_norm,method="complete",metric="euclidean")
plt.figure(figsize=(15,8));
plt.title("Hierarchical Clustering Dendogram")
plt.xlabel("Index");
plt.ylabel("Distance")

#ref help of dendogram
#sch.dendogram(z)
sch.dendrogram(z,leaf_rotation=0,leaf_font_size=10)
plt.show()

#dendogram()
'''
applying agglomerative clustering choosing 3 clusters
from dendogram
whatever has been displayed in dendogram is not clustering it is just showing
number of possible clusters
'''
from sklearn.cluster import AgglomerativeClustering
h_complete=AgglomerativeClustering(n_clusters=3,linkage='complete',affinity="euclidean").fit(df_norm)
#apply labels to the clusters
h_complete.labels_
cluster_labels=pd.Series(h_complete.labels_)
#Assign this series to Univ Dataframe as column and name the column
Univ['clust']=cluster_labels
#we want to relocate the column 7 and 0 th position
Univ1=Univ.iloc[:,[7,1,2,3,4,5,6]]
#now check the Univ1 dataframe
Univ1.iloc[:,2:].groupby(Univ1.clust).mean()
'''
from the output cluster 2 has got highest top10
lowest accept ratio best faculty ratio and highest expenses highest graduates
ratio
'''
Univ1.to_csv("University.csv",encoding="utf-7")
import os
os.getcwd()
