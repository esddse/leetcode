# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None

        root = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1])
        in_left, in_right = inorder[:idx], inorder[idx+1:] 
        post_left, post_right = postorder[:len(in_left)], postorder[len(in_left):-1]

        root.left  = self.buildTree(in_left,  post_left)
        root.right = self.buildTree(in_right, post_right)

        return root 