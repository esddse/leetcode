class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        
        def depth(root):
            if not root:
                return 0
            return (1 + max(depth(root.left), depth(root.right)))
        
        def helper(node, dep, level, pose):
            self.ans[level][pose] = str(node.val)
            if node.left:
                helper(node.left, dep, level+1, pose-2**(dep-level-2))
            if node.right:
                helper(node.right, dep, level+1, pose+2**(dep-level-2))
        dep = depth(root)
        self.ans = [['']*(2**dep-1) for _ in range(dep)]
        helper(root, dep, 0, (2**dep-1)>>1)
        return self.ans

