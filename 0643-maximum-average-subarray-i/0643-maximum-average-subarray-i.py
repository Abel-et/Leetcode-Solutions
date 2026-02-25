class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = 0
        max_sum = 0

        for i in range(k):
            curr_sum += nums[i]

        max_sum = max(curr_sum/k,max_sum)

        for j in range(k,len(nums)):
            curr_sum +=nums[j]
            curr_sum -=nums[j-k]
            max_sum = max(curr_sum/k,max_sum)
            
        return max_sum
