class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        dp = [0]*3
        dp[0]=nums[0]
        dp[1] = max(nums[1],nums[0])
        for i in range(2,n):
            dp[i%3] = max(nums[i]+dp[(i%3)-2],dp[(i%3)-1])
        return dp[(n-1)%3]
        
        
        
        