from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        email2idx = {}
        idx2name = {}
        parents = [i for i in range(len(accounts))]

        def find(idx):
            if parents[idx] == idx:
                return idx 
            else:
                parents[idx] = find(parents[idx])
                return parents[idx]

        def merge(idx1, idx2):
            parent1 = find(idx1)
            parent2 = find(idx2)
            parents[parent1] = parent2


        for idx, account in enumerate(accounts):
            name = account[0]
            idx2name[idx] = name

            emails = account[1:]
            for email in emails:
                if email not in email2idx:
                    email2idx[email] = idx 
                else:
                    prev_idx = email2idx[email]
                    merge(idx, prev_idx)

        parent2emails = defaultdict(list)
        for email, idx in email2idx.items():
            parent2emails[find(idx)].append(email)

        ret = [[idx2name[idx]]+sorted(emails) for idx, emails in parent2emails.items()]
        return ret