# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr=root
        while curr:
            if p.val>curr.val and q.val>curr.val:# if both p and q lies in the right subtree
                curr=curr.right
            elif p.val<curr.val and q.val<curr.val:# if both p and q lies in the left subtree
                curr = curr.left
            else: # means one of p or q occurs on one side and the other occurs on otherside and the node where the split occurs will be the lca
                return curr  
        
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return 
        if root==p or root==q:
            return root
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        if left and right:
            return root
        if left is None and right is None:
            return None
        return left if left else right
        
        
        
        
        
        