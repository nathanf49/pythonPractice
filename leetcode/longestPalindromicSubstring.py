"""
5. Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
"""

def longestPalindrome(s: str):
    palindrome = s[0]
    #checks palindromes with odd length
    for letter in range(len(s)): # loop through letters to check around each of them
        checkString = s[letter - int(len(palindrome) / 2 + 1):letter + int(len(palindrome) / 2 + 1) + 1] # start by taking 1 letter in each direction from current checking point
        while isPalindrome(checkString) and checkString != '': # keep loop going while checkString is a palindrome
            if len(checkString) > len(palindrome): # save new longest palindrome
                    palindrome = checkString
            if checkString == s[letter - int(len(palindrome) / 2 + 1):letter + int(len(palindrome) / 2 + 1) + 1]: # break if stuck in a loop
                break
            checkString = s[letter - int(len(palindrome) / 2 + 1):letter + int(len(palindrome) / 2 + 1) + 1]

    # check palindromes with even length
    for letter in range(int(len(palindrome)/2), len(s)):
        checkString = s[letter - int(len(palindrome) / 2 + 1):letter + int(len(palindrome) / 2 + 1)] # only check strings larger than current palindrome
        while isPalindrome(checkString) and checkString != '':
            if len(checkString) > len(palindrome):
                palindrome = checkString # update palindrome since it will be larger
            if checkString == s[letter - int(len(palindrome) / 2 + 1):letter + int(len(palindrome) / 2 + 1)]: # break if stuck in a loop
                break
            checkString = s[letter - int(len(palindrome) / 2 + 1):letter + int(len(palindrome) / 2 + 1)]  # check palindrome of 1 larger size

    return palindrome






def isPalindrome(string):
    middle = len(string)/2
    middle = int(middle) # integer rounds down if there are an odd number of chars
    start = string[:middle]
    if len(string) % 2 != 0: # skips center char if there are an odd number of chars
        end = string[middle+1:]
    else:
        end = string[middle:]
    return start == end[::-1] # reverses end for comparison