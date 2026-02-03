class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c =0
        n = len(nums)
        maxc =0
        for i in range(n):
            if nums[i] == 1:
                c+=1
                if i ==n-1:
                    maxc = max(c,maxc)
            else:
                maxc= max(c,maxc)
                c = 0
        return maxc

