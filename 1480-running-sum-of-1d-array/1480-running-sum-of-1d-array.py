class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running  = 0
        \
        for i in range(len(nums)):
            running += nums[i]
            nums[i] = running
        return nums