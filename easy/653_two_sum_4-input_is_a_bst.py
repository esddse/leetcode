class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        

        def find(root, k, num):
            if not root or num < 1:
                return False
            if num == 1 and root.val == k:
                return True

            not_select = find(root.left, k, num) or find(root.right, k, num)
            select = find(root.left, k-root.val, num-1) or find(root.right, k-root.val, num-1)
            return not_select or select

        return find(root, k, 2)