# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        max_width = 0
        queue = [(root, 0)]
        while queue:
            new_queue = []
            max_x, min_x = -1, float("inf")
            for node, x in queue:
                max_x = max(max_x, x)
                min_x = min(min_x, x)
                if node.left:
                    new_queue.append((node.left, x*2))
                if node.right:
                    new_queue.append((node.right, x*2+1))
            queue = new_queue
            width = max_x - min_x + 1
            max_width = max(max_width, width)
        return max_width