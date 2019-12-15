from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0
        word_len = len(beginWord)
        charDict = defaultdict(set)
        checked = {}
        for word in wordList:
            checked[word] = False
            for i, c in enumerate(word):
                charDict[i].add(c)

        queue = [beginWord]
        checked[beginWord] = True
        step = 1
        while queue:
            new_queue = []
            for word in queue:
                if word == endWord:
                    return step
                for i in range(word_len):
                    for c in charDict[i]:
                        new_word = word[:i]+c+word[i+1:]
                        if new_word in checked and not checked[new_word]:
                            checked[new_word] = True 
                            new_queue.append(new_word)
            queue = new_queue
            step += 1
        return 0
                    
                