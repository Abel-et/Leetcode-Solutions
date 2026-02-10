from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        container = Counter(nums)
        return [key for key,value in container.items() if value > 1]
        