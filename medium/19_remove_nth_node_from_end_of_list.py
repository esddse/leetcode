# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        p1, p2 = head, head
        for _ in range(n):
            p1 = p1.next
        if not p1:
            return head.next
        while p1.next:
            p1 = p1.next 
            p2 = p2.next 
        p2.next = p2.next.next 
        return head