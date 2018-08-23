# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None

        def insert(root, val):
            if val < root.val:
                if root.left:
                    insert(root.left, val)
                else:
                    root.left = TreeNode(val)
            else:
                if root.right:
                    insert(root.right, val)
                else:
                    root.right = TreeNode(val)

        insert(root, val)
        return root