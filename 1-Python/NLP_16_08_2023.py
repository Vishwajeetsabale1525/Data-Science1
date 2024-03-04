 # -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 09:17:28 2023

@author: Vishwajeet
"""

import re
#Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
text1='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion
'''

pattern=r'\d\d\d\d\d\d\d\d\d\d'
matches=re.findall(pattern,text1)
matches


text1='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion
'''

pattern=r'\d{10}'
matches=re.findall(pattern,text1)
matches


pattern=r'\(\d{3}\)-\d{3}-\d{4}'
matches=re.findall(pattern,text1)
matches

#Find both the matches

pattern=r'\(\d{3}\)-\d{3}-\d{4}|\d{10}'
matches=re.findall(pattern,text1)
matches
###################################################

'''
Let us try 
Following pattern

A protracted; legal battle; over a 32-carat;
 Golconda diamond-
 
 we want any character except ; and -
 parren will be[^;-]
 '''
text2='''A protracted; legal battle; over a 32-carat;
Golconda diamond-'''
pattern='[^;-]'
matches=re.findall(pattern,text2)
matches


text3='''Note 1 – Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated financial statements of Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”), including the consolidated balance sheet as of
June 30, 2023, the consolidated statements of operations, the consolidated statements of comprehensive income, the consolidated statements of
redeemable noncontrolling interests and equity for the three and six months ended June 30, 2023 and 2022, and the consolidated statements of cash
flows for the six months ended June 30, 2023 and 2022, as well as other information disclosed in the accompanying notes, are unaudited. The
consolidated balance sheet as of December 31, 2022 was derived from the audited consolidated financial statements as of that date. The interim
consolidated financial statements and the accompanying notes should be read in conjunction with the annual consolidated financial statements and the
accompanying notes contained in our Annual Report on Form 10-K for the year ended December 31, 2022.
The interim consolidated financial statements and the accompanying notes have been prepared on the same basis as the annual consolidated
financial statements and, in the opinion of management, reflect all adjustments, which include only normal recurring adjustments, necessary for a fair
statement of the results of operationssss for the periods presented. The consolidated results of operations for any interim period are not necessarily
indicative of the results to be expected for the full year or for any other future years or interim periods.

'''
pattern='Note \d . [^\n]'
matches=re.findall(pattern,text3)
matches

pattern='Note [^\n]+'
matches=re.findall(pattern,text3)
matches

pattern='Note \d...([^\n]+)'
matches=re.findall(pattern,text3)
matches


##########################################
'''
Now lwt u take another text
extract financial periods from a company financial
'''
text4='''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion.
'''
#Quarter can be q1,q2,q3,q4 not q5 or q6
pattern = 'FY\d{4} Q\d'
matched=re.findall(pattern,text4)
matched


###########################################
#Now go to right bottom widow and there is
#option single character a,b or c[abc]
#now try second pattern 'FY\d{4} Q[1234]'

pattern='FY\d{4} Q[1234]'
matched=re.findall(pattern,text4)
matched

###############################################
#######OR
pattern='FY\d{4} Q[1-4]'
matched=re.findall(pattern,text4)
matched
#you can give same result

###################################################
pattern1='FY\d{4} Q[1-4] |fy\d{4} Q[1-4]'

matched=re.findall(pattern1,text4)
matched
matched=re.findall(pattern1,text4,re.IGNORECASE)
matched
###############################################3
#We want only 2021 Q1 and 2020 Q4
pattern='FY(\d{4} Q[1-4])'
matched=re.findall(pattern,text4,re.IGNORECASE)
matched
###############################################

#Now let us assume that we want find financial no
text6='''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
 In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
'''
pattern='\$[0-9\.]+'
matched=re.findall(pattern,text6)
matched
#if we do not want to $
pattern='\$([0-9\.]+)'
matched=re.findall(pattern,text6)
matched



