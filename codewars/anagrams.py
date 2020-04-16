def anagrams(word, words):
    anagram = [] # list to store the anagrams
    for currentWord in words: #goes through each word in the list
        test = word # saves a copy of our comparison word
        for letter in currentWord: #goes through each letter in the current word,
            if letter in test:
                test = test.replace(letter, '',1) #setting the first index of that letter in our comparison word to a
                #blank if it's found
            else: #adds a long, basically pointless string onto test to make sure that it won't be
                test += 'hi there Im def not an anagram for sure !!! 10000000%%% just about almost garaunteed!, but not actually for sure i guess'
        if test == '':
            anagram.append(currentWord)
    return anagram

#test = anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])# ['aabb', 'bbaa'])
test = anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer'])# ['carer', 'racer'])
print(test)