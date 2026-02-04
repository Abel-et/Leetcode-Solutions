class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        unique = set(nums)
        for i in range(1,len(nums)+1):
            if i not in unique:
                arr.append(i)
        return arr