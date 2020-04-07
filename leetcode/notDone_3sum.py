"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answers = []
        for x in nums:
            for y in nums:
                if y is not x and -(x+y) is not y and x is not -(x+y):
                    if -(x+y) in nums:
                        if [x,-(x+y), y] not in answers and [y,x,-(x+y)] not in answers and [x,y,-(x+y)] not in answers and [y,-(x+y),x] not in answers and [-(x+y),x,y] not in answers and [-(x+y),y,x] not in answers:
                            answers.append([x,y,-(x+y)])
        return answers

test = Solution()
print(test.threeSum(nums = [-1, 0, 1, 2, -1, -4]))
"""
Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""