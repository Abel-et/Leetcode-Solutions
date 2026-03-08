from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        prefix_sum ,cnt = 0, 0
        
        for num in nums:
            prefix_sum += num

            if prefix_sum - k in prefix:
                cnt += prefix[prefix_sum - k]
            prefix[prefix_sum] +=1
        return cnt
      