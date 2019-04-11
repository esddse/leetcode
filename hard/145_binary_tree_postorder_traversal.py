# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        self.res = []
        
        def post(node):
            if not node:
                return 
            post(node.left)
            post(node.right)
            self.res.append(node.val)

        post(root)
        return self.res