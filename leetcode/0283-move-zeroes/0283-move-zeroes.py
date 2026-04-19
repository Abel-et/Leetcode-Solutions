class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return nums

        holder = 0
        for seeker in range(len(nums)):
            if nums[holder] != 0 :
                holder += 1
            elif nums[holder] == 0 and nums[seeker] != 0 :
                nums[holder], nums[seeker] = nums[seeker] , nums[holder]
                holder += 1
        return nums
