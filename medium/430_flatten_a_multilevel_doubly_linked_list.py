"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        stack = []
        last = Node(0, None, None, None)
        node = head
        while node:
            last.next = node
            node.prev = last
            last = last.next

            if node.child:
                stack.append(node.next)
                tmp = node
                node = node.child
                tmp.child = None
            else:
                if node.next:
                    node = node.next 
                else:
                    if stack:
                        node = stack.pop()
                        while stack and not node:
                            node = stack.pop() 
                    else:
                        node = node.next

        head.prev = None
        return head