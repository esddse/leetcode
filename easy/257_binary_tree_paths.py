# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        res = []

        def dfs(node, lst):
            # leaf
            if not node.left and not node.right:
                res.append("->".join(lst+[str(node.val)]))
                return 
            if node.left:
                dfs(node.left, lst+[str(node.val)])
            if node.right:
                dfs(node.right, lst+[str(node.val)])
        dfs(root, [])
        return res
