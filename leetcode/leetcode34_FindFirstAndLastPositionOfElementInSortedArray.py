"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].
"""


def searchRange(nums, target):
    targetLength = nums.count(target)  # finds how many of the target number are present
    if targetLength == 0:  # return -1-1 if none are present
        return [-1, -1]
    start = nums.index(target)  # find the index of the first since we know the target is present
    if targetLength == 1:  # if we only have one instance of the target, it is both the start and end
        return [start, start]
    return [start,
            start + targetLength - 1]  # if we have more than one instance than the end will be the start + the
    # number after (or len(target)-1)


nums = [1]
nums.sort()
target = 1
print(nums)
print(searchRange(nums, target))
"""
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""
