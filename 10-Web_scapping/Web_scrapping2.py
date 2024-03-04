# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 08:19:11 2023

@author: Vishwajeet
"""

from bs4 import BeautifulSoup
soup=BeautifulSoup(open("C:/13-Web_scapping/sample_doc.html"),'html.parser')
print(soup)
#It is going to show all the html contents extracted
soup.text
#It is going to show only text
soup.contents
#it is going to show all the html content extracted
soup.find('address')
soup.find_all('address')
soup.find_all('q')
soup.find_all('b')
table=soup.find('table')
table
for row in table.find_all('tr'):
    columns=row.find_all('td')
    print(columns)
    
#It will show all the rows except first row

#Now we want to display M.Tech which is located on third roew