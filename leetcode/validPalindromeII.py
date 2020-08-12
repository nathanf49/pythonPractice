def validPalindrome2(s):
    if s == s[::-1]: # already a palindrome without removing a character
        return True

    sReverse = s[::-1]
    for char in range(len(s)): # check all chars
        if s[char] != sReverse[char]: # found one difference
            check = s[:char] + s[char + 1:]
            if check == check[::-1]: # if removing that letter from the forward running s makes a palindrome, success
                return True
            reverseCheck = sReverse[:char] + sReverse[char + 1:]
            if reverseCheck == reverseCheck[::-1]:# if removing from the reverse makes a palindrome, success
                return True

            return False # if removing either doensn't make a palindrome, more than 1 letter must be removed


    return False


"""
 Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:

Input: "aba"
Output: True

Example 2:

Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

Note:

    The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""