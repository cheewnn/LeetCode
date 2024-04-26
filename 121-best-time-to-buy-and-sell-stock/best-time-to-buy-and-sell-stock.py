class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0]
            
        for i in range(len(prices)-1): #until 2nd last elem
            if prices[i]<buy:
                buy = prices[i]
            if (prices[i+1]-buy) > maxProfit:
                maxProfit = (prices[i+1]-buy)
            print(maxProfit)

            
        return maxProfit