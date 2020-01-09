# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
    
        def dfs(node, lst):
            if not node:
                return 
            dfs(node.left, lst)
            lst.append(node.val)
            dfs(node.right, lst)
            return 
        
        lst1, lst2 = [], []
        dfs(root1, lst1)
        dfs(root2, lst2)
        
        lst = []
        while lst1 and lst2:
            if lst1[0] < lst2[0]:
                lst.append(lst1[0])
                lst1 = lst1[1:]
            else:
                lst.append(lst2[0])
                lst2 = lst2[1:]
        if lst1:
            lst += lst1 
        if lst2:
            lst += lst2 
        return lst 