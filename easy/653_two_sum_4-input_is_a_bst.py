
from collections import deque

class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        
        if not root:
            return False

        queue = [root]
        nums = set()
        for node in queue:
            val = node.val
            if k - val in nums:
                return True
            nums.add(val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return False