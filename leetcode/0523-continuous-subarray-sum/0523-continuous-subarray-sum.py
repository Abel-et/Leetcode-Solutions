class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        remainder_map = {0: -1}
        current_sum = 0
       
        for i in range(len(nums)):
            current_sum += nums[i]
            remainder = current_sum % k
            
            if remainder in remainder_map:
                # Check if the length of this subarray is at least 2
                if i - remainder_map[remainder] > 1:
                    return True
            else:
                remainder_map[remainder] = i
        
        else:
            return False
