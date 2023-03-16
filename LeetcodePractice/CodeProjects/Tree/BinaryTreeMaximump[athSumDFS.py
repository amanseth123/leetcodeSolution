# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if root is None:
                return 0
            l = max(0,helper(root.left))
            r = max(0,helper(root.right))
            self.res = max(l+r+root.val,self.res) # with split on root node
            return max(l,r)+root.val #without split on root node
        self.res=float('-inf')
        helper(root)
        return self.res
        
        
        