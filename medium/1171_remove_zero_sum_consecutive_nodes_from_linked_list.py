# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        

        new_head = ListNode(0)
        new_head.next = head 
        head = new_head

        to_check = True
        while to_check:
            to_check = False
            record = {0:head}
            s = 0

            curr = head.next
            while curr:
                s += curr.val
                if s in record:
                    record[s].next = curr.next
                    record = {0: record[s]}
                    s = 0
                    to_check = True
                else:
                    record[s] = curr
                curr = curr.next

        return head.next