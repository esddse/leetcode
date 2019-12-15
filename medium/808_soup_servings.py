class Solution:
    def soupServings(self, N: int) -> float:
        if N > 4800:
            return 1

        prob_map = {}
        
        def prob_a_empty_first(a, b):
            if (a, b) in prob_map:
                return prob_map[(a, b)]
            if a <= 0 and b > 0:
                prob = 1
            elif a <= 0 and b <= 0:
                prob = 0.5 
            elif a > 0 and b <= 0:
                prob = 0
            else:
                prob_1 = prob_a_empty_first(a-100, b)
                prob_2 = prob_a_empty_first(a-75, b-25)
                prob_3 = prob_a_empty_first(a-50, b-50)
                prob_4 = prob_a_empty_first(a-25, b-75)
                prob = 0.25 * (prob_1+prob_2+prob_3+prob_4)

            prob_map[(a, b)] = prob 
            return prob

        return prob_a_empty_first(N, N)