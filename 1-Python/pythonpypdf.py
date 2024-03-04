from PyPDF2 import PdfFileReader

#importing requried module
from PyPDF2 import PdfReader

#creating a pdf reader object
reader = PdfReader('c:/1-Python/python_tutorial.pdf')

#printing number of pages in pdf file
print(len(reader.pages))

#getting a specific page from the pdf file
page = reader.pages[10]

#extracting text from page
text = page.extract_text()
print(text)

###############################################
import re
chat2='Hi: I have a problem with my order number 412889912'
pattern='order*.[^\d]+(\d*)'
matched=re.findall(pattern,chat2)
matched

chat2='Hi: I have a problem with my order number #412889912'
pattern='order[^\d]*(\d*)'
matched=re.findall(pattern,chat2)
matched

chat2='Hi:my order number 412889912 is having an issue,I was charged 300$ when online'
pattern='order*.[^\d]*(\d*)'
matches=re.findall(pattern,chat2)
matches



############################################3
def get_pattern_match(pattern, text):
    matches=re.findall(pattern, text)
    if matches:
        return matches[0]
get_pattern_match('order[^\d]*(\d*)',chat2)

###############################################
#Retrieve email id and phone
chat1='Hi you asked lot of questions   123456768789,Vishwajeet@123.com'













###############################################
text='''
Born	Elon Reeve Musk
June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner and CTO of Twitter
President of the Musk Foundation
Founder of the Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)​
Partner	Grimes (2018–2021)[1]
Children	10[2]
Parents	
Errol Musk
Maye Musk
Family	Musk family
'''
get_pattern_match(r'age (\d+)',text)
get_pattern_match(r'Born(.*)\n', text).strip()
#Out[21]: 'Elon Reeve Musk'
get_pattern_match(r'Born.*\n(.*)', text)
#Out[22]: 'June 28, 1971 (age 52)'
get_pattern_match(r'Born.*\n(.*)\(age', text)
#Out[23]: 'June 28, 1971 '
get_pattern_match(r'\(age.*\n(.*)', text)


############################################
def extract_personal_information(text):
    age=get_pattern_match('age (\d+)', text)
    full_name=get_pattern_match('Born(.*)\n', text)
    birth_date=get_pattern_match('Born.*\n(.*)\(age', text)
    birth_place=get_pattern_match('\(age.*\n(.*)', text)
    return{
        'age':int(age),
        'name':full_name.strip(),
        'birth_date':birth_date.strip(),
        'birth_place':birth_place.strip()
        
        }
extract_personal_information(text)

#############################################
text1='''
Born	Dhirajlal Hirachand Ambani
28 December 1932
Chorwad, Junagadh State, British India
(present-day Gujarat, India)
Died	6 July 2002 (aged 69)
Mumbai, Maharashtra, India
Citizenship	British India (1932–1947)
Dominion of India (1947–1950)
India(1950–2002)
Occupation	Businessman
Organization(s)	Reliance Industries
Reliance Capital
Reliance Infrastructure
Reliance Power
Spouse	Kokila Dhirubhai Ambani
​
​(m. 1955)​
Children	4, including Mukesh Ambani and Anil Ambani
Awards	Padma Vibhushan (2016) (posthumously)
'''
get_pattern_match(r'aged (\d+)',text1)
get_pattern_match(r'Born(.*)\n', text1).strip()
get_pattern_match(r'Born.*\n(.*)', text1)
get_pattern_match(r'Born.*\n(.*)\(age', text1)
###############################################3
def extract_personal_information(text1):
    aged=get_pattern_match('aged (\d+)', text1)
    full_name=get_pattern_match('Born(.*)\n', text1)
    birth_date=get_pattern_match('Born.*\n(.*)\(age', text1)
    birth_place=get_pattern_match('\(aged.*\n(.*)', text1)
    return{
        'aged':int(aged),
        'name':full_name.strip(),
        'birth_date':birth_date.strip(),
        'birth_place':birth_place.strip()
        
        }
extract_personal_information(text1)

#############################################
