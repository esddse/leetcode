from collections import defaultdict
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        

        def check_is_one_change(str1, str2):
            cnt = 0
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    cnt += 1
            if cnt != 1:
                return False
            return True

        is_valid = False
        for i, s in enumerate(bank):
            if s == end:
                is_valid = True
                bank[i], bank[-1] = bank[-1], bank[i]
                break
        if not is_valid:
            return -1


        bank = [start] + bank
        next_node = defaultdict(set)
        for i in range(len(bank)):
            for j in range(i+1, len(bank)):
                if check_is_one_change(bank[i], bank[j]):
                    next_node[i].add(j)
                    next_node[j].add(i)

        checked = [0] * len(bank)
        queue = {0}
        checked[0] = 1
        target = len(bank) - 1 
        step = 1
        while queue:
            new_queue = set()
            for node in queue:
                for n in next_node[node]:
                    if checked[n]: continue
                    checked[n] = 1
                    if n == target:
                        return step
                    new_queue.add(n)
            queue = new_queue
            step += 1
        return -1