def numSteps(s: str):
    num = int(s, 2)  # convert from binary to integer
    steps = 0
    while num != 1:
        if num % 2 != 0:  # if number is odd, increase by 1
            num += 1
            steps += 1
        # number is even, divide by 2
        num = num // 2  # must do int division to avoid buffer overflow
        steps += 1
    return steps

test = "1111011110000011100000110001011011110010111001010111110001" # 85

"""
Given a number s in their binary representation. Return the number of steps to reduce it to 1 under the following rules:

    If the current number is even, you have to divide it by 2.

    If the current number is odd, you have to add 1 to it.

It's guaranteed that you can always reach to one for all testcases.

 

Example 1:

Input: s = "1101"
Output: 6
Explanation: "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14. 
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.  
Step 5) 4 is even, divide by 2 and obtain 2. 
Step 6) 2 is even, divide by 2 and obtain 1.  

Example 2:

Input: s = "10"
Output: 1
Explanation: "10" corressponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.  

Example 3:

Input: s = "1"
Output: 0
"""