# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        p, q = l1, l2
        carry = 0
        while p and q:
            v1, v2 = p.val, q.val
            p.val = (v1+v2+carry)%10
            carry = (v1+v2+carry)//10
            if not p.next:
                if q.next:
                    p.next, q.next = q.next, p.next
                elif carry:
                    p.next = ListNode(carry)
                    carry = 0
            p = p.next 
            q = q.next
        while p:
            val = p.val
            p.val = (val+carry)%10
            carry = (val+carry)//10
            if not p.next and carry:
                p.next = ListNode(carry)
                carry = 0
            p = p.next
        return l1

