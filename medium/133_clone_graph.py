"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        nodecopy = Node(node.val, [])
        d = {node: nodecopy}
        queue = [node]
        while queue:
            new_queue = []
            for node in queue:
                for neighbor in node.neighbors:
                    if neighbor not in d:
                        neighborcopy = Node(neighbor.val, [])
                        d[neighbor] = neighborcopy 
                        new_queue.append(neighbor)
                    d[node].neighbors.append(d[neighbor])
            queue = new_queue
        return nodecopy
                        