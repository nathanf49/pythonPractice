# O(n)
"""
String Compression: Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2blc5a3, If the "compressed" string would not become smaller than the
original string, your method should return the original string. You can assume the string has only uppercase and
lowercase letters (a - z)
"""


def stringCompression(string):
    if len(string) < 2:
        return string  # string of length 0 or 1 will not compress

    out = string[0] + '1'
    count = 1
    for letter in string[1:]:  # goes over all letters except the first since that's already in out
        if letter == out[-(len(str(count)) + 1)]:  # last letter found will be right before the count
            out = out[0:len(out) - len(str(count))] + str(int(out[-len(str(count)):]) + 1)  # increments count if last letter is the same
            count += 1
        else:
            out += letter + '1'  # if there's a new letter, add the letter and start count at 1
            count = 1

    if len(out) >= len(string):
        return string  # returns original string if the compressed version is not shorter
    else:
        return out


test = stringCompression('aabcccccaaa')  # given example
test1 = stringCompression('abcdefg')  # changes letter every time, so compressed is longer, should return original
test2 = stringCompression('')  # blank string
test3 = stringCompression('hi')  # length is 2, so 'compressed' will be 4, should return original
test4 = stringCompression('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')  # all the same char, length of count is 3 digits
test5 = stringCompression('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab')  # has a diff char at the end, a has count of 2 chars
test6 = stringCompression('aabbccdd')  # same length as compressed, should return orginal
