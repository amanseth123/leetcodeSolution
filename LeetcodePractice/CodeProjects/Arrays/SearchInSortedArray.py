class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return -1
        low,high=0,len(nums)-1
        n=len(nums)
        while low<high:
            mid=(low+(high-low+1)//2)
            if nums[0]>nums[mid]:
                high=mid-1
            else:
                low=mid
        p=low
        print(p)
        if nums[0]<=target<=nums[p]:
            low=0
            high=p
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    return mid
                if nums[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
            # if nums[low]==target:
            #     return low
        else:
            low=p+1
            high=n-1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]==target:
                    return mid
                if nums[mid]>=target:
                    high=mid-1
                else:
                    low=mid+1
            # if nums[high]==target:
            #     return high
        return -1
    def search2(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return -1
        l,r  = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            #left sorted portion
            if nums[l]<=nums[mid]:
                if target>nums[mid] or target<nums[l]:
                    l = mid+1
                else:
                    r = mid-1
            #right sorted portion
            else:
                if target<nums[mid] or target>nums[r]:
                    r = mid-1
                else:
                    l = mid+1
        return -1
        