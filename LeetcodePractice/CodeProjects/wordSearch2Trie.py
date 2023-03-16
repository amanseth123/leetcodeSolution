class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie={}
        words=set(words)
        for word in words:
            curr=trie
            for ch in word:
                if ch not in curr:
                    curr[ch]={}
                curr=curr[ch]
            curr['*']={}
        
        def dfs(r,c,path,currDict):
            if '*' in currDict:
                self.output.add(path)
            visited.add((r,c))
            for row,col in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0<=row<len(board) and 0<=col<len(board[0]) and (row,col) not in visited and board[row][col] in currDict:
                    dfs(row,col,path+board[row][col],currDict[board[row][col]])
            visited.remove((r,c))
        visited=set()
        self.output=set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie:
                    curr=trie
                    dfs(i,j,board[i][j],curr[board[i][j]])
        return self.output
        