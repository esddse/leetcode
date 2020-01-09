# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        lst = []
        p = head 
        while p:
            lst.append(p.val)
            p = p.next 
        
        num, base = 0, 1
        for b in lst[::-1]:
            num += (base * b)
            base *= 2
        return num