# -*- coding: utf-8 -*-
"""
Students are asked to stand in non-decreasing order of heights for an annual photo. Return the 
minimum number of students that must move in order for all students to be standing in non-decreasing order of height.
"""
def heightChecker(heights):
    studentCount = 0
    for index in range(int(len(heights))): 
        if (heights[index] != sorted(heights)[index]): #compares current index to sorted index to check if they should move
            studentCount += 1
    return(studentCount)
    
import random
length = random.randint(0,100) #generates length of height list
heights = []
for x in range(length):
    heights.append(random.randint(1,10))
print(heights)
print('------------------------------------------------')
print(heightChecker(heights))
"""
Example 1:

Input: heights = [1,1,4,2,1,3]
Output: 3


Constraints:

    1 <= heights.length <= 100
    1 <= heights[i] <= 100
"""