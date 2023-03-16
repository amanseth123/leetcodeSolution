class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res=0
        n=len(nums)
        r=n-1
        mod = 10**9 + 7
        for i,leftMin in enumerate(nums):
            while leftMin+nums[r]>target and i<=r:
                r-=1
            if i<=r:
                res+=(2**(r-i)%mod)%mod
        return res%mod