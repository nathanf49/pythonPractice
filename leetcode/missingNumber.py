import numpy as np
def missingNumber(nums):
    if nums == [0]:
        return 1
    diff = list(np.setdiff1d(list(range(max(nums) + 1)), nums)) #finds difference between range from 0 to max and nums

    if diff == []:
        return max(nums) + 1
    return diff[0]

def missingNumber2(nums):
    if nums == []:
        return 0

    if nums == [0]:
        return 1

    for x in range(max(nums) + 1): # goes through all numbers to find what isn't there
        if x not in nums:
            return x

    return max(nums) + 1

"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2

Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""