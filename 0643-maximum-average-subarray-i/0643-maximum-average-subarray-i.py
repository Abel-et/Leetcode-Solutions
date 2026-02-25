class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        max_sum =  float('-inf')

        max_sum = curr_sum

        for j in range(k,len(nums)):
            curr_sum +=nums[j] -nums[j-k]
            max_sum = max(curr_sum,max_sum)

        return max_sum/k
