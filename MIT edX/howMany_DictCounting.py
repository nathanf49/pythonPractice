# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:33:23 2020

@author: Nathan
"""

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0
    for key in aDict:
        count += len(aDict[key])
    return(count)
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
print(how_many(animals))