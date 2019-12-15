# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        stack = []
        def dfs(node, stack):
            if not node:
                return True
            left_valid = dfs(node.left, stack)
            if not left_valid:
                return False
            if stack:
                if node.val <= stack[-1]:
                    return False 
            stack.append(node.val)
            right_valid = dfs(node.right, stack)
            if not right_valid:
                return False 
            return True 
        
        return dfs(root, stack)
            
            
            
            