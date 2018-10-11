# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        res = []
        queue = [root]
        while queue:
            vals = []
            new_queue = []
            for node in queue:
                vals.append(node.val)
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            res.append(vals)
            queue = new_queue
        return res
