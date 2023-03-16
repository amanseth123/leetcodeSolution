class Solution:
    def mincostTickets(self, days, costs):
        dayset = set(days)
        durations = [1, 7, 30]
        @lru_cache(None)
        def dp(i):
            if i > max(days): # or i>365
                return 0
            elif i in dayset:
                return min(dp(i + d) + c
                           for c, d in zip(costs, durations))
            else:
                return dp(i + 1)

        return dp(1)
    def mincostTickets2(self, days: List[int], costs: List[int]) -> int:
        dp={}
        def dfs(index):
            if index==len(days):
                return 0
            if index in dp:
                return dp[index]
            dp[index] = float("inf")
            for c,d in zip(costs,[1,7,30]):
                j = index
                while j<len(days) and days[j]<days[index]+d:
                    j+=1
                print(j,index,c,d)
                dp[index] = min(dp[index],dfs(j)+c)
            return dp[index]
        return dfs(0)
        
        
        