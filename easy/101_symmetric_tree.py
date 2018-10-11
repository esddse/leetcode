# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def check(node1, node2):
            if not node1 and not node2:
                return True
            if node1 and node2 and node1.val == node2.val:
                check_left = check(node1.left, node2.right)
                check_right = check(node1.right, node2.left)
                return check_left and check_right
            return False

        if not root:
            return True
        return check(root.left, root.right)

        