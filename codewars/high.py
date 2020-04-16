"""
Given a string of words, you need to find the highest scoring word.
Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
You need to return the highest scoring word as a string.
If two words score the same, return the word that appears earliest in the original string.
All letters will be lowercase and all inputs will be valid.
"""


def high(x):
    words = x.split(' ')  # breaks into a list of words
    highScore = -1  # initial highscore is negative so anything will overwrite it
    out = ''
    for word in words:
        if score(word) > highScore:
            highScore = score(word)
            out = word
    return out


def score(word):  # counts position of each letter of a word in the alphabet and adds it together
    points = '_abcdefghijklmnopqrstuvwxyz'  # underscore at the start so position of each is proper number of points
    currentScore = 0
    for letter in word:
        currentScore += points.find(letter)  # adds position of each letter to currentScore
    return currentScore


test = 'what time are we climbing up the volcano'  # 'volcano'
print(high(test))
