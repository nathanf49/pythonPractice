# O(n)

def checkPermuation(string1, string2):
    if len(string1) != len(string2):  # definitely not permutations if they're not even the same length
        return False

    for char in string1: # if the strings are the same length, they will have the same count of every char
        if string1.count(char) != string2.count(char):
            return False
    return True
