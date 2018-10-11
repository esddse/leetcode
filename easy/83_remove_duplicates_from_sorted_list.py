# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        prev = head
        curr = head.next

        while curr:
            if prev.val == curr.val:
                prev.next = curr.next
                curr = prev.next
            else:
                prev = curr
                curr = curr.next
        return head