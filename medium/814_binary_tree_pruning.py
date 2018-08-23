# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def prune(tree):
            if tree is None:
                return True

            # leaf
            if tree.left is None and tree.right is None:
                if tree.val is None:
                    return True
                elif tree.val == 0:
                    return True
                else:
                    return False

            # not leaf
            prune_left  = prune(tree.left)
            prune_right = prune(tree.right)

            if prune_left:
                tree.left = None
            if prune_right:
                tree.right = None

            if tree.val == 0 and prune_left and prune_right:
                return True
            else:
                return False

        prune(root)
        return root