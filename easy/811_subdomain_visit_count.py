class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        
        d = {}

        for cpdomain in cpdomains:
            item = cpdomain.split(" ")
            num  = int(item[0])
            domain = item[1]

            domain = domain.split(".")
            for i in range(len(domain)):
                pdomain = ".".join(domain[i:])
                if pdomain in d:
                    d[pdomain] += num
                else:
                    d[pdomain] = num

        return [str(num)+" "+domain for domain, num in d.items()]