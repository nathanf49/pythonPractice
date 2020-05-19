# O(n)

"""
There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a
character. Given two strings, write a function to check if they are one edit (or zero edits) away.
"""


def oneAway(string1, string2):
    if string1 == string2:  # 0 edits away
        return True
    fromFront = sameLength(string1, string2)  # counts how far letters are the same
    fromBack = sameLength(string1[::-1], string2[::-1])  # counts how far letters are the same in reversed versions of
    # the strings
    if string1[:fromFront] + string1[::-1][:fromBack] == string2[:fromFront] + string2[::-1][:fromBack] and (
            len(string1[:fromFront] + string1[::-1][:fromBack]) + 1 == len(string1) or len(
            string2[:fromFront] + string2[::-1][:fromBack]) + 1 == len(string2)):
        # checks that once all replaced/removed/inserted characters are taken out, the strings are the same and 1 of
        # them only had 1 char changed, whether that char was inserted, removed, or replaced
        return True
    else:
        return False


def sameLength(string1, string2):
    for pos in range(1, len(string1) + 1):
        if string1[:pos] == string2[:pos]:
            pass  # just keep going until there is a difference, this function won't run if there is no diff,
            # so it will return something
        else:
            return pos - 1  # once the strings don't match, return how far they did match
    return len(string1)  # will only reach here if string 2 is longer than string 1 and in that case it can only be an
    # extra letter inserted or removed from the end


# Working
# True Tests
test1 = oneAway('nathan', 'nathan')  # test same string
test2 = oneAway('nathan', 'nathen')  # replace char with 1 char
test3 = oneAway('nathan', 'nathaen')  # replace char with more than 1 char
test4 = oneAway('nathan', 'nathan1')  # char inserted at end of string 2 / removed from end of string 1
test5 = oneAway('nathan', '1nathan')  # char inserted at beginning of string 2 / removed from start of string 1
test6 = oneAway('nathan', 'nat1han')  # char inserted in middle of string 2 / removed from middle of string 1
test7 = oneAway('nathan1', 'nathan')  # char inserted at end of string 1 / removed from end of string 2
test8 = oneAway('1nathan', 'nathan')  # char inserted at start of string 1 / removed from start of string 2
test9 = oneAway('nat1han', 'nathan')  # char inserted in middle of string 1 / removed from middle of string 2
test14 = oneAway('nathan', 'natha123')  # replaces last char of string 2 with 3 chars
test15 = oneAway('nathan', '123athan')  # replaces first char of string 2 with 3 chars
test16 = oneAway('123athan', 'nathan')  # replaces first char of string 1 with 3 chars
test17 = oneAway('natha123', 'nathan')  # replaces last char of string 1 with 3 chars

# False Tests
test10 = oneAway('nathan', 'nethen')  # replaces letters in 2 positions
test11 = oneAway('nathan', 'nahtan')  # replaces a letter in both center positions
test12 = oneAway('nathan', 'nathan123')  # inserts more than 1 letter in string 2 / removes more than 1 from string 1
test13 = oneAway('nathan123', 'nathan')  # inserts more than 1 letter in string 1 / removes more than 1 from string 2
