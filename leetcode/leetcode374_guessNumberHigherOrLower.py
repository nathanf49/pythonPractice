"""
374. Guess Number Higher or Lower
Easy
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I'll tell you whether the number is higher or lower.
You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):
-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
"""


# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:
def guessNumber(n):
    high = n + 1  # sets bounds 1 outside of max and minbecause it's faster to binary search the start and end than
    # check them manually
    low = 0
    while guess(int((high + low) / 2)) != 0:
        if guess(int((high + low) / 2)) == 1:  # guess is too low
            low = int((high + low) / 2)  # makes min the guess that was too low
        elif guess(int((high + low) / 2)) == -1:  # guess is too high
            high = int((high + low) / 2)  # makes max the guess that was too high
    return int((high + low) / 2)


def guess(num):
    if myNumber < num:
        return -1
    elif myNumber > num:
        return 1
    else:
        return 0


import random

intMax = 7
myNumber = 1
print(guessNumber(intMax))
"""
Example :
Input: n = 10, pick = 6
Output: 6
"""
