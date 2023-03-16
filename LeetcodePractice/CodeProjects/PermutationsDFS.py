#from itertools import permutations as p
class Solution:
    # DFS with memoization 
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(i):
            if i==len(nums)-1:
                return [nums[:]]
            if i in dp:
                return dp[i]
            res=[]
            for j in range(i,len(nums)):
                n=nums.pop(0)
                perms = self.permute(nums) # NOTE: we call permute and not helper here to avoid list hashing
                for perm in perms:
                    perm.append(n)
                res.extend(perms)
                nums.append(n)
            dp[i]=res
            return res
        dp={}
        return helper(0)

    # purely dfs
    def permute(self, nums: List[int]) -> List[List[int]]:
        #return list(p(nums))
        res=[]
        if len(nums)==1:
            return [nums[:]]
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)  #recur for remaining popped already
            for perm in perms:
                perm.append(n) #add popped number to the permutation in last
                #print(perm,perms)
            res.extend(perms) #include in the answer
            nums.append(n) # put the number back into the nums 
        return res
                
        
        
        
        
        