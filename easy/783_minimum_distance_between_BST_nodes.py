# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.min_dist = float('inf')
        self.pre = None

        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            if self.pre is None:
                self.pre = node.val
            else:
                if node.val - self.pre < self.min_dist:
                    self.min_dist = node.val - self.pre
                self.pre = node.val
            dfs(node.right)

        dfs(root)

        return self.min_dist