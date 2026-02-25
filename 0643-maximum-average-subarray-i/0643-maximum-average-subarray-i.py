class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = 0
        max_sum =  float('-inf')

        for i in range(k):
            curr_sum += nums[i]

        max_sum = curr_sum

        for j in range(k,len(nums)):
            curr_sum +=nums[j] -nums[j-k]
            max_sum = max(curr_sum,max_sum)

        return max_sum/k
