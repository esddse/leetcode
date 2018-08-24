# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        def search(node, depth):
            # leaf
            if not node.left and not node.right:
                return node, depth
            # single child
            if not node.right:
                return search(node.left, depth+1)
            if not node.left:
                return search(node.right, depth+1)

            # 
            node_left,  depth_left  = search(node.left, depth+1)
            node_right, depth_right = search(node.right, depth+1)

            if depth_left > depth_right:
                return node_left, depth_left
            elif depth_left < depth_right:
                return node_right, depth_right
            else:
                return node, depth_left

        node, depth = search(root, 0)
        return node