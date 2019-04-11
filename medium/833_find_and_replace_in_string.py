class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        replacements = sorted(zip(indexes, sources, targets), key=lambda item:item[0])
        length = len(S)
        start = 0
        new_S = ""
        for idx, source, target in replacements:
            if idx >= length:
                break
            new_S += S[start:idx]
            sl = len(source)
            if S[idx:idx+sl] == source:
                new_S += target 
                start = idx+sl
            else:
                start = idx
        new_S += S[start:]
        return new_S