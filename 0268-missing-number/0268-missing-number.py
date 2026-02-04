class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        max = nums[-1]
        for index ,value in enumerate(nums):
            if index != value:
                return index
        else:
            return max+1