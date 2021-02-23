def generate_hashtag(s):
    out = '#' # start output string with a hashtag
    words = s.strip('  ').split(' ').remove('') #strip gets rid of any space of more than 1 character and split breaks up words with spaces between them
    if words is None: # if len(words) is 0, s was blank
        return False
    for word in words:
        out += word[0].upper() # add word onto hashtag
        if len(word) > 1:
            out += word[1:].lower()
    if len(out) > 140:
        return False
    return out

test = generate_hashtag('Do  We  Have  A  Hashtag')
print(test)