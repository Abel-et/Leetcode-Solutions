import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix start from the first to the end and postfix starts form the end and comes to first 
        postfix,prefix = 1,1

        # an output arr which hold 1 on all its indexes
        res = [1]*(len(nums))

        # a pointer which start from last end decrement 
        from_the_last = len(nums)-1

        for i in range(len(nums)):
            # updating the output arr by adding the prefix value
            res[i] *= prefix
            prefix *= nums[i]

            # multiplying the output arr elemenst from the last to the first 
            res[from_the_last-i] *= postfix
            postfix *= nums[from_the_last - i]
        return res