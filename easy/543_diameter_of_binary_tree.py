# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def diameter(node):
            if not node or (not node.left and not node.right):
                return 0, 0
            left_len, left_dia = diameter(node.left)
            right_len, right_dia = diameter(node.right)
            if not node.right:
                return left_len + 1, max(left_dia, left_len + 1)
            if not node.left:
                return right_len + 1, max(right_dia, right_len + 1)
            else:
                return max(left_len, right_len) + 1, max(left_dia, right_dia, left_len + right_len + 2)
        return diameter(root)[1]
