# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        small = ListNode(0)
        big   = ListNode(0)
        node, s, b = head, small, big 
        while node:
            n = node.next
            node.next = None
            if node.val >= x:
                b.next = node
                b = b.next
            else:
                s.next = node
                s = s.next
            node = n
        s.next = big.next
        return small.next

