# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        def merge(head1, head2):
            if head1.val <= head2.val:
                head = head1 
                p1, p2 = head1, head2 
            else:
                head = head2 
                p1, p2 = head2, head1

            while p1.next and p2:
                if p2.val >= p1.next.val:
                    p1 = p1.next
                else:
                    tmp = p2.next 
                    p2.next = p1.next 
                    p1.next = p2
                    p2 = tmp
            if not p1.next:
                p1.next = p2 
            
            return head

        fast, slow, prev = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next 
        prev.next = None
        head1, head2 = self.sortList(head), self.sortList(slow)
        return merge(head1, head2)