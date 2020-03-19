"""Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product
of all the elements of nums except nums[i]. """
from operator import mul
from functools import reduce


def productExceptSelf(nums):
    output = []  # creates list for products
    for x in range(len(nums)):
        temp = nums[x]  # saves copy of current nums[x] for temporary removal
        del nums[x]  # temporarily removes nums[x]
        product = reduce(mul,
                         nums)  # applies the multiplication operator to all elements of nums (multiplies all elements)
        output.append(product)  # appends product to output list
        nums.insert(x, temp)  # inserts removed number back into list
    return output


"""
Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""
