class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            j = i+1
            if nums[i] == nums[j]:
                return nums[i]