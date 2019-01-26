# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_pathlen = 0

        def dfs(node):
            if not node:
                return 0, None
            left_pathlen, left_val = dfs(node.left)
            right_pathlen, right_val = dfs(node.right)

            val = node.val
            if val == left_val and val == right_val:
                self.max_pathlen = max(self.max_pathlen, left_pathlen + right_pathlen + 2)
                pathlen = max(left_pathlen, right_pathlen) + 1
            elif val == left_val:
                self.max_pathlen = max(self.max_pathlen, left_pathlen + 1)
                pathlen = left_pathlen + 1
            elif val == right_val:
                self.max_pathlen = max(self.max_pathlen, right_pathlen + 1)
                pathlen = right_pathlen + 1
            else:
                pathlen = 0
            return pathlen, node.val

        dfs(root)
        return self.max_pathlen