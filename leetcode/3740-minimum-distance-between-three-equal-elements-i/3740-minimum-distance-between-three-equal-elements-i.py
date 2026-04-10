from collections import defaultdict
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        map = defaultdict(list)
        ans = []

        if len(nums) < 3:
            return -1

        def good (i , j , k):
            return abs(i - j) + abs(j - k) + abs(k - i)
        
        for index, val in enumerate(nums):
            map[val].append(index)
         
        
        for key ,val in map.items():
            if len(val) >= 3:
                val.sort()
                for i in range(len(val)-3+1):
                    ans.append(good(val[i],val[i+1],val[i+2]))
            else:
                continue
        return min(ans) if  ans else -1
