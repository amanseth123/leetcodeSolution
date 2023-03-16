class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        ROWS,COLS = len(matrix),len(matrix[0])
        def inside(r,c):
            return 0<=r<ROWS and 0<=c<COLS
        dp={}
        def dfs(r,c,prevValue):
            if r<0 or c<0 or r==ROWS or c==COLS or matrix[r][c]<=prevValue:
                return 0
            if (r,c) in dp:
                return dp[(r,c)]
            res = 1+max(dfs(r+1,c,matrix[r][c]),dfs(r-1,c,matrix[r][c]),dfs(r,c+1,matrix[r][c]),dfs(r,c-1,matrix[r][c]))
            dp[(r,c)] = res
            return res
            
        maxValue = -1
        for r in range(ROWS):
            for c in range(COLS):
                maxValue = max(maxValue,dfs(r,c,-1))
        return maxValue
'''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def inside(r,c):
            return 0<=r<R and 0<=c<C
        queue=[]
        R=len(matrix)
        C=len(matrix[0])
        for i in range(R):
            for j in range(C):
                queue.append((matrix[i][j],i,j))
        ans=0
        queue.sort()
        print(queue)
        distance=[[1 for _ in range(C)] for _ in range(R)]
        for q in queue:
            r=q[1]
            c=q[2]
            ans=max(ans,distance[r][c])
            # going from row-1 to row+1(inclusive) is same as visiting neighbours
            for row in range(r-1,r+2): 
                for col in range(c-1,c+2):
                    if abs(r-row)+abs(c-col)==1 and inside(row,col):
                        if matrix[row][col]>matrix[r][c]:
                            distance[row][col]=max(distance[row][col],distance[r][c]+1)
        return ans

from collections import Counter
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def inside(r,c):
            return 0<=r<R and 0<=c<C
        def traverse(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            max_moves=0
            for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if inside(nr,nc) and matrix[nr][nc]>matrix[r][c]:
                    max_moves=max(max_moves,traverse(nr,nc))
            memo[(r,c)]=max_moves+1
            return memo[(r,c)]
                    
                    
        memo=Counter()
        R=len(matrix)
        C=len(matrix[0])
        ans=1
        for i in range(R):
            for j in range(C):
                ans=max(ans,traverse(i,j))
        return  ans
'''

        
        



















        
        
        