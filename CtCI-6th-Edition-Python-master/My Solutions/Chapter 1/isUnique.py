# O(n)
def uniqueChars(x):
    for char in x:
        if char in x.replace(char, '', 1):  # replaces the first instance of the current char with a blank, effectively
            # removing it for the pass through #checks if char is still in x after being removed
            return False
    return True  # made it to the end of the loop without finding duplicate chars

# O(n)
def uniqueCharsV2(x):
    for char in x:
        if x.count(char) != 1:  # goes char by char, checking each char appears once
            return False
    return True
