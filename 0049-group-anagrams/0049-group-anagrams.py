from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collector  =defaultdict(list)
        for i in strs:
            collector["".join(sorted(i))].append(i) 
        return sorted(list(collector.values()) , key=len)
        



        