# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 12:23:57 2020

@author: Nathan
"""
s = 'abcdefghijklmnopqrstuvwxyz'

#Makes dictrionary to get the position of each letter by calling dict[letter]
letterPosition = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
currentString = '' #initialize blank strings at start
maxString = ''
i = 0 # initialize loop variable
while i < len(s):
    letter = s[i]
    if currentString == '': #if current string is empty, start by adding a letter
        currentString += letter #add letter to the end of currentString
    else: 
        if letterPosition.index(letter) >= letterPosition.index(currentString[len(currentString)-1]): #if index of letter is >= index of last letter in currentString
            currentString += letter #add letter to the end of currentString
        else: #if index of letter is less than index of last letter in currentString
            if len(currentString) > len(maxString): #if the currentString is longer than current max
                maxString = currentString #replace current max
            i -= len(currentString)
            currentString = ''
    i += 1
if len(currentString) > len(maxString): #if the currentString is longer than current max
                maxString = currentString #replace current max
print('Longest substring in alphabetical order is: ' + maxString)