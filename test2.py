# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 12:10:39 2020

@author: Nathan
"""

def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    out = []
    for s in L:
        if f(s) is True:
            out.append(s)
    L[:] = out
    return(len(out))
    

#run_satisfiesF(L, satisfiesF)

#For your own testing of satisfiesF, for example, see the following test function f and test code:
def f(s):
    return 'a' in s
      
L = ['a', 'b', 'a']
print(satisfiesF(L))
print(L)
'''
Should print:
2
['a', 'a']
'''