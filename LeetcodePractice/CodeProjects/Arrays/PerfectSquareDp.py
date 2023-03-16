'''

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
'''
class Solution:
    def numSquares(self, n: int) -> int:
        dp=[n]*(n+1)
        dp[0]=0
        for targetSum in range(1,n+1):
            for j in range(1,targetSum+1):
                square = j*j
                if targetSum-square<0:
                    break
                dp[targetSum]=min(dp[targetSum],1+dp[targetSum-square])
        return dp[n]
        
        
        
        
        
        