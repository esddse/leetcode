# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        is_left = None
        prev = None
        node = root
        while node and node.val != key:
            if key < node.val:
                prev = node
                node = node.left 
                is_left = True
            else:
                prev = node
                node = node.right
                is_left = False

        if not node:
            return root


        if not node.right:
            node = node.left
        elif not node.left:
            node = node.right
        else:
            extra = node.right.left
            node.right.left = node.left
            l = node.left
            while l.right:
                l = l.right
            l.right = extra
            node = node.right
        if prev:
            if is_left:
                prev.left = node 
            else:
                prev.right = node
            return root
        else:
            return node 
        



