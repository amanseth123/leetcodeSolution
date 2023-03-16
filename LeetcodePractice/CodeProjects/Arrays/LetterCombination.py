class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def helper(i,s): #it works as a dfs so based on the output of the sample input
            if i>=len(digits):
                self.ans.append(s)
                return 
            for ch in di[digits[i]]:
                helper(i+1,s+ch)
        di={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}    
        self.ans=[]
        if digits:
            helper(0,"")
        return self.ans
        