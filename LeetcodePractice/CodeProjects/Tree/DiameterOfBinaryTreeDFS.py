class Solution:
    def height(self,root):
        if not root:
            return 0
        return 1+max(self.height(root.left),self.height(root.right))
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        lheight=self.height(root.left)
        print(root.val,lheight)
        rheight=self.height(root.right)
        print("rjheight",root.val,rheight)
        ldiam=self.diameterOfBinaryTree(root.left)
        print("ld",ldiam,root.val)
        rdiam=self.diameterOfBinaryTree(root.right)
        print("rd",rdiam,root.val)
        return max(lheight+rheight,ldiam,rdiam)


        # BFS SOLUTION
class Solution:
    def lt(self,r):
        q=[(r,1)]
        m=0
        while q:
            r,l=q.pop()
            m=max(m,l)
            if r.left:
                q.append((r.left,l+1))
            if r.right:
                q.append((r.right,l+1))
        return  m
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            ans1,ans2=0,0
            if root.left:
                ans1=self.lt(root.left)
            if root.right:
                ans2=self.lt(root.right)
        return max(ans1+ans2,self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))