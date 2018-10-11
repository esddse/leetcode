# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.min_val = float("inf")
        self.sec_val = float("inf")

        def dfs(node):
            if not node:
                return 
            val = node.val
            if val < self.min_val:
                self.sec_val = self.min_val
                self.min_val = val
            elif val > self.min_val and val < self.sec_val:
                self.sec_val = val
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        dfs(root)
        if self.min_val == self.sec_val or self.sec_val == float("inf"):
            return -1
        return self.sec_val
