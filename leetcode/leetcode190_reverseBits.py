"""
Reverse bits of a given 32 bits unsigned integer.
"""


def reverseBits(n):
    return int('{:032b}'.format(n)[::-1], 2) # converts to a string in the format of 32 bit binary, reverses the
    # string, and converts to an integer


example1 = int("00000010100101000001111010011100", 2)
example2 = int("11111111111111111111111111111101", 2)
reverseBits(example1)
reverseBits(example2)

"""
Example 1:

Input: 00000010100101000001111010011100 Output: 00111001011110000010100101000000 Explanation: The input binary string 
00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary 
representation is 00111001011110000010100101000000. 

Example 2:

Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so 
return 3221225471 which its binary representation is 10111111111111111111111111111111
"""
