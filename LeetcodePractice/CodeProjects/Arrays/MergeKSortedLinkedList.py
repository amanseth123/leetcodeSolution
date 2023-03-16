# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
        
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge(l1,l2):
            root = ListNode(-1)
            if l1 is None:
                return l2
            if l2 is None:
                return l1
            if l1.val<l2.val:
                root = l1
                root.next = merge(l1.next,l2)
            else:
                root=l2
                root.next = merge(l1,l2.next)
            return root
        if len(lists)==0:
            return None
        if len(lists)==1:
            return lists[0]
        k = len(lists)
        mid = k//2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])    
        return merge(left,right)
    
        