class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        
        for i in range(len(nums)-2):
            a,b = nums[i+1],nums[i+2]
            c = nums[i]
            if (a+b) > c:
                return a + b + c
        else:
            return 0