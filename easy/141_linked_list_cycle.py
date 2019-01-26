# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        pl, pf = head, head.next

        while pf != pl:
            pl = pl.next
            if not pf.next or not pf.next.next:
                return False
            pf = pf.next.next

        return True