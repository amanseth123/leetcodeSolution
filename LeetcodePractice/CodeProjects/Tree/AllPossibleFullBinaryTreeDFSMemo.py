# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp={}
        def helper(n):
            if n==0:
                return []
            if n==1:
                return [TreeNode()]
            if n in dp:
                return dp[n]
            res=[]
            for l in range(n):
                r=n-l-1
                leftTree = helper(l)
                rightTree = helper(r)
                for t1 in leftTree:
                    for t2 in rightTree:
                        res.append(TreeNode(0,t1,t2))
            dp[n]=res
            return res
        return helper(n)
        
    
        
        
        
        
        
        