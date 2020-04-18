# O(1)
"""
String Rotation; Assume you have a method isSubst ring which checks if one word is a substring of another.
Given two strings, si and s2, write code to check if s2 is a rotation of si using only one call to isSubst ring
[e.g., "water bottle" is a rotation oP'erbottlewat"),
"""

def stringRotation(string1, string2):
    return is_substring(string2 * 2, string1) # multiplying s2 *2 will make s1 in the middle if it is a rotation of s1
    #return string1 in 2*string2
def is_substring(string, sub): # returns True if sub is in string, False if sub is not
    return string.find(sub) != -1


print(stringRotation('hello','llohe')) # multiplying 'llohe' by 2 gives 'llohellohe' which contains 'hello'