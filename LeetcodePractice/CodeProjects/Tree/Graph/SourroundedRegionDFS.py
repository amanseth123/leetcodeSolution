class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #change all border "O" to "T"
        # mark every other "O" as "X" as they'll be surrounded anyhow 
        # mark all "T" back to "O"
        
        ROWS,COLS = len(board),len(board[0])
        def captureDFS(r,c):
            if r<0 or c<0 or r==ROWS or c==COLS or board[r][c]!="O":
                return 
            board[r][c]="T"
            captureDFS(r+1,c)
            captureDFS(r-1,c)
            captureDFS(r,c+1)
            captureDFS(r,c-1)
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j]=="O" and (i in [0,ROWS-1] or j in [0,COLS-1]):
                    captureDFS(i,j)
                
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j]=="O" :
                    board[i][j]="X"
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j]=="T":
                    board[i][j]="O"
        
        
        
        
        
        
        
        