# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        fast, slow, step = head, head, 0
        while step == 0 or fast != slow:
            if not fast.next or not fast.next.next:
                return None 
            fast = fast.next.next
            slow = slow.next
            step += 1
        p, pos = head, 0
        while p != slow:
            p = p.next 
            slow = slow.next 
            pos += 1
        return p
        