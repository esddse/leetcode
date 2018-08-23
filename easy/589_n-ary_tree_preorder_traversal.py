"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        if not root:
            return []

        self.output = []

        def pre(root):
            self.output.append(root.val)
            for child in root.children:
                pre(child)
        pre(root)
        return self.output