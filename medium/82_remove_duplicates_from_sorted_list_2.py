# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        h = ListNode("#")
        h.next = head
        p1, p2, p3 = h, h.next, h.next.next
        while True:
            if p2.val == p3.val:
                val = p3.val
                while p3 and p3.val == val:
                    p3 = p3.next
                p1.next = p3
            else:
                p1 = p2
            if not p1.next or not p1.next.next:
                break
            else:
                p2, p3 = p1.next, p1.next.next 
        return h.next  


