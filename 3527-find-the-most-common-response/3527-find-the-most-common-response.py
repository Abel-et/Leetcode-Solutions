from collections import Counter
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count = Counter()
        # getting each elements frequecy in every day
        for i in responses:
            count.update(set(i))
        
        # getting the highest element appear all the days
        max_value = max(count.values())

        # assing elements which have highest apperance
        max_element = [k for k,v in count.items() if v == max_value]

        # sorting lexicographically smallest 
        max_element.sort()
        
        return max_element[0]
        