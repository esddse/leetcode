"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        h = Node("#", head, None)
        hcopy = Node("#", None, None)
        node_dict = {h: hcopy}
        p, pcopy = h, hcopy 
        while p:
            if p.next:
                if p.next not in node_dict:
                    pcopynext = Node(p.next.val, None, None)
                    node_dict[p.next] = pcopynext 
                pcopy.next = node_dict[p.next]
            if p.random:
                if p.random not in node_dict:
                    pcopyrandom = Node(p.random.val, None, None)
                    node_dict[p.random] = pcopyrandom 
                pcopy.random = node_dict[p.random]
            p, pcopy = p.next, pcopy.next
        return hcopy.next
            
            
            
        