class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def atMost(target):
            if target < 0:
                return 0
            
            res = 0
            left = 0
            current_sum = 0
            
            for right in range(len(nums)):
                current_sum += nums[right]
                
                # Shrink window if sum exceeds target
                while current_sum > target:
                    current_sum -= nums[left]
                    left += 1
                
                # All subarrays ending at 'right' and starting from 'left' to 'right'
                # have a sum <= target. The count of these is (right - left + 1).
                res += (right - left + 1)
            
            return res
        
        return atMost(goal) - atMost(goal - 1)