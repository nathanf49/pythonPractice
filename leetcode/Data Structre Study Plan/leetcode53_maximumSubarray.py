# times out on leetcode but I'm not sure why since it only hits each element once
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subarray = []
        subIndex = 0
        maxTotal = -99999999999999999
        for i in nums:
            subarray.append(i)
            if sum(subarray) > maxTotal:
                maxTotal = sum(subarray)

            if sum(subarray) <= 0:  # if this part of the subarray is 0 or negative it won't help raise the max Sum
                subarray = []

        return maxTotal


"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part+
 
 of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""