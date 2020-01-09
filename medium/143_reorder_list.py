# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None 
        fast, slow, prev = head, head, None
        while fast:
            fast = fast.next.next if fast.next else fast.next 
            prev = slow
            slow = slow.next 
        prev.next = None
        
        def reverse(head):
            if not head or not head.next:
                return head
            p, q = head, head.next
            head.next = None
            while q:
                tmp = q.next 
                q.next = p 
                p = q
                q = tmp
            return p 
        p, q = head, reverse(slow)
        
        while q:
            tmp = q.next
            q.next = p.next
            p.next = q
            q = tmp
            p = p.next.next
            
        return head
        
        