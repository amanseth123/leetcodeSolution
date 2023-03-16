# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            if self.prev is not None:
                if self.prev.val > root.val:
                    if self.ptr1==None:
                        self.ptr1=self.prev
                    self.ptr2=root
            self.prev=root
            inorder(root.right)
        q=[root]
        self.ptr1=None
        self.ptr2=None
        self.prev=TreeNode(float('-inf'))
        inorder(root)
        self.ptr1.val,self.ptr2.val=self.ptr2.val,self.ptr1.val
        
        