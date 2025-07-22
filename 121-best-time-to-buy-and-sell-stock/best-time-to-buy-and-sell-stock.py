class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        profit=0
        for i in range(len(prices)):
           # cost = prices[i] -mini
            profit= max(profit, prices[i] -mini)
            mini=min(prices[i],mini)
        return profit    

        