# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(root,s):
            
            if root.left==None and root.right==None:
                self.ans+=int(s)
                return
            if root and root.left:
                helper(root.left,s+str(root.left.val))
            if root and root.right:
                helper(root.right,s+str(root.right.val))
        self.ans=0
        helper(root,str(root.val))
        return self.ans
    
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root,temp):
            if root and root.left is None and root.right is None:
                temp+=str(root.val)
                self.total+=int(temp)
                return 
            if root and root.left:
                dfs(root.left,temp+str(root.val))
            if root and root.right:
                dfs(root.right,temp+str(root.val))
                
            
        self.total  =0
        dfs(root,"")
        return self.total
        
        
        
        
        