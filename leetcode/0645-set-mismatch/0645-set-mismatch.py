from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        conut = Counter(nums)

        dup = 1
        for key,val in conut.items():
            if val > 1:
                dup = key
                break
        missing = 1
        nums.sort()
        for index, element in enumerate(nums):
            if index + 1 != element:
                if index+1 not in nums:
                    missing = index+1
                    return [dup, missing]
        
        else:
            missing = max(nums) +1 
        return [dup, missing]


        