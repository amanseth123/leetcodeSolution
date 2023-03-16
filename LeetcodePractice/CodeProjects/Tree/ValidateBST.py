'''

class Solution:
    def helper(self,curr,ans):
        if curr is None:
            return None
        self.helper(curr.left,ans)
        ans.append(curr.val)
        self.helper(curr.right,ans)
    
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        ans=[]
        self.helper(root,ans)
        if all(ans[i]<ans[i+1] for i in range(len(ans)-1)):
            return True
        return False
'''
class Solution:
    def helper(self,curr,lb,ub):
        if not curr:
            return True
        return (lb<curr.val<ub) and self.helper(curr.left,lb,curr.val) and self.helper(curr.right,curr.val,ub)
    def isValidBST(self, root: TreeNode) -> bool:
        ub=float("inf")
        lb=float("-inf")
        return self.helper(root,lb,ub)