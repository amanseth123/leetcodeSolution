class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)//2
        if sum(nums)%2==1:
            return False
        def dfs(target,start):
            if target==0:
                return True
            if target<0:
                return False
            if target in dp:
                return False
            for i in range(start,len(nums)):
                if dfs(target-nums[i],i+1) or dfs(target,i+1):
                    return True
            dp[target]=False
            return dp[target]
        dp={}
        return dfs(target,0)
        
    def canPartition3(self, nums: List[int]) -> bool:
        target = sum(nums)//2
        if sum(nums)%2==1:
            return False
        dpSet = set()
        dpSet.add(0)
        for i in nums[::-1]:
            newDpSet = set()
            for n in dpSet:
                if n+i == target:
                    return True
                newDpSet.add(n+i)
                newDpSet.add(n)
            dpSet = newDpSet
        return target in dpSet
            
    
    def canPartition2(self, nums: List[int]) -> bool:
        #self.canPartition2(len(nums)-2,sum(nums)-nums[-1],nums)
        n=len(nums)
        target=sum(nums)
        if target%2!=0:
            return False
        target=target//2
        dp=[[True for _ in range(target+1)]for _ in range(len(nums)+1)]
        for i in range(1,n):
            dp[i][0]=True
            
        for i in range(1,target+1):
            dp[0][i]=False
        print(dp)
        for i in range(1,len(nums)+1):
            for j in range(1,target+1):
                if j>=nums[i-1]:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j]=dp[i-1][j]
        #print(dp)
        return dp[len(nums)][target]
                
                
                