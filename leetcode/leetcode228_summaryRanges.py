# -*- coding: utf-8 -*-
"""
Given a sorted integer array without duplicates, return the summary of its ranges.
"""
def summaryRanges(nums):
    out = []
    if nums == []:
        return(nums)
    if (len(nums) == 1):
        return([str(nums[0])])
    end = min(nums)-1 #initialize end for start of condition to check if we are past end later on
    for x in nums:#range(min(nums),max(nums)+1):
        if (x in nums) and (x > end): #if number is in nums and we are past end of previous range we checked
            start = x
            if x + 1 in nums: #find out if the range continues
                while x + 1 in nums: #find how far the range continues
                    x+=1
            end = x 
            if end <= start: #single number case
                out.append(str(start))
            else: #range case
                out.append(str(start) + '->' + str(end)) 
    return(out)
      
import random
#nums = [-2147483648,-2147483647,2147483647]
nums = [-1]
for x in range(10):
    nums.append(random.randint(max(nums)+1,max(nums)+2))
print(nums)
print(summaryRanges(nums))
"""
Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.

Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
"""