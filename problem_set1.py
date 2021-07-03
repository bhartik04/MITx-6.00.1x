#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#problem: Assume s is a string of lower case characters.
#
#Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
#
#@author: bhartikindra


s=str(input("Enter a string: "))

i=0
c=1
noOfChar=[]
indices=[]

length=len(s)

for i in range(length-1):
    '''
    Returns two lists: noOfChar and indices.
    
    noOfChar is a list the length of substrings in alphabetical order.
    
    indices is a list of indices of the last character corresponding to every substring in noOfChar
    '''
    if ord(s[i+1])>=ord(s[i]):
        c=c+1
        
    else: 
        noOfChar.append(c)
        indices.append(i)
        c=1
       
noOfChar.append(c)
indices.append(i+1)

if len(noOfChar)==0:
    print('Longest substring in alphabetical order is:' + s) 
else:
    
    longest=max(noOfChar)       
    position=noOfChar.index(longest)
    initialIndex= indices[position]-noOfChar[position]+1
    finalIndex=indices[position]
    print('Longest substring in alphabetical order is:' + s[initialIndex:finalIndex+1]) 


 