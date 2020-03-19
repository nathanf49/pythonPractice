"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
"""

def maxSubArray(self, nums: List[int]) -> int:
        maxSum = max(nums)  #default max is highest single number
        for x in range(len(nums)): #x will step through nums from the start to the end
            while nums[x] <= 0 and x < len(nums)-1: #skips negative numbers from x direction
                x += 1
            for y in range(len(nums),x,-1): #y will step from the end of nums up to x
                while nums[y-1] <= 0 and y-1>x: #has to be -1 because nums[x:y] goes up to y, not including y
                    y -= 1 #skips negative numbers from y direction
                if sum(nums[x:y]) > maxSum:
                    maxSum = sum(nums[x:y])
        return maxSum

"""
Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""