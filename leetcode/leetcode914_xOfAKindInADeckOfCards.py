# -*- coding: utf-8 -*-
"""
914. X of a Kind in a Deck of Cards:
In a deck of cards, each card has an integer written on it.
Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of
cards, where:
    Each group has exactly X cards.
    All the cards in each group have the same integer.
   
Example 1:
Input: [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]

Example 2:
Input: [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.

Example 3:
Input: [1]
Output: false
Explanation: No possible partition.

Example 4:
Input: [1,1]
Output: true
Explanation: Possible partition [1,1]



Example 5:
Input: [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2]
"""

def hasGroupsSizeX(deck):
    if len(deck) < 2:
        return(False)
    found = {} #dictionary of cards 
    for card in deck:
        if str(card) not in found: #if card is not in dict, inialize card and count at 1
            found[str(card)] = 1
        elif str(card) in found: #if card is in dict, increase count by 1
            found[str(card)] += 1
                
    check = found[str(max(found))] #finds value of last element in dict, could be any element
    for card in found:
        if found[card] != check: #if not even, return False
            return(False)
    return(True)
deck = [1,1,2,2,2,2] #Should return True [1,1], [2,2], [2,2]
print(hasGroupsSizeX(deck))