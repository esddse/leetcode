class Node:
    def __init__(self, start, end):
        self.start = start
        self.end   = end
        self.total = 0
        self.left  = None
        self.right = None

class NumArray:

    def __init__(self, nums: List[int]):
        if not nums:
            return 
        size = len(nums)
        def build(start, end):
            if start > end:
                return None
            node = Node(start, end)
            if start == end:
                node.total = nums[start]
                return node
            else:
                m = (start + end) // 2
                node.left  = build(start, m)
                node.right = build(m+1,end)
                node.total = node.left.total + node.right.total
                return node
        self.tree = build(0, size-1)        

            
    def update(self, i: int, val: int) -> None:
        def tree_update(i, v, node):
            if node.start == node.end == i:
                node.total = v
            else:
                m = (node.start + node.end) // 2
                if i <= m:
                    tree_update(i, v, node.left)
                else:
                    tree_update(i, v, node.right)
                node.total = node.left.total + node.right.total
        tree_update(i, val, self.tree)

    def sumRange(self, i: int, j: int) -> int:
        def tree_query(i, j, node):
            if i == node.start and j == node.end:
                return node.total
            m = (node.start + node.end) // 2
            if j <= m:
                return tree_query(i, j, node.left)
            elif i > m:
                return tree_query(i, j, node.right)
            else:
                return tree_query(i, m, node.left) + tree_query(m+1, j, node.right)
        return tree_query(i, j, self.tree)
