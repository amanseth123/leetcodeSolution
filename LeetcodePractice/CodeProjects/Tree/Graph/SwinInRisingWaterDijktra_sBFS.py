class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N=len(grid)
        visit=set()
        minHeap = [(grid[0][0],0,0)]
        # visit.add((0,0))
        while minHeap:
            t,r,c = heappop(minHeap)
            if r==N-1 and c==N-1:
                return t
            #cannot add visit here because (0,0) already visited in minHeap
            for new_r, new_c in [(r+1,c),(r,c+1),(r-1,c),(r,c-1)]:
                if 0<=new_r<N and 0<=new_c<N and (new_r,new_c) not in visit:
                    visit.add((new_r,new_c)) #when we follow a specific path we don't want it to be visited again that's why we add it into the visit set 
                    heappush(minHeap,(max(t,grid[new_r][new_c]),new_r,new_c))
# we want min of max height across all path because we need to wait until time 
# t(suppose t at r,c) for any value in the path and ultimately we need max of all values
#  in the path because we will then have to wait until that time to reach it  
                
        
        
        
        
        
                    
        
ob = Solution()
print(ob.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))