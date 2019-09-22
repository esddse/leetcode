# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        
        def flt(node):
            if not node.left and not node.right:
                return node
            elif not node.left:
                return flt(node.right)
            elif not node.right:
                left = flt(node.left)
                node.right = node.left
                node.left = None 
                return left
            else:
                right = flt(node.right)
                left  = flt(node.left)
                left.right = node.right 
                node.right = node.left 
                node.left  = None
                return right
        flt(root)


            