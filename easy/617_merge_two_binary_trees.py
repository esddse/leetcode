class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        def merge(t1, t2):
            if t1 and t2:
                new_node = TreeNode(t1.val + t2.val)
            elif t1:
                new_node = TreeNode(t1.val)
            elif t2:
                new_node = TreeNode(t2.val)
            else:
                return None

            new_node.left  = merge(t1.left if t1 else None, t2.left if t2 else None)
            new_node.right = merge(t1.right if t1 else None, t2.right if t2 else None)
            return new_node

        return merge(t1, t2)