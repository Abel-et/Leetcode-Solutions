class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = max(nums)

        for i in range(n):
            if i not in nums:
                return i
        else:
            return n+1