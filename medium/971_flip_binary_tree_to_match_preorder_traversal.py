# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        
        res = []
        self.idx = 0

        def dfs(node):
            if not node:
                return True
            if node.val != voyage[self.idx]:
                return False
            self.idx += 1

            left, right = node.left, node.right
            if left and left.val != voyage[self.idx]:
                left, right = right, left
                res.append(node.val)

            return dfs(left) and dfs(right)

        return res if dfs(root) else [-1]

