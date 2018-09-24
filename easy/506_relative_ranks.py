class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranked_scores = sorted(nums, reverse=True)
        score2rank = {ranked_scores[rank]:rank for rank in range(len(nums))}

        awards = []
        for score in nums:
            rank = score2rank[score]
            if rank == 0:
                award = "Gold Medal"
            elif rank == 1:
                award = "Silver Medal"
            elif rank == 2:
                award = "Bronze Medal"
            else:
                award = str(rank+1)
            awards.append(award)
        return awards