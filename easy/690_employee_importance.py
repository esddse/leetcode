"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """

        uid_val, uid_sub, checked = {}, {}, {}

        for employee in employees:
            uid = employee.id
            val = employee.importance
            sub = employee.subordinates
            uid_val[uid] = val 
            uid_sub[uid] = sub
            checked[uid] = False

        total = 0
        q = [id]
        while q:
            new_q = []
            for uid in q:
                checked[uid] = True
                total += uid_val[uid]
                for sub in uid_sub[uid]:
                    if not checked[sub]:
                        new_q.append(sub)
            q = new_q
        return total