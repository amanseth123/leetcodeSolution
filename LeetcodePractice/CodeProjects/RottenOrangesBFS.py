class Solution:
    # using normal bfs 
    #using bfs with the concept we use in trees assigning every node its layer value and then it acts as a time 
    def orangesRotting2(self, grid: List[List[int]]) -> int:
        q=[]
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((i,j,0))
                if grid[i][j]==1:
                    count+=1
        step=0
        while q:
            i,j,step=q.pop(0)
            for r,c in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                #result=max(result,step)
                if 0<=r<len(grid) and 0<=c<len(grid[0]) and grid[r][c]==1:
                    grid[r][c]=2
                    count-=1
                    q.append((r,c,step+1))
                   
        print(count)
        if count>0:
            return -1
        else:
            return step


    # using multi source bfs layerwise
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=[]
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    count+=1
        step=0
        while q and count>0:
            for _ in range(len(q)):
                r,c = q.pop(0)
                for newR, newC in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                    if newR<0 or newC<0 or newR==len(grid) or newC==len(grid[0]) or grid[newR][newC]!=1:
                        continue
                    grid[newR][newC]=2
                    count-=1
                    q.append((newR,newC))
            step+=1
        return step if count==0 else -1