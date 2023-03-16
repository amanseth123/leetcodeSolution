class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(i,prev):
            if i==len(s):
                return True
            for j in range(i,len(s)):
                subVal = int(s[i:j+1])
                if subVal+1==prev and dfs(j+1,subVal):
                    return True
            return False
        for i in range(len(s)-1):
            val = int(s[:i+1])
            if dfs(i+1,val): # splitting the string and comparing prev value with new value
                return True
        return False
        
        
        
        
        