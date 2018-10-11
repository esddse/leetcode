# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        vp, vq = p.val, q.val
        vp, vq = sorted([vp, vq])
        if vp == vq:
            return p

        def find(node, p, q):
            if not node:
                return None
            val = node.val
            if val < p:
                return find(node.right, p, q)
            elif val > q:
                return find(node.left, p, q)
            else:
                return node
        return find(root, vp, vq)

