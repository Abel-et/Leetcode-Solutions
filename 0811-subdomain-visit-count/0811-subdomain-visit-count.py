from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain = defaultdict(int)

        for i in cpdomains:
            k=i.split('.')
            root = k[0].split()
            full = f"{root[1]}.{'.'.join(k[1:])}"
            domain[full] +=int(root[0])

            for i in range(1,len(k)):
                dom = '.'.join(k[i:])
                domain[dom] += int(root[0])
        return [f"{value} {key}" for key , value in domain.items()]

            
            
        