# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        self.lst = []

        def inorder(root):
            if root.left:
                inorder(root.left)
            self.lst.append(root.val)
            if root.right:
                inorder(root.right)
        inorder(root)
        return self.lst