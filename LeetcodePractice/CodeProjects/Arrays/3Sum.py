class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        n=len(nums)
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:#if duplicate, skip to the next iteration
                continue
            l=i+1
            r=n-1
            temp=nums[i]
            while l<r:
                if nums[l]+nums[r]+temp==0:
                    ans.append([nums[l],nums[r],temp])
                    l+=1 # only increase l or decrease right because if we change either l or r the other one will set itself later inside the while loop
                    while l<r and nums[l]==nums[l-1]:# dont want to reuse the same value to avoid duplicate
                        l+=1
                elif nums[l]+nums[r]<(0-temp):
                    l+=1
                else:
                    r-=1
        return ans
#same as Two Sum when the array is sorted use 2 pointer approach
#Time complexity: O(nlogn)+O(n^2)