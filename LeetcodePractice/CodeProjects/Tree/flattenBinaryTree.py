# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    #BFS Solution
    # Pick every node and assign its right to the top of the stack which will be the left value because
    # we are inserting right first in the stack in line 18, and assign left as null after proper insertion
    def helper(self,root):
        if root is None:
            return 
        stack=[root]
        while stack:
            temp=stack.pop()
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
            if stack:
                print([i.val for i in stack],temp.val)
                temp.right=stack[-1]
            temp.left=None
        return root
    def flatten(self, root: TreeNode) -> None:
        return self.helper(root)


        # DFS Solution
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left: # that's the only case because if root.left is not present then we don't need to do anything
            curr=root.left #store root.left pointer
            while curr.right: # root.left can also have more right child so traverse through the tail of its rightmost child
                curr=curr.right
            curr.right = root.right# the right of the rightmost child of root.left must point to root.right 
            root.right=root.left# insert the left subtree inbetween the root.right
            root.left=None# make root.left None as we don't need it anymore
        return root # although not required because we're changing the root in place
        
        
        
        
        
        
        
        