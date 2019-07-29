# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        
        candidates = {i for i in range(1, 11)}
        while len(candidates) > 1:
            new_candidates = None 
            while not new_candidates:
                d = {i: rand7() for i in candidates}
                new_candidates = {i for i, v in d.items() if v == 1}
            candidates = new_candidates
        return list(candidates)[0]