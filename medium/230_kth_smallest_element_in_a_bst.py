# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        self.cnt = 0

        def dfs(node):
            if not node:
                return None
            numl = dfs(node.left)
            if numl is not None:
                return numl
            self.cnt += 1
            if self.cnt == k:
                return node.val
            numr = dfs(node.right)
            if numr is not None:
                return numr
            return None

        return dfs(root)


