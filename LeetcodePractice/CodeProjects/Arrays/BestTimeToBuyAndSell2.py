class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices )==0:
            return 0
        maxP=0
        for i in range(1,len(prices)): 
            if prices[i]>prices[i-1]:# never buy when its going down, buy low and sell high valley peak approach
                maxP+=(prices[i]-prices[i-1])
        return maxP
        
        
        
        