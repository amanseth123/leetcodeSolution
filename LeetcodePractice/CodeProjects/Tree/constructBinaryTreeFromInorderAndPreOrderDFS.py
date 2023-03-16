# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pos=0
        
    # easy to understand
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder)==1:
            return TreeNode(inorder[0])
        if not preorder:
            return None
        new_node = TreeNode(preorder[0]) 
        pivot = inorder.index(preorder[0]) 
        new_node.left = self.buildTree(preorder[1:pivot+1],inorder[:pivot])
        new_node.right  = self.buildTree(preorder[pivot+1:],inorder[pivot+1:])
        return new_node

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid]) #preorder[0] already taken
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        
        return root     
    
    #my solution
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[self.pos])
        mid = inorder.index(preorder[self.pos])
        self.pos+=1
        root.left = self.buildTree(preorder,inorder[:mid]) #preorder[0] already taken
        root.right = self.buildTree(preorder,inorder[mid+1:])
        return root
        
    def buildTree2(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(preorder,inorder,low,high):
            if low>high:
                return None
            root=TreeNode(preorder[self.pos])
            curr=root
            inor=inorder.index(preorder[self.pos])
            self.pos+=1
            root.left=helper(preorder,inorder,low,inor-1)
            root.right=helper(preorder,inorder,inor+1,high)
            return curr
        if len(preorder)==0 or len(inorder)==0:
            return 
        self.pos=0
        return helper(preorder,inorder,0,len(preorder)-1)
    
    
    
    
    
    
    