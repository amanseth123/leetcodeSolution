# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
        if r1 is None or r2 is None:
            return not r1 and not r2#If root1 or root2 is null, then they are equivalent if and only if they are both null.

        if r1.val!=r2.val:
            return False
        noFlips = self.flipEquiv(r1.left,r2.left) and self.flipEquiv(r1.right,r2.right)#check left subtree of r1 with left subtree of r2 and check right subtree of r1 and right subtree of r2
        flips = self.flipEquiv(r1.left,r2.right) and self.flipEquiv(r1.right,r2.left)#check if we require flips, by checking the left subtree of r1 with right subtree of r2 and right subtree of r1 with left subtree of r1
        return noFlips or flips # return if any of them is true
        
        
        
        
        
        
        
        
        