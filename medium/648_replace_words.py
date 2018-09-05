class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        
        words = sentence.split(" ")

        for i in range(len(words)):
            word = words[i]
            min_root = word
            for root in dict:
                if word.startswith(root):
                    if len(root) < len(min_root):
                        min_root = root
            words[i] = min_root
        return " ".join(words)