# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def __init__(self):
        self.hash={}
    def rob2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        elif root in self.hash:
            return self.hash[root]
        taken = root.val
        if root.left:
            taken+=self.rob(root.left.left)
            taken+=self.rob(root.left.right)
        if root.right:
            taken+=self.rob(root.right.left)
            taken+=self.rob(root.right.right)
        
        notTaken = self.rob(root.left)+self.rob(root.right)
        self.hash[root]=max(taken,notTaken)
        return self.hash[root]
    
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return [0,0] #[withRoot,withoutRoot]
            left = dfs(root.left)
            right = dfs(root.right)
            withRoot = root.val+left[1]+right[1]
            withoutRoot = max(left)+max(right)
            return [withRoot,withoutRoot]
        return max(dfs(root))
        
        
    
        
        
        