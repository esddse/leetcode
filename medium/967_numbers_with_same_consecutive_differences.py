class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            return [i for i in range(10)]
        queue = {i for i in range(1, 10)}
        N -= 1
        while N:
            new_queue = set()
            for num in queue:
                last = num % 10
                plus  = last + K
                if 0<=plus<10:
                    new_queue.add(num*10+plus) 
                minus = last - K
                if 0<=minus<10:
                    new_queue.add(num*10+minus)
            queue = new_queue
            N -= 1
        return list(queue)
        