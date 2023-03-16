'''
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def inorder(root,ans):
            if not root:
                return 
            inorder(root.left,ans)
            ans.append(root.val)
            inorder(root.right,ans)
        if not root:
            return None
        ans=[]
        inorder(root,ans)
        di={}
        for i in range(len(ans)):
            di[ans[i]]=sum(ans[i:])
        q=[root]
        while q:
            r=q.pop()
            r.val=di[r.val]
            if r.left:
                q.append(r.left)
            if r.right:
                q.append(r.right)
        return root

'''

class Solution:
    def convertBST2(self, root: TreeNode) -> TreeNode:
        #using reverse inorder traversal
        self.currSum=0
        def dfs(node):
            if not node:
                return 
            dfs(node.right)
            temp = node.val
            print(node.val,self.currSum)
            node.val+=self.currSum
            self.currSum+=temp
            dfs(node.left)
        dfs(root)
        return root
        # time complexity: O(n) space complexity: O(height)
        
    def convertBST(self, root: TreeNode) -> TreeNode:
        # using reverse postorder traversal
        def addsum(node,top):
            if not node:
                return 0
            x0, rhs = node.val, addsum(node.right,top)
            lhs = addsum(node.left, top + x0 + rhs)
            node.val += top + rhs
            print(x0,rhs,lhs,node.val,top)
            return x0 + rhs + lhs
        addsum(root,0)
        return root