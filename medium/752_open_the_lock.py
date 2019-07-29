class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        checked = set(deadends)
        move = {str(i):[str((i + 1) % 10), str((i - 1) % 10)] for i in range(10)}
        q = ["0000"]
        step = 0
        if "0000" in checked:
            return -1
        checked.add("0000")
        while q:
            new_q = []
            for lock in q:
                if lock == target:
                    return step
                for i in range(4):
                    for sub in move[lock[i]]:
                        new_lock = lock[:i] + sub + lock[i+1:]
                        if new_lock not in checked:
                            new_q.append(new_lock)
                            checked.add(new_lock)
            step += 1
            q = new_q
        return -1
