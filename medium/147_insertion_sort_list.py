# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        
        empty = ListNode(0)
        empty.next = head
        head, tail = empty, empty
        
        while tail.next:
            if head == tail:
                tail = tail.next
                continue
            node = tail.next
            p = head
            while p != tail and p.next.val <= node.val:
                p = p.next
            if p == head:
                tail.next = node.next
                node.next = head.next
                head.next = node
            elif p == tail:
                tail = tail.next
            else:
                tail.next = node.next 
                node.next = p.next
                p.next = node
        return head.next


