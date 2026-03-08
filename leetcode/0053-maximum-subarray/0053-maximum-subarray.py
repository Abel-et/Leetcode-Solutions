class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # the problem need to select add the current element or choose to start form this element
        max_sum = nums[0]
        curr_sum = nums[0]

        for num in nums[1:]:
            # if the current element is greater sum of current and the current element choose current element
            curr_sum = max(num, curr_sum + num)

            # hold the max form curr_SUM or prev max sum 
            max_sum = max(max_sum, curr_sum)
        return max_sum