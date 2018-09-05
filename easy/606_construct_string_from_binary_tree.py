class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """

        def construct(node):
            if not node:
                return ""

            string = str(node.val)
            if not node.left and not node.right:
                return string
            string += "(" + construct(node.left) + ")"
            if node.right:
                string +=  "(" + construct(node.right) + ")"
            return string

        return construct(t)
