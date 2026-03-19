class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def max_differ(left,right):
            # base case ,when all the arr elements are finished
            if left == right:
                return nums[left]
        
            left_part = nums[left] - max_differ(left+1,right)
            
            right_part = nums[right] - max_differ(left , right - 1)

            return max(left_part, right_part)
        return max_differ(0,len(nums)-1) >= 0

