"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = [root]
        while queue:
            new_queue = []
            for i in range(len(queue)-1):
                queue[i].next = queue[i+1]
                if queue[i].left:
                    new_queue += [queue[i].left, queue[i].right]
            if queue[-1].left:
                new_queue += [queue[-1].left, queue[-1].right]
            queue = new_queue
        return root