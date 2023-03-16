class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp={}
        globalLis,res = 0,0
        for i in range(len(nums)-1,-1,-1):
            maxLen,maxCount =  1,1
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    length,count = dp[j]
                    if length+1> maxLen :
                        maxLen,maxCount = length+1,count
                    elif length+1==maxLen:
                        maxCount+=count
            if maxLen>globalLis:
                globalLis,res = maxLen,maxCount
            elif maxLen==globalLis:
                res+=maxCount
            dp[i] = [maxLen,maxCount]
        return res                        
                        
        
        
        
        
        