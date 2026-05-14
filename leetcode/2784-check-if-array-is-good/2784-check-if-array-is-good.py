class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        nums.sort()

        for i in range(n):
            if i+1 != nums[i]:
                return False
        return True if nums[-1] == n else False
