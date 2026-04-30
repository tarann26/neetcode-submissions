class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        j=len(prices)-1
        res=[0]*len(prices)
        buy=prices[0]
        for i in range(1,len(prices)):
            buy=min(buy,prices[i])
            res[i]=max(res[i-1],prices[i]-buy)
        return res[len(prices)-1]