class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parents = {letter: letter for letter in "abcdefghijklmnopqrstuvwxyz"}

        def find(item):
            if parents[item] == item:
                return item
            parents[item] = find(parents[item])
            return parents[item]
        def merge(item1, item2):
            parent1, parent2 = find(item1), find(item2)
            parents[parent1] = parent2

        equations = sorted(equations, key=lambda string: string[1:3], reverse=True)
        for eq in equations:
            item1, item2 = eq[0], eq[-1]
            if eq[1] == "=":
                merge(item1, item2)
            else:
                if find(item1) == find(item2):
                    return False
        return True