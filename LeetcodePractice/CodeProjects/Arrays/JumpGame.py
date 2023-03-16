class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        if 0 not in nums :
            return True
        else:
            reachable=0
            for i in range(n):
                if reachable < i:
                    return False
                reachable=max(reachable,nums[i]+i)
            return True