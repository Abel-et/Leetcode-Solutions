class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        if len(nums) <3:
            return nums
        left = nums[:n]
        right = nums[n:]
        combined = []
        for i in range(n):
            combined.append(left[i])
            combined.append(right[i])
        return combined

        