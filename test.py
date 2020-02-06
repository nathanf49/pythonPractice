# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 12:23:57 2020

@author: Nathan
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    count = 0
    returns = []
    for element in aTup:
        if count % 2 == 0:
            returns.append(element)
            count+=1
        else:
            count+=1
    return(returns)
test = ('I', 'am', 'a', 'test', 'tuple')
print(oddTuples(test))