# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        def collect(node, depth):
            if node:
                if depth == len(view):
                    print(view,depth,node.val) # the len(view) will always contain the rightmost and it'll increment only by one so its good to compare with depth
                    view.append(node.val)
                collect(node.right, depth+1)
                collect(node.left, depth+1)
        view = []
        collect(root, 0)
        return view
    def rightSideViewBFS(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q=[(root,0)]
        ans=defaultdict(list)
        while q:
            node,level = q.pop(0)
            ans[level].append(node.val)
            if node and node.left:
                q.append((node.left,level+1))
            if node and node.right:
                q.append((node.right,level+1))        
        final=[]
        for k,v in ans.items():
            final.append(v[-1])
        return final
        
        
        