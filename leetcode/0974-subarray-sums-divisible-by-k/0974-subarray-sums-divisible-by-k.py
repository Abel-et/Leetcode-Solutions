
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Map to store frequency of remainders
        # Key: remainder, Value: count
        remainder_freq = {0: 1}
        
        current_sum = 0
        total_subarrays = 0
        
        for num in nums:
            current_sum += num
            remainder = current_sum % k
            
            # If this remainder has been seen before,
            # it means there are subarrays ending here divisible by k
            if remainder in remainder_freq:
                total_subarrays += remainder_freq[remainder]
                remainder_freq[remainder] += 1
            else:
                remainder_freq[remainder] = 1
                
        return total_subarrays
