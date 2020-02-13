# -*- coding: utf-8 -*-
"""
Given an array of 2n integers, your task is to group these integers into n pairs of integer, 
say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible. 
"""
def arrayPairSum(nums):
    nums.sort()
    return(sum(nums[0:len(nums:2]))
nums = []
import random
numsLen = random.randint(1,10000)
for i in range(2*numsLen):
    nums.append(random.randint(-10000,10000))
print(arrayPairSum(nums))    
"""
Example 1:
Input: [1,4,3,2]
Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).

Note:
    n is a positive integer, which is in the range of [1, 10000].
    All the integers in the array will be in the range of [-10000, 10000].
"""