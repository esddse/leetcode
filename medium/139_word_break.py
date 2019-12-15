class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        size = len(s)
        end_idx = [-1]
        for i in range(size):
            for end in end_idx:
                start = end+1
                if s[start:i+1] in wordDict:
                    end_idx.append(i)
                    break
        if end_idx[-1] == size-1:
            return True 
        return False