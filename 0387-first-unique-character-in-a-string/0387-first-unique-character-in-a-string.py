from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        container = defaultdict(int)
        for i in s:
            container[i] +=1
        for key, value in container.items():
            if value == 1:
                return s.index(key)
        else:
            return -1
        
        