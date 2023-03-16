# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
from collections import defaultdict
class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        graph=defaultdict(list)
        q=[(A)]
        visit=set()
        while q:
            node = q.pop(0)
            visit.add(node.val)
            if node.left:
                if node.left.val not in visit:
                    graph[node.val].append(node.left.val)
                    graph[node.left.val].append(node.val)
                q.append(node.left)
            if node.right:
                if node.right.val not in visit:
                    graph[node.val].append(node.right.val)
                    graph[node.right.val].append(node.val)
                q.append(node.right)
        q=[(B,0)]
        count=0
        visit=set()
        while q:
            node,time = q.pop(0)
            visit.add(node)
            for nodes in graph[node]:
                if nodes not in visit:
                    q.append((nodes,time+1))
        return time