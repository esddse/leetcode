# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


import random
class Solution:

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """

        self.head = head
        
        self.length = 0
        p = head
        while p:
            self.length += 1
            p = p.next

        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """

        pos = random.randint(0, self.length-1)
        p = self.head
        while pos:
            p = p.next
            pos -= 1
        return p.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()