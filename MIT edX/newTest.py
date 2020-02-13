# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 13:39:46 2020

@author: Nathan
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) == 0:
        return(False)
    if len(aStr) == 1 and aStr[0] != char:
        return(False)
    start = len(aStr) // 2
    if char < aStr[start]:
        return(isIn(char, aStr[:start]))
    elif char > aStr[start]:
        return(isIn(char, aStr[start:]))
    elif char == aStr[start]:
        return(True)
    else:
        return(False)

print(isIn('c', 'cdeefghjkrssvzz'))