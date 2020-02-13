# -*- coding: utf-8 -*-
"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
"""

def twoSum(numbers, target): #return list (index +1)
    front = 0
    back = front + 1 #start 1 after front
    while numbers[front] + numbers[back] != target:
        if numbers[front] + numbers[back] > target: #if you've gone past, start at next index for front and initialize back
            front += 1
            while numbers[front] == numbers[front-1]:
                front += 1
            back = front + 1
        elif numbers[front] + numbers[back] < target:#if you haven't reached target, increase back
            back += 1
            if back <= len(numbers)-1:
                while (numbers[back] == numbers[back-1]):
                    back += 1
            if back == len(numbers):#if back goes over length of numbers, increase front
                front += 1
                while numbers[front] == numbers[front-1]:
                    front += 1
                back = front + 1
    return(front+1, back+1)
    
numbers = [5,25,75]
target = 100
print(twoSum(numbers, target))
"""
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

    Your returned answers (both index1 and index2) are not zero-based.
    You may assume that each input would have exactly one solution and you may not use the same element twice.

"""