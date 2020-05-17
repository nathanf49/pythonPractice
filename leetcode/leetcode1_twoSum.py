"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dict = {}
    for i in range(len(nums)):
        if target - nums[i] not in dict:  # if pair to i (nums[i] + target-nums[i] = target) is not in the dictionary
            dict[nums[i]] = i  # saves value of index
        else:
            return [dict[target - nums[i]],
                    i]  # returns the index of the match and the current index when match is found


"""
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
