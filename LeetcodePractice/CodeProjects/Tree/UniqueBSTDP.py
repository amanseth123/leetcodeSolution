class Solution:
    def numTrees(self, n: int) -> int:
        # numsTree[4] = numTree[0]*numTree[3]+  when node 0 is the root 
        #               numTree[1]*numTree[2]+  when node 1 is root we have 1 node left and 2 node right
        #               numTree[2]*numTree[1]+
        #               numTree[3]*numTree[0]
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        total=0
        for i in range(2,n+1):
            #dp[i]=0
            for j in range(i):
                dp[i]=dp[i]+dp[j]*dp[i-j-1]
        return dp[n]