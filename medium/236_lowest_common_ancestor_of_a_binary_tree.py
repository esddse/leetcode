# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.p_ancestors, self.q_ancestors = None, None
        def dfs(node, ancestors):
            if node == p:
                self.p_ancestors = [a for a in ancestors] + [node]
            if node == q:
                self.q_ancestors = [a for a in ancestors] + [node]
            if self.p_ancestors and self.q_ancestors:
                return True
            ancestors.append(node)
            if node.left:
                if dfs(node.left, ancestors):
                    return True
            if node.right:
                if dfs(node.right, ancestors):
                    return True
            ancestors.pop()
            return False

        ancestors = []
        res = dfs(root, ancestors)
        common = None 
        for i, j in zip(self.p_ancestors, self.q_ancestors):
            if i == j:
                common = i 
            else:
                break 
        return common

