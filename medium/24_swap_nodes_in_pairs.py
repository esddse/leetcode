# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        

        p, last = head, None
        while p:
            if p.next:
                q = p.next
                # swap
                p.next = q.next 
                q.next = p  
                if not last:
                    head = q 
                else:
                    last.next = q
                last = p
            p = p.next

        return head