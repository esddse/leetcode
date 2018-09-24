# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def tilt(node):
            if not node:
                return 0, 0, 0

            sum_left, tilt_left, tilt_sum_left = tilt(node.left)
            sum_right, tilt_right, tilt_sum_right = tilt(node.right)

            sum_this  = sum_left + sum_right + node.val
            tilt_this = abs(sum_left - sum_right)
            tilt_sum  = tilt_sum_left + tilt_sum_right + tilt_this
            return sum_this, tilt_this, tilt_sum

        _1, _2, tilt_sum = tilt(root)
        return tilt_sum


