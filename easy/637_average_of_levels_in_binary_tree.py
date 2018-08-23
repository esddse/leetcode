# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        queue = deque([(root, 0)])
        avgs = []
        avgdepth = 0
        outputs = []
        while queue:
            node, depth = queue.popleft()
            if depth != avgdepth:
                outputs.append(sum(avgs) / len(avgs))
                avgs = []
            avgdepth = depth
            avgs.append(node.val)
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        outputs.append(sum(avgs) / len(avgs))

        return outputs    
        
