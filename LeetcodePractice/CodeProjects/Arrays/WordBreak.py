class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(s):
            if s in memo:
                return memo[s]
            if s == "":
                return True
            doesBreak = False
            for word in wordDict:
                if s.startswith(word):
                    if dfs(s[len(word):]):
                        doesBreak = True         
            memo[s] = doesBreak
            return memo[s]
        return dfs(s)
    def fun(self,dp,s,wordDict,n):
        for i in range(n-1,-1,-1):
            t=""
            for j in range(i,n):
                t+=s[j]
                if t not in wordDict:
                    continue
                if dp[j+1]:
                    dp[i]=True
                    break
        return dp[0]
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[False]*(n+1)
        dp[n]=True
        return self.fun(dp,s,wordDict,n)
        
        
        
        
        
        
        