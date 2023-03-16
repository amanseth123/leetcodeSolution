class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def numWays(self, n, k) -> int:

        dp = [0 for i in range(n)]
        
        if n == 0: return 0
        if n == 1: return k 
        if n == 2: return k * k
        if k == 1: return 0
        
        dp[0] = k
        dp[1] = k * k        
        for i in range(2,len(dp)):
            dp[i] = dp[i-1] * (k-1) + dp[i-2] * (k-1)
        return dp[n-1]