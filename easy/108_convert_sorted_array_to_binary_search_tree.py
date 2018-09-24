# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        def insert(tree, val):
            if val < tree.node:
                if tree.left:
                    insert(tree.left, val)
                else:
                    tree.left = TreeNode(val)
            elif val > tree.node:
                if tree.right:
                    insert(tree.right, val)
                else:
                    tree.right = TreeNode(val)

        def construct(nums):
            if not nums:
                return None
            if len(nums) == 1:
                return TreeNode(nums[0])
            mid = len(nums) // 2
            node = TreeNode(nums[mid])
            node.left  = construct(nums[:mid])
            node.right = construct(nums[mid+1:])
            return node

        return construct(nums)
