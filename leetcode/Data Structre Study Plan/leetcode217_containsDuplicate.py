def containsDuplicate(self, nums: List[int]) -> bool:
    if len(set(nums)) == len(nums):
        return False  # sets contain each element once by definition so if the set is the same length as the list each num will appear once
    else:
        return True

"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true"""