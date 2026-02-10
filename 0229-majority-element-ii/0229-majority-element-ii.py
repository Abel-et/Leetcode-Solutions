class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        container = {}
        for i in nums:
            container[i] = container.get(i,0)+1
        return [key for key ,value in container.items() if value > len(nums)//3]
        