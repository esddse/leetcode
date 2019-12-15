# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        l = 0
        p = head
        while p:
            l += 1
            p = p.next
        k = k % l

        p_fast, p_slow = head, head
        for _ in range(k):
            p_fast = p_fast.next if p_fast.next else head
        while p_fast.next:
            p_fast = p_fast.next 
            p_slow = p_slow.next
        p = p_slow
        if not p.next:
            return head
        else:
            tail = p
            while tail.next:
                tail = tail.next
            tail.next = head
            head = p.next 
            p.next = None
            return head