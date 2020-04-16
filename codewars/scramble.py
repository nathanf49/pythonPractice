def scramble(s1, s2):
    for letter in s2:
        if letter in s1: #removes every letter in s2 from s1 if letters are valid
            s1.replace(letter,'',1) #replaces letter with nothing if it is available
        else: #if letter is not available in s1, it cannot be unscrambled to s2
            return False
    return True #if the loop is successfully completed, s1 has the chars to make s2

test = scramble('dzywcrzbhg', 'fdsbemqyuwturgtyy')
print(test)