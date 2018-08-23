# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root is None:
            return []

        queue = [root]
        largests = []

        while queue:

            next_queue, nums = [], []
            for node in queue:
                nums.append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            largests.append(max(nums))

            if not next_queue:
                return largests

            queue = next_queue

