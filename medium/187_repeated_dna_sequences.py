class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        size = len(s)
        repeat_seqs = set()
        storage = set()
        start, end = 0, 9
        while end < size:
            seq = s[start: end+1]
            if seq in storage:
                repeat_seqs.add(seq)
            else:
                storage.add(seq)
            start, end = start+1, end+1
        return list(repeat_seqs)