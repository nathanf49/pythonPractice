# -*- coding: utf-8 -*-
"""
Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to A[i] interpreted as a binary number 
(from most-significant-bit to least-significant-bit.)
Return a list of booleans answer, where answer[i] is true if and only if N_i is divisible by 5.
"""
def prefixesDivBy5(A):
    out = [] #output list
    total = 0 #value for storing total as we move through binary number
    zeroCount = 0
    for element in A:
        if element == 1:
            break
        else:
            zeroCount += 1
            out.append(True)
    for i in range(zeroCount):
        A.remove(0)
    for element in A: #uses bit shifting starting from the first one to double the total 
        total *= 2 #each time and add 1 if there is a new one
        if element == 1:
            total += 1
        if total % 5 == 0: #checks divisibility for total on each loop
            out.append(True)
        else:
            out.append(False)
    return(out)
    
import random       
A = []
for x in range(0,30000):
    A.append(random.randint(0,1))
A = [0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,1,0,1,1,1,0,0,0,0,0,1,0,1,1]
print(prefixesDivBy5(A))
"""
Input:
[0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,1,0,1,1,1,0,0,0,0,0,1,0,1,1]
Expected:
[true,false,false,true,true,true,false,false,false,false,false,false,false,false,false,true,true,false,false,false,false,false,false,false,false,false,false,false,true]

Example 1:
Input: [0,1,1]
Output: [true,false,false]
Explanation: 
The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.  Only the first number is divisible by 5, so answer[0] is true.

Example 2:
Input: [1,1,1]
Output: [false,false,false]

Example 3:
Input: [0,1,1,1,1,1]
Output: [true,false,false,false,true,false]

Example 4:
Input: [1,1,1,0,1]
Output: [false,false,false,false,false]

Note:
    1 <= A.length <= 30000
    A[i] is 0 or 1
"""