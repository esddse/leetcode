# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        queue = [(root, 1)]
        while queue:
            new_queue = []
            for node, depth in queue:
                if not node.left and not node.right:
                    return depth
                if node.left:
                    new_queue.append((node.left, depth+1))
                if node.right:
                    new_queue.append((node.right, depth+1))
            queue = new_queue
