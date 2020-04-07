"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:  # returns itself for 1, 2, or 3
            return n
        else:
            current = 3  # current starts at 3
            prev = 2  # holds previous result
            for x in range(3, n):
                temp = current  # saves current for prev before overwriting
                current += prev  # adds previous two answers (Fibonacci sequence)
                prev = temp  # saves last answer
            return current

sol1 = Solution()
print(sol1.climbStairs(15))

"""
Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""