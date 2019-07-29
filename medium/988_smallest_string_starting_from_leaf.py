# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import copy
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        
        def dfs(node, cur_str, min_str):
            # leaf
            if not node.left and not node.right:
                cur_str = [node.val] + cur_str
                if not min_str:
                    min_str = cur_str
                else:
                    min_str = list(min(tuple(min_str), tuple(cur_str)))
            else:
                if node.left:
                    min_str = dfs(node.left, [node.val] + cur_str, min_str)
                if node.right:
                    min_str = dfs(node.right, [node.val] + cur_str, min_str)

            return min_str

        cur_str, min_str = [], []
        min_str = dfs(root, cur_str, min_str)
        return "".join([chr(num+97) for num in min_str])