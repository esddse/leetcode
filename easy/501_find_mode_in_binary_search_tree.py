# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []
        d = defaultdict(int)
        def dfs(node):
            if not node:
                return
            d[node.val] += 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        d = sorted(d.items(), key=lambda item: item[1], reverse=True)
        res, max_cnt = [d[0][0]], d[0][1]
        for val, cnt in d[1:]:
            if cnt != max_cnt:
                break
            res.append(val)
        return res


