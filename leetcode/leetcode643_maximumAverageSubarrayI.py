# -*- coding: utf-8 -*-
"""
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average 
value. And you need to output the maximum average value.
"""
def findMaxAverage(nums, k):
    check = 0 #holds current average
    array = nums[:k] #array starts with
    maxAverage = sum(array) #holds max average found
    for num in range(k,len(nums)):
        array.append(nums[num]) #appends next num
        if array[k] > array[0]: #if next num is greater than num being removed
            del array[0] #delete the number and save the new score
            check = sum(array)
            if check > maxAverage:
                maxAverage = check
        else:
            del array[0] #ignore calculations
    return(maxAverage/k)
    '''
    for start in range(len(nums)-k+1):
        checkAverage = sum(nums[start:start+k])/k #finds average of subarray
        if checkAverage > maxAverage: #saves current if greater than max
            maxAverage = checkAverage
    return(maxAverage)
    '''
import random
nums = []
arrayLength = random.randint(0,30000)
k = random.randint(0,arrayLength)
for x in range(arrayLength):
    nums.append(random.randint(-10000,10000))

print(findMaxAverage(nums,k))
"""
Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

Note:
    1 <= k <= n <= 30,000.
    Elements of the given array will be in the range [-10,000, 10,000].
"""