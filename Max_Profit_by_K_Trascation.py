#You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

#Find the maximum profit you can achieve. You may complete at most k transactions.

#Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

#Input: k = 2, prices = [2,4,1]
##Output: 2
#Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

#Time COmplexity O(n)
#Space Complexity O(2n) -> O(n)
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buy = [float("inf")] * k
        sell = [float("-inf")] * k
        if len(prices) == 0 or k == 0:
            return 0
        
        for price in prices:
            buy[0] = min(buy[0],price)
            sell[0] = max(sell[0],price - buy[0])
            
            for i in range(1,k):
                buy[i] = min(buy[i],price - sell[i-1])
                sell[i] = max(sell[i],price - buy[i]) 
        return sell[k-1]
prices = [2,4,1]
k = 2
#output = 2
ans = Solution()
ans.maxProfit(k)