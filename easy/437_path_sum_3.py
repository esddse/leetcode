# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        
        self.cnt = 0

        def dfs(node, is_start, need):
            if not node:
                return 
            val = node.val
            if is_start:
                if val == need:
                    self.cnt += 1
                dfs(node.left, is_start, need - val)
                dfs(node.right, is_start, need - val)
            else:
                if val == need:
                    self.cnt += 1
                dfs(node.left, not is_start, need - val)
                dfs(node.right, not is_start, need - val)
                dfs(node.left, is_start, need)
                dfs(node.right, is_start, need)

        dfs(root, False, sum)
        return self.cnt