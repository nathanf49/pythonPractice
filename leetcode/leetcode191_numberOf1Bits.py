"""
Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).
"""

def hammingWeight(n):
    return str(bin(n)).count("1") # convert from decimal to binary to string and count 1's

example1 = 0o0000000000000000000000000001011
example2 = 0o0000000000000000000000010000000
example3 = 0o11111111111111111111111111111101

"""
Example 1:

Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example 2:

Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Example 3:

Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
"""