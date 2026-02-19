from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # s used to conver all nums int elements into string 
        s = []
        for i in nums:
            s.append(str(i))

#       this compare  3 and 30 make 330 or 303 and return 1 or -1
        def compare(a,b):
            if a + b > b + a:
                return -1
            else:
                return 1
        
        # sort based ot the sumation of elements in give arr
        s.sort(key= cmp_to_key(compare))
        largest = "".join(s)
        
        # return result by convering into string because of size
        return str(largest)

