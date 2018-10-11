# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def balance(node, depth):
            if not node:
                return True, depth
            left_balence, left_depth = balance(node.left, depth+1)
            right_balance, right_depth = balance(node.right, depth+1)
            depth = max(left_depth, right_depth)
            if not left_balence or not right_balance:
                return False, depth
            if abs(left_depth-right_depth) > 1:
                return False, depth 
            return True, depth
        return balance(root, 0)[0]


