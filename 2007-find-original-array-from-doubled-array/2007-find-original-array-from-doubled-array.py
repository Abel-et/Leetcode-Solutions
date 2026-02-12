from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # if the give arr length is not even can be doubled
        if len(changed)%2 == 1:
            return []
        
        # hold each elements as a key and their frequency as a value , original hold elements after process
        freq = Counter(changed)
        original = []

        # iterating each elements of dictionary 
        for x in sorted(freq):
            if freq[x] == 0 :
                continue
            
            # handling the when zero in the changed arr
            if x == 0:
                if freq[x]%2 == 1:
                    return []
                original.extend([0]* (freq[x]//2))
            
            else:
                if freq[2*x] < freq[x]:
                    return []
                original.extend([x]*freq[x])
                freq[2*x] -=freq[x]
        return original




        