# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val>high:
            return self.trimBST(root.left,low,high) # skip entire right subtree as the values are gonna be higher 
        if root.val<low:
            return self.trimBST(root.right,low,high) # skip the entire left subtree as the value are gonna be lower
        root.left = self.trimBST(root.left,low,high) # if the root is within the range then run same trim function on it left subtree
        root.right = self.trimBST(root.right,low,high) # if the root is within range then run same trim function on it right subtree
        return root # as this root will be assigned to either left of right of parent root in case we did a trim inside 2 if statements 