class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        n = len(nums)
        arr = [0]*n
        unique = set(nums) 
        if len(unique) == 1:
            return arr
        arr1 = []
        c = 0
        
        for i in range(n):
            for j in range(n):
                if nums[i] > nums[j]:
                    c+=1
            arr1.append(c)
            c = 0
        return arr1