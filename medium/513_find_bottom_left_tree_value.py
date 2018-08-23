# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def dfs(self, root, depth):
        if depth > self.max_depth:
            self.max_depth = depth
            self.num = root.val
        if root.left is not None:
            self.dfs(root.left, depth+1)
        if root.right is not None:
            self.dfs(root.right, depth+1)

    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.max_depth = -1
        self.num = 0

        self.dfs(root, 0)

        return self.num
