def isPalindrome(aString):
    '''
    aString: a string,
    determines if string is a palindrome (returns True) or not (returns False)
    '''
    for pos in range(len(aString)):
        if aString[pos] != aString[len(aString)-pos-1]:
            return False
    return True

def longestRun(L):
    '''
    L: a list,
    determines the longest run in which the elements of L are not decreasing while stepping through L
    '''
    maxRun, currentRun = 1,1
    for pos in range(len(L)-1):
        if L[pos + 1] < L[pos]: #if next element is less than current element
            currentRun = 1 #reset current run, different than initialization because if this is reset we do have elements in the list
        else:
            currentRun += 1
            if currentRun > maxRun: #saves high score
                maxRun = currentRun
    return maxRun

def cipher(map_from, map_to, code):
    """
    map_from, map_to: strings where each contain N unique lowercase letters.
    code: string (assume it only contains letters also in map_from)
    Returns a tuple of (key_code, decoded).
    key_code is a dictionary with N keys mapping str to str where
    each key is a letter in map_from at index i and the corresponding
    value is the letter in map_to at index i.
    decoded is a string that contains the decoded version
    of code using the key_code mapping.
    """
    key_code = {}
    decoded = ''
    for letterIndex in range(len(map_from)):
        key_code[str(map_from[letterIndex])] = map_to[letterIndex]
    for letter in code:
        decoded += key_code[letter]
    return (key_code, decoded)
