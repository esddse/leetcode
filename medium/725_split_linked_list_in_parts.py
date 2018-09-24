# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        
        def lst_len(lst):
            length = 0
            while lst:
                lst = lst.next
                length += 1
            return length

        length = lst_len(root)
        base_len, num_addone = length // k, length % k

        lsts = []
        for _ in range(num_addone):
            length = base_len + 1
            head, p = root, root
            while length > 1:
                p = p.next
                length -= 1
            root = p.next
            p.next = None
            lsts.append(head)

        for _ in range(k - num_addone):
            if base_len == 0:
                lsts.append(None)
            else:
                length = base_len
                head, p = root, root
                while length > 1:
                    p = p.next
                    length -= 1
                root = p.next
                p.next = None
                lsts.append(head)
        return lsts