# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        def travel(node, s_parent):
            if not node:
                return 0
            origin_val = node.val
            s_right = travel(node.right, s_parent)
            node.val += s_parent + s_right
            s_left = travel(node.left, s_parent + origin_val + s_right)
            return s_right + origin_val + s_left

        travel(root, 0)
        return root