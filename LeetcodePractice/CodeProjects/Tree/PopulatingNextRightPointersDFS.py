"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def populateLowerLevel(start):
            iter=start
            while iter:
                iter.left.next=iter.right# connect left.nect with root.right
                if iter.next is not None: # if iter has next pointer then 
                    iter.right.next=iter.next.left #connect its right with next's left child
                iter=iter.next # move to the next column
        node=root
        while node and node.left :
            populateLowerLevel(node)# in each level we connect every node before n=moving to next level
            node=node.left
        return root