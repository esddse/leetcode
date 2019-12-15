# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        if not head or m >= n:
            return head
        
        # virtual head
        h = ListNode("#")
        h.next = head
        head = h
        
        # find prev
        prev, p, q = head, head, None
        for i in range(n+1):
            if i < m-1:
                p = p.next
            elif i == m-1:
                prev = p
                p = p.next
            elif i == m:
                inner_tail = p 
                q = p 
                p = p.next 
            elif i < n-1:
                tmp = p.next
                p.next = q
                q = p
                p = tmp
            else: 
                tmp = p.next
                p.next = q
                q = p
                p = tmp
                inner_head = q
            
        # post process
        inner_tail.next = p
        prev.next = inner_head
            
            
        return head.next