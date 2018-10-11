# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        if not s and not t:
            return True
        if not s or not t:
            return False
        
        def check(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2 or node1.val != node2.val:
                return False
            return check(node1.left, node2.left) and check(node1.right, node2.right)

        def find(t, s):
            if not t:
                return False
            if t.val == s.val and check(t, s):
                return True
            return find(t.left, s) or find(t.right, s)

        return find(s, t)




