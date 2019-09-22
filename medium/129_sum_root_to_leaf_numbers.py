# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        def dfs(node, current):
            if not node.left and not node.right:
                self.res += int(current+str(node.val))
            else:
                if node.left:
                    dfs(node.left, current+str(node.val))
                if node.right:
                    dfs(node.right, current+str(node.val))
        dfs(root, "")
        return self.res