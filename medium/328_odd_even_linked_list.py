# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        odd_head  = head
        even_head = head.next

        p_odd  = odd_head
        p_even = even_head
        while True:
            if not p_even.next:
                p_odd.next = even_head
                break
            p_odd.next = p_even.next
            p_odd = p_odd.next
            if not p_odd.next:
                p_even.next = None
                p_odd.next = even_head
                break
            p_even.next = p_odd.next
            p_even = p_even.next 
        return odd_head

