class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = sorted(list(set(nums)))
        earn1,earn2 = 0,0
        for i in range(len(nums)):
            currEarn = nums[i]*count[nums[i]]
            #if nums[i] and nums[i-1] are difference of 1 as per question
            if i-1>=0 and nums[i]==nums[i-1]+1:
                temp = earn2
                earn2 = max(earn2,currEarn+earn1)
                earn1=temp
            else:
                temp=earn2
                earn2 = currEarn+earn2
                earn1 = temp
        return earn2
    
    # Using 1D dp
'''
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        nums = sorted(list(set(nums)))
        dp = [0]*3
        for i in range(len(nums)):
            currEarn = nums[i]*count[nums[i]]
            if i-1>=0 and nums[i]==nums[i-1]+1:
                dp[i%3] = max(dp[(i-1)%3],currEarn+dp[(i-2)%3])
            else:
                dp[i%3] = currEarn+dp[(i-1)%3]
        return dp[(len(nums)-1)%3]
'''

        
        
        
        