class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #State: buying or selling boolean
        # if buying: i+1
        # if selling: i+2 considering we have forced cooldown after buy
        dp={}
        def dfs(i,buying):
            if i>=len(prices):
                return 0
            if (i,buying) in dp:
                return dp[(i,buying)]
            if buying:
                buy = dfs(i+1,not buying)-prices[i]
                cooldown = dfs(i+1,buying) #this could also be moved before line "if buying"
                dp[(i,buying)] = max(cooldown,buy)
            else:
                sell = dfs(i+2,not buying)+prices[i]
                cooldown = dfs(i+1,buying)
                dp[(i,buying)] = max(cooldown,sell)
            return dp[(i,buying)]
        return dfs(0,True)
                
        
        
        
        