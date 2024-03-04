# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 08:55:49 2023

@author: Vishwajeet
"""

import pandas as pd
import seaborn as sns
import numpy as np
df=pd.read_csv('c:/2-datasets/Boston.csv')
df
df.dtypes
df.shape
df.columns
summery=df.describe()
summery

#from the the summery we inference that the data is continuoues in nature
#understanding of data
#if we observe the 5 number summery
#In zn column 0th,25th,50th percentile value is 0
#also in chas column 0th,25ht,50th,75th percentile value is 0
######################################
#checking duplicates 


df_dup=df.duplicated()
sum(df_dup)

#after checking for duplicated
#we get inference that ther is no any duplicated value

############################################
#checking outliers
sns.boxplot(df.crim) #outliers present
sns.boxplot(df.zn)
#it contains several outliers
sns.boxplot(df.indus) #no outliers
sns.boxplot(df.chas) #only 1 outlier
#from boxplot of chas we get that
#oth,25th,50th,75th percentile is 0 and only 100th percentile is 1 that is the outlier
sns.boxplot(df.nox) #no outlier
sns.boxplot(df.rm) #several outlier
sns.boxplot(df.age) #no outlier
sns.boxplot(df.dis) #outlier is there
sns.boxplot(df.rad) #no outlier
sns.boxplot(df.tax) #no outlier
sns.boxplot(df.ptratio) #outliers are there
sns.boxplot(df.black) #outlier are there
sns.boxplot(df.lstat) #outlier present
sns.boxplot(df.medv) #outlier present

###############################################
#handling outliers
#Handling ouliers by trimmimg
#1.on crim column
Iqr_crim=df.crim.quantile(0.75)-df.crim.quantile(0.25)
Iqr_crim
up_lm_crim=df.crim.quantile(0.75)+1.5*Iqr_crim
up_lm_crim
low_crim=df.crim.quantile(0.25)-1.5*Iqr_crim
low_crim
crim_outlier=np.where(df.crim>up_lm_crim,True,np.where(df.crim<low_crim,True,False))
trimmed_outliers1=df.loc[~crim_outlier]
trimmed_outliers1.shape
#(440,15)

#2.on zn column
Iqr_zn=df.zn.quantile(0.75)-df.zn.quantile(0.25)
Iqr_zn
up_lm_zn=df.zn.quantile(0.75)+1.5*Iqr_zn
up_lm_zn
low_zn=df.zn.quantile(0.25)-1.5*Iqr_zn
low_zn
zn_outlier=np.where(df.zn>up_lm_zn,True,np.where(df.zn<low_zn,True,False))
trimmed_outliers2=df.loc[~zn_outlier]
trimmed_outliers2.shape
#(438,15)

#3.on chas column
Iqr_chas=df.chas.quantile(0.75)-df.chas.quantile(0.25)
Iqr_chas
up_lm_chas=df.chas.quantile(0.75)+1.5*Iqr_chas
up_lm_chas
low_chas=df.chas.quantile(0.25)-1.5*Iqr_chas
low_chas
chas_outlier=np.where(df.chas>up_lm_chas,True,np.where(df.chas<low_chas,True,False))
trimmed_outliers3=df.loc[~chas_outlier]
trimmed_outliers3.shape
#(471,15)

#4.on rm column
Iqr_rm=df.rm.quantile(0.75)-df.rm.quantile(0.25)
Iqr_rm
up_lm_rm=df.rm.quantile(0.75)+1.5*Iqr_rm
up_lm_rm
low_rm=df.rm.quantile(0.25)-1.5*Iqr_rm
low_rm
rm_outlier=np.where(df.rm>up_lm_rm,True,np.where(df.rm<low_rm,True,False))
trimmed_outliers4=df.loc[~rm_outlier]
trimmed_outliers4.shape
#(476,15)

#5.on dis column
Iqr_dis=df.dis.quantile(0.75)-df.dis.quantile(0.25)
Iqr_dis
up_lm_dis=df.dis.quantile(0.75)+1.5*Iqr_dis
up_lm_dis
low_dis=df.dis.quantile(0.25)-1.5*Iqr_dis
low_dis
dis_outlier=np.where(df.dis>up_lm_dis,True,np.where(df.dis<low_dis,True,False))
trimmed_outliers5=df.loc[~dis_outlier]
trimmed_outliers5.shape
#(501,15)

#6.on ptratio column
Iqr_ptratio=df.ptratio.quantile(0.75)-df.ptratio.quantile(0.25)
Iqr_ptratio
up_lm_ptratio=df.ptratio.quantile(0.75)+1.5*Iqr_ptratio
up_lm_ptratio
low_ptratio=df.ptratio.quantile(0.25)-1.5*Iqr_ptratio
low_ptratio
ptratio_outlier=np.where(df.ptratio>up_lm_ptratio,True,np.where(df.ptratio<low_ptratio,True,False))
trimmed_outliers6=df.loc[~ptratio_outlier]
trimmed_outliers6.shape

#7.on black column
Iqr_black=df.black.quantile(0.75)-df.black.quantile(0.25)
Iqr_black
up_lm_black=df.black.quantile(0.75)+1.5*Iqr_black
up_lm_black
low_black=df.black.quantile(0.25)-1.5*Iqr_black
low_black
black_outlier=np.where(df.black>up_lm_black,True,np.where(df.black<low_black,True,False))
trimmed_outlier7=df.loc[~black_outlier]
trimmed_outlier7.shape
#(429,15)

#8.on lstat column
Iqr_lstat=df.lstat.quantile(0.75)-df.lstat.quantile(0.25)
Iqr_lstat
up_lm_lstat=df.lstat.quantile(0.75)+1.5*Iqr_lstat
up_lm_lstat
low_lstat=df.lstat.quantile(0.25)-1.5*Iqr_lstat
low_lstat
lstat_outlier=np.where(df.lstat>up_lm_lstat,True,np.where(df.lstat<low_lstat,True,False))
trimmed_outliers8=df.loc[~lstat_outlier]
trimmed_outliers8.shape

#9.on medv column
Iqr_medv=df.medv.quantile(0.75)-df.medv.quantile(0.25)
Iqr_medv
up_lm_medv=df.medv.quantile(0.75)+1.5*Iqr_medv
up_lm_medv
low_medv=df.medv.quantile(0.25)-1.5*Iqr_medv
low_medv
medv_outlier=np.where(df.medv>up_lm_medv,True,np.where(df.medv<low_medv,True,False))
trimmed_outliers9=df.loc[~medv_outlier]
trimmed_outliers9.shape
#(466,15)

#################################################
#Handling by retain technique
#1.on crim column
outlier_replacement1=pd.DataFrame(np.where(df.crim>up_lm_crim,up_lm_crim,np.where(df.crim<low_crim,low_crim,df.crim)))
sns.boxplot(outlier_replacement1[0])

#2.on zn column
outlier_replacement2=pd.DataFrame(np.where(df.zn>up_lm_zn,up_lm_zn,np.where(df.zn<low_zn,low_zn,df.zn)))
sns.boxplot(outlier_replacement2[0])

#3.on chas column
outlier_replacement3=pd.DataFrame(np.where(df.chas>up_lm_chas,up_lm_chas,np.where(df.chas<low_chas,low_chas,df.chas)))
sns.boxplot(outlier_replacement3[0])

#4.on rm column
outlier_replacement4=pd.DataFrame(np.where(df.rm>up_lm_rm,up_lm_rm,np.where(df.rm<low_rm,low_rm,df.rm)))
sns.boxplot(outlier_replacement4[0])

#5.on dis column
outlier_replacement5=pd.DataFrame(np.where(df.dis>up_lm_dis,up_lm_dis,np.where(df.dis<low_dis,low_dis,df.dis)))
sns.boxplot(outlier_replacement5[0])

#6.on ptratio column
outlier_replacement6=pd.DataFrame(np.where(df.ptratio>up_lm_ptratio,up_lm_ptratio,np.where(df.ptratio<low_ptratio,low_ptratio,df.ptratio)))
sns.boxplot(outlier_replacement6[0])

#7.on black column
outlier_replacement7=pd.DataFrame(np.where(df.black>up_lm_black,up_lm_black,np.where(df.black<low_black,low_black,df.black)))
sns.boxplot(outlier_replacement7[0])

#8.on lstat column
outlier_replacement8=pd.DataFrame(np.where(df.lstat>up_lm_lstat,up_lm_lstat,np.where(df.lstat<low_lstat,low_lstat,df.lstat)))
sns.boxplot(outlier_replacement8[0])

#9.on medv column
outlier_replacement9=pd.DataFrame(np.where(df.medv>up_lm_medv,up_lm_medv,np.where(df.medv<low_medv,low_medv,df.medv)))
sns.boxplot(outlier_replacement9[0])










