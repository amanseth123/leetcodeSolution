class Solution:
    def jump(self, nums: List[int]) -> int:
        res=0
        l,r = 0,0
        while r<len(nums)-1:
            farthest = 0
            for i in range(l,r+1): # iterate through left to right to determine who can go farthest
                farthest  =max(farthest,i+nums[i])
            l=r+1 #shift the left to right +1 that's new left out of the window l:r
            r=farthest # and r will reach the farthest 
            res+=1 # calculate number of jumps
        return res
    
            
        
        