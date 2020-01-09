# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode(0)
        curr = head
        pq = PriorityQueue()
        for p in lists:
            if p:
                pq.put((p.val, id(p), p))
        while not pq.empty():
            _, __, p = pq.get()
            curr.next = p
            curr = curr.next
            while not pq.empty() and not p.next:
                _, __, p = pq.get()
                curr.next = p
                curr = curr.next
            if p.next:
                pq.put((p.next.val, id(p), p.next))
        return head.next
            
            
        