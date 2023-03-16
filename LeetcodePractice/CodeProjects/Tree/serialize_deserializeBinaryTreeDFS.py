# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def helper(self,root,path):
        if not root:
            path.append("None")
            return 
        path.append(str(root.val))
        self.helper(root.left,path)
        self.helper(root.right,path)
    def helper2(self,data):
        if data[0]=='None':
            data.pop(0)
            return 
        else:
            root=TreeNode(data[0])
            #print(root.val)
            data.pop(0) #again preorder and after we consume data[0] as root we need to pop it so as we don't consider it again
            root.left=self.helper2(data)
            root.right=self.helper2(data)
        
        return root
    def serialize(self, root):
        if root is None:
            return []
        #self.path=[]
        path=[]
        self.helper(root,path)
        path=','.join(path)
        print(path)
        return path
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return 
        data=data.split(',')
        #print(data)
        return self.helper2(data)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))