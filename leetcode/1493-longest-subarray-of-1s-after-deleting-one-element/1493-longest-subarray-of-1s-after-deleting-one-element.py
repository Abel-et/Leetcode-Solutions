class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        window,z,l = 0,0,0

        for r in range(len(nums)):
            if nums[r] == 0:
                z+= 1
            
            while z > 1:
                if nums[l] == 0:
                    z-= 1
                l+=1
            window = max(window, r - l)
        
        return window
