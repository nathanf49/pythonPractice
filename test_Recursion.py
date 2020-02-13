# -*- coding: utf-8 -*-
"""
Write a Python function that returns a list of keys in aDict with the value target. 
The list of keys you return should be sorted in increasing order. 
The keys and values in aDict are both integers. 
(If aDict does not contain the value target, you should return an empty list.)
This function takes in a dictionary and an integer and returns a list.
"""
def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '': #If strings are not of same length, then the extra elements should appear at the end.
            return(s2)
        if s2 == '': #If strings are not of same length, then the extra elements should appear at the end.
            return(s1)
        else: #Returns a new str with elements of s1 and s2 interlaced, beginning with s1.
            return(s1[0] + s2[0] + helpLaceStrings(s1[1:], s2[1:], out))
    return helpLaceStrings(s1, s2, '')
            
s1 = 'NathanFrank'
s2 = 'Frank'
print(laceStringsRecur(s1,s2))