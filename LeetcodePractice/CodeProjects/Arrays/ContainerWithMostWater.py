class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        l,r = 0,len(height)-1
        while l<r:
            maxArea = max(maxArea,(r-l)*min(height[l],height[r]))
            if height[l]<height[r]:
                l+=1
            elif height[l]>height[r]:# when height[l] is more better decrement the right pointer to get more height
                r-=1
            else: # when both heights are all same 
                l+=1
                r-=1
        return maxArea
        
        
        
        