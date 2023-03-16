class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            return s[::-1]==s
        def dfs(i,path):
            if i>=len(s):
                self.ans.append(path)
                return 
            for j in range(i,len(s)):
                if isPalindrome(s[i:j+1]):
                    #path.append(s[i:j+1])
                    dfs(j+1,path+[s[i:j+1]])
                    #path.pop()
        self.ans=[]
        path=[]
        dfs(0,[])
        return self.ans
        
        # def isPalindrome(s):
        #     return s[::-1]==s
        # def dfs(s,res,path,index):
        #     if len(s)==0:
        #         res.append(path)
        #         return 
        #     for i in range(1,len(s)+1):#O(n)
        #         if isPalindrome(s[:i]): #O(n)
        #             dfs(s[i:],res,path+[s[:i]],i+1)# worst case O(2^n)
        #         else:
        #             continue
        # res=[]
        # path=[]
        # dfs(s,res,path,0)
        # print(len(res))
        # return res
    
    
    
    
    