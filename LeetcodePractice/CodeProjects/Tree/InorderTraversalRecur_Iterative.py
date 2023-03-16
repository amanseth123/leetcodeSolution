# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        # iterative approach
        def inorderIterative(root):
            stack=[]
            curr=root
            while curr or stack:
                while curr: # go as much left as possible as we do in recursive way
                    stack.append(curr)
                    curr=curr.left
                curr=stack.pop() #after the curr hits a None value pop it and iterate for right subtree
                res.append(curr.val)
                curr=curr.right# left subtree done, iterate for right subtree
            return res
        #recursive approach
        def inorderRecur(root):
            if not root:
                return 
            inorderRecur(root.left)
            res.append(root.val)
            inorderRecur(root.right)
        #inorderRecur(root)
        inorderIterative(root)
        return res
        
        
        
        
        
        