class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums) # 0 len->-1
        currMin,currMax = 1,1
        for n in nums:
            if n==0:
                currMin,currMax=1,1
                continue # next iteration i for loop
            temp = currMax*n
            currMax  = max(currMax*n,currMin*n,n) # why n-> [-1,8] currMax=8 not -8
            currMin = min(temp,currMin*n,n) # replacing currMax*n with temp with older currMax value bc we don't want updated currMax value to use here
            res = max(res,currMax)
        return res
            
        
        
        
        
        
        