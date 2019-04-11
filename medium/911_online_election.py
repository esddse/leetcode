
import bisect
from collections import Counter
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times, self.record = times, []
        counter = Counter()
        max_vote = -1
        lead = -1
        for person, time in zip(persons, times):
            counter[person] += 1
            vote = counter[person]
            if vote >= max_vote:
                max_vote = vote
                lead = person
            self.record.append(lead)


    def q(self, t: int) -> int:
        return self.record[bisect.bisect(self.times, t) - 1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)