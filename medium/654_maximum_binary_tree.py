# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def find_max(self, lst):
        max_num = lst[0]
        max_index = 0
        for i, num in enumerate(lst):
            if num > max_num:
                max_num = num
                max_index = i
        return max_num, max_index

    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None

    	max_num, max_index = self.find_max(nums)

    	node = TreeNode(max_num)
    	node.left  = self.constructMaximumBinaryTree(nums[:max_index])
    	node.right = self.constructMaximumBinaryTree(nums[max_index+1:])

        return node

    