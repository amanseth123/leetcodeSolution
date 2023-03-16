'''
import math
class Solution:
    def integerBreak(self, n: int) -> int:
        def prod(a):
            return math.prod(a)
        def helper(arr,index,temp,target,product):
            if index>len(arr) or sum(temp)>target:
                return 
            if sum(temp)==target and len(temp)>=2:
                #x=prod(temp)
                #print(temp)
                if product>self.m:
                    self.m=max(self.m,product)
                return
            for i in range(index,target):
                helper(arr,i,temp+[arr[i]],target,product*arr[i])
                #helper(arr,i+1,temp,target)
   
        arr=list(range(1,n+1))
        target=n
        #self.res=[]
        self.m=-1
        helper(arr,0,[],target,1)
        return self.m

class Solution:
    def integerBreak(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[2]=1
        for i in range(3,n+1):
            for j in range(1,i-1):
                dp[i]=max(dp[i],j*max(i-j,dp[i-j]))
        return dp[-1]
'''
class Solution:
    def integerBreak(self, n: int) -> int:
        dp={1:1}
        if n in dp:
            return dp[n]
            
        for nums in range(2,n+1):
            dp[nums] = 0 if nums==n else nums
            for i in range(1,nums):
                val = dp[i]*dp[nums-i]
                dp[nums]= max(dp[nums],val)
        return dp[n]
                    
        #return dfs(n)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            

