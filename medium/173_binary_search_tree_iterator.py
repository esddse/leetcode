# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.lst = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            self.lst.append(node.val)
            dfs(node.right)
        dfs(root)

        self.length = len(self.lst)
        self.p = 0

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.p < self.length
        

    def next(self):
        """
        :rtype: int
        """
        val = self.lst[self.p]
        self.p += 1
        return val
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())