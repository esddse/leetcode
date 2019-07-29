class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        
        tree = []
        d, p = 1, 0
        while len(tree) < label:
            layer = list(range(2 ** p, 2 ** (p+1)))
            if d < 0:
                layer.reverse()
            tree += layer
            d *= -1
            p += 1
        ret = []
        pos = tree.index(label)
        while pos != 0:
            ret.append(tree[pos])
            if pos % 2 == 1:
                pos = (pos - 1) // 2
            else:
                pos = (pos - 2) // 2
        ret.append(tree[0])
        ret.reverse()
        return ret


