class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        # find k level friends
        queue, l, checked = set([id]), 0, set([id])
        while queue and l < level:
            new_queue = set()
            for i in queue:
                for f in friends[i]:
                    if f not in checked:
                        new_queue.add(f)
                        checked.add(f)
            l += 1
            queue = new_queue

        # TV
        counter = {}
        for i in queue:
            for v in watchedVideos[i]:
                if v not in counter:
                    counter[v] = 1
                else:
                    counter[v] += 1
        ret = sorted(counter.keys(), key=lambda v: (counter[v], v))
        return ret