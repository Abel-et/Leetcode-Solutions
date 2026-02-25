from collections import defaultdict
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        classifier = defaultdict(list)

        for i in arr:
            ones = bin(i).count('1')
            classifier[ones].append(i)
        
        keys = list(classifier.keys())
        keys.sort()
        print(keys)

        return [val for key in keys  for val in sorted(classifier[key])]
     