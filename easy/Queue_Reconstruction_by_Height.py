class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if people == []:
            return []
        d = {}
        for person in people:
            if person[0] in d:
                d[person[0]].append(person[1])
            else:
                d[person[0]] = [person[1]]
        d = sorted(d.items(), key = lambda item: item[0])
        for i in range(len(d)):
            d[i][1].sort()
        
        q = [[d[-1][0], x] for x in d[-1][1]]
        for i in range(len(d)-1):
            i = len(d) - 2 - i
            num = d[i][0]
            lst = d[i][1]
            for l in lst:
                q.insert(l, [num, l])
            
            
        return q
                
                