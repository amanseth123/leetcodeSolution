class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currSum = 0
        for n in nums:
            if currSum<0:# if currSum is negative then we don't need to consider it and we can discard every element that contributed to negative sum
                currSum=0
            currSum+=n # take up the sum and and check if its negative in next iteration
            maxSub = max(maxSub,currSum)
        return maxSub
    def maxSubArray2(self, nums: List[int]) -> int:
        
        n=len(nums)
        dp=[0]*n
        dp[0]=nums[0]
        for i in range(1,n):
            dp[i]=max(nums[i]+dp[i-1],nums[i]) # we cannot have dp[i-1] because then the subarray will not be contiguous
            
        print(dp)
        return max(dp)
            
            