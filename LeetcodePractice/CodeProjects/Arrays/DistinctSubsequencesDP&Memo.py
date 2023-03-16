class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache={}
        def dfs(i,j):
            if j==len(t):
                return 1
            if i==len(s):
                return 0
            if (i,j) in cache:
                return cache[(i,j)]
            if s[i]==t[j]:
                cache[(i,j)] = dfs(i+1,j+1)+dfs(i+1,j) # we cannot increment j(of t) unless we increment s also because t is what we want to achieve and we cannot skip any character
            else:
                cache[(i,j)] = dfs(i+1,j) # look for other part of the string s
            return cache[(i,j)]
        return dfs(0,0)
        #time complexity: O(n*m) n=len(s), m=len(t) same is the space complexity as well
        
        
        
    def numDistinct2(self, s: str, t: str) -> int:
        dp = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
        
        # set right column to 1
        for i in range(len(s)+1): # string t is empty
            dp[i][-1] = 1
        #print(dp)
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i]==t[j]:
                    dp[i][j]=dp[i-1][j]+dp[i-1][j-1]
                else:
                    dp[i][j]=dp[i-1][j]
        #for i in reversed(range(len(s))):
            #for j in reversed(range(len(t))):
                #if s[i] == t[j]:
                    #dp[i][j] = dp[i+1][j] + dp[i+1][j+1]
                #else:
                    #dp[i][j] = dp[i+1][j]
        #print(dp)
        return dp[len(s)-1][len(t)-1]
        