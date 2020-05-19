# O(n)
# n a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that
# is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be
# limited to just dictionary words.

# can be a palindrome if it has an even number of each letter (except middle letter if length of string is odd)
# assuming spaces and case doesn't matter

def palindromePermuation(string):
    string = string.replace(' ', '')  # get rid of any spaces, only want to deal with chars here
    string = string.lower()  # makes all letters lowercase since case doesn't matter here
    oddAllowed = False  # variable to hold whether or not we can have an odd number of a letter
    if (len(string) % 2) != 0:  # if string length is odd
        oddAllowed = True  # Will be true if string length without spaces is odd and no odd count has been found yet
    checked = []  # a list of the letters that have already been checked to avoid killing the oddAllowed in odd cases
    # more than 1
    for letter in string:
        if letter not in checked:  # will only check each letter once, if the letter has already come up it will be
            # skipped
            checked.append(letter)
            if (string.count(letter) % 2) != 0:  # if letter count is odd
                if oddAllowed == False:  # returns false if there is an odd count of a letter when there shouldn't
                    # be. Makes a permutation impossible
                    return False
                else:  # oddAllowed will be true if the string length is odd and this is the first odd count,
                    # but this must be the only odd count, so set oddAllowed to False
                    oddAllowed = False
    return True


test = 'aa bb cC Dddd eeffF'
