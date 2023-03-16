# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right




class Solution:
    def goodNodes3(self, root: TreeNode) -> int:
        def dfs(node,maxVal):
            if not node:
                return 0
            res = 1 if node.val>=maxVal else 0
            maxVal = max(maxVal,node.val)
            res+=dfs(node.left,maxVal)
            res+=dfs(node.right,maxVal)
            return res
        return dfs(root,root.val)
    
    #better dfs
    def __init__(self):
        self.count = 0
    def goodNodes2(self, root: TreeNode) -> int:
        
        self.helper(root,-100000)
        return self.count;
    
    def helper(self, root, max_number):
        if not root :  return;
        if root.val >= max_number:
            self.count+=1;
            max_number = root.val
        self.helper(root.right,max_number);
        self.helper(root.left,max_number)
    
    #BFS
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, root.val)]
        goodNodes = 0
        while stack:
            node, currMax = stack.pop()
            if node:
                if node.val >= currMax:
                    goodNodes += 1
                newMax = max(node.val, currMax)
                stack += (node.left, newMax), (node.right, newMax)
        return goodNodes
        
        
        
        
        
        