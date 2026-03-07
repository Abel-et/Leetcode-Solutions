import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # the problem is to put a product of all element in the arr which not include the current elemnt 
        # and division is not allowed to solve this task  
        #           approch 
        #   first prepare an output arr which is every its elemnts is one 
        #   then multiply it all element from starting to the end and from the end to the starting 

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