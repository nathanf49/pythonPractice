"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.
"""

def threeSum(nums):
    answers = []
    for x in nums[:-1]: # picks one number
        for y in nums[x:]: # picks another number from the following numbers
            firstTwo = x + y
            if -firstTwo in nums: # check that x and y can be zero'd
                if (x == -firstTwo) or (y == -firstTwo):
                    if nums.count(-firstTwo) < 2: # makes sure that -firstTwo isn't x or y
                        pass
                    else: # if there are enough of -firstTwo, add set
                        answers = addSet(answers, x, y, -firstTwo)
                else: # if there are enough of -firstTwo, add set
                    answers = addSet(answers, x, y, -firstTwo)

    return answers

def addSet(nums, x, y, z):
    allThree = [x, y, z]
    allThree.sort()
    if allThree not in nums:
        nums.append(allThree)
    return nums

nums = [1,2,-1,0,-1]
nums1 = [-1, 0, 1, 2, -1, -4]

"""
Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""