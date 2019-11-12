from collections import Counter, deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(senate)
        ban_r, ban_d = 0, 0
        counter = Counter(queue)
        if counter["R"] == 0: return "Dire"
        if counter["D"] == 0: return "Radiant"
        while True:
            senator = queue.popleft()
            if senator == "R":
                if ban_r:
                    ban_r -= 1
                    counter["R"] -= 1
                    if counter["R"] == 0:
                        return "Dire"
                else:
                    queue.append(senator)
                    ban_d += 1
            else:
                if ban_d:
                    ban_d -= 1
                    counter["D"] -= 1
                    if counter["D"] == 0:
                        return "Radiant"
                else:
                    queue.append(senator)
                    ban_r += 1
