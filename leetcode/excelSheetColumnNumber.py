def titleToNumber(s):
    # index alphabet, blank at the beginning because arrays start at 0, but column numbers don't
    alphabet = ['','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    columnNum = 0
    letterIndex = 0
    for letter in s[::-1]: # goes through s letter by letter in reverse
        columnNum += alphabet.index(letter) * (26 ** letterIndex)
        letterIndex += 1
    return columnNum



"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

Example 1:
Input: "A"
Output: 1

Example 2:
Input: "AB"
Output: 28

Example 3:
Input: "ZY"
Output: 701



Constraints:

    1 <= s.length <= 7
    s consists only of uppercase English letters.
    s is between "A" and "FXSHRXW".


"""