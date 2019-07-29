class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        size = len(people)
        people.sort()

        cnt = 0
        i, j = 0, size-1
        while i < j:
            if people[i] + people[j] <= limit:
                i += 1
                j -= 1
            else:
                j -= 1
            cnt += 1
        if i == j:
            cnt += 1
        return cnt