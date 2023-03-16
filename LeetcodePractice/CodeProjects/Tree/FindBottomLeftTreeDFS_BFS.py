# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # first we traverse the left tree, and we add it into view but when we start traversing right tree we only need nodes which are at level> len(view)(previously visit nodes represent depth) and then we add it into our views
        def collect(node, depth):
            if node:
                if depth == len(view):
                    print(depth,view,node.val)
                    view.append(node.val)# if we encounter level>len(visit) then add the noode
                collect(node.left, depth+1)
                collect(node.right, depth+1)
        view = []
        collect(root, 0)
        print(view)
        return view[-1]
        
    def findBottomLeftValue2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        q=[(root,0)]
        ans=defaultdict(list)
        while q:
            node,level = q.pop(0)
            ans[level].append(node)
            if node and node.left:
                q.append((node.left,level+1))
            if node and node.right:
                q.append((node.right,level+1))
        return ans[len(ans)-1][0].val
        
        
        