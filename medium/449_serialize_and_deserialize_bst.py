# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        def dfs(node, ret):
            ret.append(str(node.val))
            if node.left:
                dfs(node.left, ret)
            if node.right:
                dfs(node.right, ret)
        ret = []
        dfs(root, ret)
        return "\t".join(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return []
        vals = data.split("\t")
        root = TreeNode(int(vals[0]))
        def insert(node, val):
            if val < node.val:
                if not node.left:
                    node.left = TreeNode(val)
                else:
                    insert(node.left, val)
            if val > node.val:
                if not node.right:
                    node.right = TreeNode(val)
                else:
                    insert(node.right, val)

        for val in vals[1:]:
            insert(root, int(val))
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))