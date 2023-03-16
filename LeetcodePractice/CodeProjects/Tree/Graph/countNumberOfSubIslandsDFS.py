class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS,COLS=len(grid1),len(grid1[0])
        #visit=set()
        def dfs(r,c):
            if r<0 or c<0 or r==ROWS or c==COLS or grid2[r][c]==0 or grid1[r][c]==2 or grid2[r][c]==2: #if r<0 or c<0 or r==ROWS or c==COLS or grid2[r][c]==0 or (r,c) in visit
                return True 
            res=True
            if grid1[r][c]==0:# grid2[r][c]==0 and grid[r][c]==1 compare grid1 and grid2 at (1,1)
                res=False
            
            grid1[r][c]=2 #visit.add((r,c))
            grid2[r][c]=2
            res = dfs(r-1,c) and res
            res = dfs(r+1,c) and res
            res = dfs(r,c+1) and res
            res = dfs(r,c-1) and res
            return res  
        #visit=set()  
        count=0
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] and grid1[r][c]!=2 and grid2[r][c]!=2 and dfs(r,c): #if grid2[r][c] and (r,c) not in visit and dfs(r,c)
                    count+=1
        return count


# Alternative Way
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROWS,COLS=len(grid1),len(grid1[0])
        #visit=set()
        def dfs(r,c):
            if r<0 or c<0 or r==ROWS or c==COLS or grid2[r][c]==0 or grid1[r][c]==2 or grid2[r][c]==2: #if r<0 or c<0 or r==ROWS or c==COLS or grid2[r][c]==0 or (r,c) in visit
                return True 
            res=True
            if grid1[r][c]==0: # grid2[r][c]==0 and grid[r][c]==1 compare grid1 and grid2 at (1,1) confirm false no island at r,c
                res=False
            #visit.add((r,c))
            grid1[r][c]=2
            grid2[r][c]=2
            for new_r,new_c in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                res = dfs(new_r,new_c) and res
            # res = dfs(r-1,c) and res
            # res = dfs(r+1,c) and res
            # res = dfs(r,c+1) and res
            # res = dfs(r,c-1) and res
            return res  
            
        count=0
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] and grid1[r][c]!=2 and grid2[r][c]!=2 and dfs(r,c):#if grid2[r][c] and (r,c) not in visit and dfs(r,c)
                    count+=1
        return count
        
        
        
        
        
        
        
        
        
        