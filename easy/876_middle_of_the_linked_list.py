# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        length = 0
        p = head
        while p is not None:
            p = p.next
            length += 1
        middle = length // 2

        p = head
        for i in range(middle):
            p = p.next
        return p
