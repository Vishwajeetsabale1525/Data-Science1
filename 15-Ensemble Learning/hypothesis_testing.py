# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 09:42:40 2024

@author: Vishwajeet
"""
#for given dataset check weather scores are equal or less than 89
import pandas as pd
import numpy as  np
import scipy
from scipy import stats
import statsmodels.stats.descriptivestats as sd
import statsmodels.stats.weightstats
"""
1 sample sign test
for given dataset check wweather the scores are either equal or less than 80
H0=scores are either equal or less than 80
H1=scores are not equal and greater than 80
whenever there is single sample and data is not normal
"""
marks=pd.read_csv("C:/Data Science/datasets/hypothesis_datasets/Signtest.csv")
#Normal QQ plot
import pylab
stats.probplot(marks.Scores,dist='norm',plot=pylab)
#Data is not normal
#H0=data is normal
#H1=Data is not normal
stats.shapiro(marks.Scores)
"""
p_value is 0.024>0.005 p is high null fly
Decision:Data is not normal
Let us check the distribution of the data
"""
marks.Scores.describe()
#1 sample sign test
sd.sign_test(marks.Scores,mu0=marks.Scores.mean())