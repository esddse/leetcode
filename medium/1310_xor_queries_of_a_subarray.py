class Node:
    def __init__(self, l, r):
        self.val = None
        self.l, self.r = l, r
        self.left, self.right = None, None

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        def build(l, r):
            if l == r:
                node = Node(l, r)
                node.val = arr[l]
            else:
                node = Node(l, r)
                m = (l + r) // 2
                node.left = build(l, m)
                node.right = build(m+1, r)
            return node
              
        def query(l, r, node):
            if node.l == l and node.r == r and node.val:
                return node.val, node.val
            nodem = (node.l + node.r) // 2
            if r <= nodem:
                return query(l, r, node.left)[0], node.val
            elif l > nodem:
                return query(l, r, node.right)[0], node.val
            else:
                ret_l, val_l = query(l, nodem, node.left)
                ret_r, val_r = query(nodem+1, r, node.right)
                if val_l is not None and val_r is not None:
                    node.val = val_l ^ val_r
                ret = ret_l ^ ret_r
                return ret, node.val
          
        tree = build(0, len(arr)-1)
        ans = []
        for l, r in queries:
            ans.append(query(l, r, tree)[0])
        return ans