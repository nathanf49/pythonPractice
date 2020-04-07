"""
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int)
        if amount > (2 * coins[-1]
            output -= coins[-1]
        if ammout > (2 * coins-2)
            output -= coins[-2]
        if amount


coins = [1,2,5]
amount = 11

test = Solution()
print(test.coinChange(coins,amount))
"""
Example 1:
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Note:
You may assume that you have an infinite number of each kind of coin.
"""