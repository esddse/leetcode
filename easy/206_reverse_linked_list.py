# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        pre = None
        while head:
            cur = head.next
            head.next = pre
            pre = head
            head = cur
        return pre

