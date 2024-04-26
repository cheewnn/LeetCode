class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]
        for i in range(len(prices)-1):
            if buy < prices[i]:
                buy = prices[i]
            if prices[i+1]-prices[i] > 0:
                maxProfit += prices[i+1]-prices[i]
            else:
                buy = prices[i]
        return maxProfit
            
        