"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

        if not root:
            return []

        levels = []

        q = [root]
        while q:
            new_q = []
            level = []
            for node in q:
                level.append(node.val)
                for child in node.children:
                    new_q.append(child)
            levels.append(level)
            q = new_q
        return levels