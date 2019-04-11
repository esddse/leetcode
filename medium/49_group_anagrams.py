from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = defaultdict(list)
        for word in strs:
            c = Counter(word)
            hashstr = "".join([str(c[a]) for a in "abcdefghijklmnopqrstuvwxyz"])
            ana_dict[hashstr].append(word)
        return [v for k, v in ana_dict.items()]