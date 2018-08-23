"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0

        self.maxdepth = 0

        def find(root, depth):
            if depth > self.maxdepth:
                self.maxdepth = depth
            if root.children:
                for child in root.children:
                    find(child, depth+1)
        find(root, 1)
        return self.maxdepth