class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS,COLS = len(matrix),len(matrix[0])
        cache={}
        def helper(r,c):
            if r>=ROWS or c>=COLS:
                return 0
            if (r,c) not in cache:
                down = helper(r+1,c)
                right = helper(r,c+1)
                diag = helper(r+1,c+1)
                cache[(r,c)]=0
                if matrix[r][c]=="1":
                    cache[(r,c)]=1+min(down,right,diag)
            return cache[(r,c)]
        helper(0,0)
        return max(cache.values())**2
    def maximalSquare2(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        nrows = len(matrix)
        ncols = len(matrix[0])
        max_square_len = 0
        dp = [[0] * (ncols + 1) for i in range(nrows + 1)]
        
        for i in range(1, nrows + 1):
            for j in range(1, ncols + 1):
                if (matrix[i - 1][j - 1] == '1'):
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                    max_square_len = max(max_square_len, dp[i][j])
                    
        return max_square_len ** 2
    def maximalSquare1(self, matrix: List[List[str]]) -> int:
        ROWS=len(matrix)
        COLS = len(matrix[0])
        dp=[[0 for _ in range(COLS+1)] for _ in range(ROWS+1)]
        maxLen = 0
        for i in range(1,ROWS+1):
            for j in range(1,COLS+1):
                if matrix[i-1][j-1]=='1':
                    dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1 # min because if there's a 0 in any 4 direction then we don't need to consider that
                    maxLen = max(maxLen,dp[i][j])
        return maxLen**2
        
        
        
        