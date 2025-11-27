class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if i == 0:
                if sum(nums[i+1:]) == 0:
                    return 0
            elif i == n:
                if sum(nums[:i+1]) == 0:
                    return i
            else:
                if sum(nums[:i]) == sum(nums[i+1:]):
                    return i
        else:
            return -1