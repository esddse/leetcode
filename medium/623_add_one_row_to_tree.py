class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        
        def add(node, v, d, cur, left):
            if cur == d:
                new_node = TreeNode(v)
                if left or cur == 1:
                    new_node.left = node
                else:
                    new_node.right = node
                return new_node
            else:
                if not node:
                    return None
                node.left = add(node.left, v, d, cur+1, left=True)
                node.right = add(node.right, v, d, cur+1, left=False)
                return node

        return add(root, v, d, 1, True)