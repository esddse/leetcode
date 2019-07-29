class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:

        i, give = 0, 1
        ret = [0] * num_people
        while candies > 0:
            ret[i] += min(give, candies)
            candies -= give
            i = (i+1) % num_people
            give += 1 
        return ret