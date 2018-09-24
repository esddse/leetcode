class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """

        stack = []
        time_spend = [0] * n
        prev_time = 0

        for log in logs:
            fid, tag, timestamp = log.split(":")
            fid, timestamp = int(fid), int(timestamp)
            if tag == "start":
                if stack:
                    time_spend[stack[-1]] += timestamp - prev_time
                stack.append(fid)
                prev_time = timestamp
            else:
                time_spend[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1
            
        return  time_spend