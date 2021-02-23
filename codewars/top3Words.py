def top_3_words(text):
    text = text.lower() # matches are case insensitive and should be returned lowercase anyway
    validChars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',"'"," "]
    for char in text: # remove invalid chars
        if char not in validChars:
            text = text.replace(char, '')
    text = text.split(' ') # splits words
    while '' in text:
        text.remove('')
    words = [' ', ' ', ' '] # top 3 words
    values = [0, 0, 0] # top 3 values
    validChars.remove("'")
    for word in text:
        if word in words: # skip words that have already been covered
            skip = True
        else:
            skip = False
        if "'" in word and skip == False:
            if any(ele in word for ele in validChars):
                skip = False
            else:
                skip = True
        if skip == False:
            if text.count(word) > values[0]: # current word is new #1 word
                words = [word, words[0], words[1]]
                values = [text.count(word), values[0],values[1]]
            elif text.count(word) > values[1]: # new #2 word
                words = [words[0], word, words[1]]
                values = [values[0], text.count(word), values[1]]
            elif text.count(word) > values[2]: # new #3 word
                words = [words[0], words[1], word]
                values = [values[0],values[1], text.count(word)]


    while ' ' in words: # remove the spaces put in to hold the 3 spots at the start
        words.remove(' ')

    return words


text = """  //wont won't won't """

if __name__ == '__main__':
    x = top_3_words(text)

# Works for my tests, sample tests don't break ties arbitrarily and split words in nonsensical ways

"""
Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, in descending order of the number of occurrences.
Assumptions:

    A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII. (No need to handle fancy punctuation.)
    Matches should be case-insensitive, and the words in the result should be lowercased.
    Ties may be broken arbitrarily.
    If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.

Examples:

top_3_words("In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.")
# => ["a", "of", "on"]

top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# => ["e", "ddd", "aa"]

top_3_words("  //wont won't won't")
# => ["won't", "wont"]
"""