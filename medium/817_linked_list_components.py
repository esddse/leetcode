# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        G = set(G)
        cnt = 0
        flag = False
        while head:
            if head.val in G:
                flag = True
            else:
                if flag:
                    cnt += 1
                flag = False
            head = head.next
        if flag:
            cnt += 1
        return cnt
