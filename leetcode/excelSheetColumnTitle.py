from excelSheetColumnNumber import titleToNumber

def convertToTitle(n):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                'U', 'V', 'W', 'X', 'Y', 'Z']
    out = '' # output string of letters
    spacesNeeded = 1 # will need at least one letter to return the column number, may need more than 1
    maximum = 26  # maximum counts the max with all spaces as Z
    while maximum < n:
        spacesNeeded += 1  # if the number can not be displayed, add another space to the number of spaces needed
        maximum += 26 ** spacesNeeded  # each space added can contain (26 ^ space number) * letter index and the rest of the spaces contain what was already in maximum

    while spacesNeeded > 1:
        currentLetter = 1 # will always have to move the index back one to get the actual letter
        while (currentLetter + 1) * (26 ** (spacesNeeded - 1)) < n: # if the next letter can still fit in n, move onto it
            currentLetter += 1
        n -= currentLetter * (26 ** (spacesNeeded - 1))
        spacesNeeded -= 1
        out += alphabet[currentLetter - 1]

    # for last space, just add the index of n
    out += alphabet[n-1]

    return out



"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...

Example 1:
Input: 1
Output: "A"

Example 2:
Input: 28
Output: "AB"

Example 3:
Input: 701
Output: "ZY"
"""