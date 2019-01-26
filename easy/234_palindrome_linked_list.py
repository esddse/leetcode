# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        node = None
        while slow:
            nxt = slow.next
            slow.next = node 
            node = slow 
            slow = nxt

        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True