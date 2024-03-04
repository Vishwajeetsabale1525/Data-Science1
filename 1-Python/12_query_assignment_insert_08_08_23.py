
#12 08 August 2023

'''
1.Write pandas program to create dataframe from a dictionary and display
Sample Data:{'X':[34,35,67,56,43],'Y':[67,46,88,97,65], 'Z':[67,89,78,65,45]}
'''
import pandas as pd
abc={'X':[34,35,67,56,43],'Y':[67,46,88,97,65], 'Z':[67,89,78,65,45]}
df=pd.DataFrame(abc)
print(df)


'''
2.Write pandas program to create and display a dataframe from a specified
Sample python dictionary data and list labels:
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,45,34,21,35],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
           labels=['a','b','c','d','e']
           
'''
import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,45,34,21,35],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df2=pd.DataFrame(exam_data,index=row_labels)
print(df2)


'''
3.Write pandas program to display summary of basic info about the dataframe 
and its data.
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,45,34,21,35],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
           labels=['a','b','c','d','e']

'''
import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,45,34,21,35],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
df=pd.DataFrame(exam_data)
df.describe()


'''
4.Write pandas program to to get the first  3 rows of given dataframe
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,45,34,21,35],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
'''
import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,45,34,21,35],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)
print(df.iloc[:3])


'''
5.Write a pandas progarm to select the 'name ' and 'score' column from the 
dataframe
'''
import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,45,34,21,35],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)
print(df[['name','score']])


'''
6.Write a pandas program to select the specified columns and 
rows from a dataframe
Select specific columns and rows:
'''
df2 = df.iloc[1:3 , 1:4] #1:3 means two rows and 1:4 means 3 columns
df2

'''
7) Write a pandas program to select rows were number of attempts
    in exam is>2.
'''
#1
df5 = df[df['attempts']>2] 
df5

#2
df5 = df.loc[df.attempts>2]
df5

'''
write panmdas program to find no of rows and columns
in a DataFrame

'''

'''
7.Write a pandas program to select rows where the no. of attempts of 
examination is greater than 2
'''
import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,45,34,21,35],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)
print('Attempts in examination greater than 2:')
print(df[df['attempts']>2])

'''OR'''

df2=df.loc[df.attempts>2]
print(df2)


'''
8.Write a pandas program to count the number of rows and columns in 
dataframe.
'''
import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,45,34,21,35],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)

rows_count=len(df.axes[0])
print(rows_count)
column_count=len(df.axes[1])
print(column_count)

row_count = df.shape[0]
print(row_count)
col_count = df.shape[0]
print(col_count)


'''
9.write pandas program to select the rows were the 
score is missing
'''
import pandas as pd
import numpy as np
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,45,34,21,35],
           'attempts':[1,3,2,np.nan,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)
print("")
df2 = (df[df['score'].isnull()])
df2

'''
10. write pandas program to select the rows 
    were score is between 15 and 20.
'''
import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,17,34,21,35],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)

print(df[df['score'].between(15,20)])

'''
11. write pandas program to select the rows were the no of attempts
   in exam is less than 2 and score gretter than 15
'''
import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,17,34,21,35],
           'attempts':[1,1,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)
print(df[(df['attempts'] < 2) & (df['score'] >15)])

'''
12.write pandas program to change the score in row 'd' to 11.5
'''
import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,17,34,21,35],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)
df.loc['d', 'score']=11.5  # d means row value score means column value
print(df)

'''
13.write pandas program to calculate the sum of the exam attempts 
by the student
'''
import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,17,34,21,35],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)
print(df['attempts'].sum())

'''
14.write pandas program to calculate the mean of all students 
score
'''
import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,17,34,21,35],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)
print(df['score'].mean())
####df.describe

'''
15.write pandas program to append a new row 'k' 
to dataframe
'''
import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,17,34,21,35],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)
print("Original row:")
print(df)
print("\n append a new row:")
df.loc['k']=['Suresh',22,3,'yas']
print(df)

'''
16.write pandas program to sort the detaframe 
first by 'name' in desending order,
then by 'score' in assending order
'''
import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,17,34,21,35],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)
df = df.sort_values(by=['name'],ascending=[False])
df = df.sort_values(by=['score'],ascending=[True])
print(df)

################################################################
'''
17.write pandas program to replace 
the 'qualify' columns contains the values
'yes' and 'no' with True and False.
'''
import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,17,34,21,35],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)
df['qualify'] = df['qualify'].map({'Yes':True,'No':False})
print(df)

'''
18. Write pandas program to change name 'Ganesh' to 'Jeams' in 
name column of the DataFrame 
'''
import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,17,34,21,35],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)
df['name'] =df['name'].replace('Ganesh','Jeams')
print(df)

'''
19.Write a pandas program to insert a new columns in 
existing Datafram
'''
import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,17,34,21,35],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)
color= ['Red','Orange','Blue','Yellow','Black']
df['color']=color
print(df)

'''
20.Write a search pandas program to iterrate 
   over rows in a dataFram
'''
import pandas as pd
exam_data={'name':['Ram','Sham','Ghansham','Ganesh','Ramesh'],
           'score':[12,17,34,21,35],
           'attempts':[1,3,2,3,2],
           'qualify':['Yes','No','Yes','No','No']}
row_labels=['a','b','c','d','e']
df=pd.DataFrame(exam_data,index=row_labels)

for index,row in df.iterrows():
    print(row['name'], row['score'])








































    