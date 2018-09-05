# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.s = 0
        def dfs(node, left):
            if node.left:
                dfs(node.left, True)
            if node.right:
                dfs(node.right, False)
            if not node.left and not node.right and left:
                self.s += node.val
        dfs(root, False)
        return self.s