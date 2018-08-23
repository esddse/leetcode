# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        if not root1 or not root2:
            return False
        
        def get_leaf(root):
            seq = []

            stack = [root]
            while stack:
                node = stack.pop()
                if not node.left and not node.right:
                    seq.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

            return seq

        seq1 = get_leaf(root1)
        seq2 = get_leaf(root2)

        return seq1 == seq2
