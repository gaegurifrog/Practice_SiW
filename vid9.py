# -*- coding: utf-8 -*-

#%%

current_year=2021

print("The year is "+current_year) #TypeError


#%%

print(currentyear) #NameError

#%%

A=range(100)

print(A[0])

#A[100] #IndexError

#%%

for i in range(10):
print(i**2) #IndentationError

#%%

100.1**200 #OverflowError

#%%

def wrap(s, index):
    return s[index:]+s[:index]

wrap("Python is not difficult " 11) #SyntaxError


#%%

import os

os.chdir("E:\Work")
text=""
#UnicodeDecodeError:
with open("Sample Text 4.txt", 'r') as infile:
    for character in infile:
        text+=character

#%%
import re

def subsentence(sentence, start, end):
    """ Returns a fragment of sentence, beginning with the start'th word and ending before the end'th one.
    
    subsentence('a b c d', 1,3) returns 'b c'
    """
    
    sentence_list=re.split(' ', sentence)
    return sentence_list[start:end]
    
sentence='Python is not very difficult at all'
print(subsentence(sentence, 2,5)) # Not really what we wanted!!!!


#%%
import re

sentence=re.split(' ', 'This 문장 contains some 한국어 and some 영어!')

print([word for word in sentence if re.search('?????????', word)])


