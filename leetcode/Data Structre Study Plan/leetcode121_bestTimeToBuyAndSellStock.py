class Solution:
    def maxProfit(prices: [int]) -> int:
        maxProfit = 0
        prices.reverse()  # reversing prices lets me use .pop() for each iteration instead of making a new list
        for i in range(len(prices)):
            highestPrice = max(prices)
            if highestPrice - prices[-1] > maxProfit:
                maxProfit = highestPrice - prices[
                    -1]  # -1 will always be the last element in prices even thou index is changing
            prices.pop()  # pops the previous days out of the list

        return maxProfit
    

if __name__ == '__main__':
    Solution.maxProfit([7,6,4,3,1])
    
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""