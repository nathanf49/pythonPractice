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

def missingNumber3(nums):
    if nums == []:  # base cases
        return 0
    if nums == [0]:
        return 1
    if 1 in nums and 0 not in nums:
        return 0
    nums.sort()  # get numbers in order, so nums[1] should always be nums[0] + 1
    while len(nums) > 1:  # keep at least 2 elements
        if nums[1] == nums[0] + 1:  # remove nums[0] if it's correct
            nums = nums[1:]
        else:  # return the missing number
            return nums[0] + 1
    return nums[0] + 1  # return 1 more than the last number if all numbers are there

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