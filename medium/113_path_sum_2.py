# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        if not root:
            return []

        rets = []
        def dfs(node, s, lst):
            s += node.val
            if not node.left and not node.right:
                if s == sum:
                    rets.append(lst+[node.val])
            if node.left:
                dfs(node.left, s, lst+[node.val])
            if node.right:
                dfs(node.right, s, lst+[node.val])
        dfs(root, 0, [])
        return rets