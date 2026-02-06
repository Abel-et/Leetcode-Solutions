from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collector  = {}

        for i in strs:
            new ="".join(sorted(i))
            if new not in collector:
                collector[new] = []
                collector[new].append(i)
            else:
                collector[new].append(i)
           
        values = list(collector.values())
        angrams = sorted(values , key=len)
        return angrams



        