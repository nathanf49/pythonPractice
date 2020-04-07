"""
Given an integer, write a function to determine if it is a power of two.
"""
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        currentPower = 1
        powers = [2 ** 0]
        while powers[-1] <= n:
            powers.append(2 ** currentPower)
            currentPower += 1
        if n in powers:
            return True
        else:
            return False

test = Solution()
print(test.isPowerOfTwo(128))

"""
Example 1:

Input: 1
Output: true 
Explanation: 20 = 1

Example 2:

Input: 16
Output: true
Explanation: 24 = 16

Example 3:

Input: 218
Output: false

"""