# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        
        if not root:
            return None

        def dfs(node, s):

            sums = set()
            if not node.left and not node.right:
                sums.update([s+node.val])
            if node.left:
                sums_l, valid_l = dfs(node.left, s+node.val)
                sums.update(sums_l)
                if not valid_l:
                    node.left = None
            if node.right:
                sums_r, valid_r = dfs(node.right, s+node.val)
                sums.update(sums_r)
                if not valid_r:
                    node.right = None

            valid = True
            if all([num < limit for num in sums]):
                valid = False

            return sums, valid

        sums, valid = dfs(root, 0)
        if valid:
            return root
        else:
            return None
