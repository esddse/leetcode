# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:

        def height(node):
            p = node
            h = -1
            while p:
                p = p.left
                h += 1
            return h

        h = height(root)
        if h < 0:
            return 0
        if height(root.right) == h-1:
            return (1 << h) + self.countNodes(root.right) 
        else:
            return (1 << h-1) + self.countNodes(root.left)

