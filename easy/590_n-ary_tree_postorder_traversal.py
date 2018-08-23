"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []

        self.outputs = []
        def post(root):
            if root.children:
                for node in root.children:
                    post(node)
            self.outputs.append(root.val)
        post(root)
        return self.outputs