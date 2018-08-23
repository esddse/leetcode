class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        alphabet = "abcdefghijklmnopqrstuvwxyz"
        pos_dict = {}
        for letter in alphabet:
            pos_dict[letter] = {"start":None, "end":None}

        for i, c in enumerate(S):
            if pos_dict[c]["start"] is None:
                pos_dict[c]["start"] = i
                pos_dict[c]["end"] = i
            else:
                pos_dict[c]["end"] = i

        partition = []
        p, start, end = 0, 0, 0
        while p < len(S):
            while p <= end:
                if pos_dict[S[p]]["end"] > end:
                    end = pos_dict[S[p]]["end"]
                p += 1
            partition.append(end-start+1)
            start, end = p, p

        return partition

        
