# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def robsub(root):
            if not root:
                return (0, 0)

            res_left  = robsub(root.left)
            res_right = robsub(root.right)

            val_select = root.val + res_left[1] + res_right[1]
            val_not_select = max(res_left) + max(res_right)

            return (val_select, val_not_select)

        return max(robsub(root))
