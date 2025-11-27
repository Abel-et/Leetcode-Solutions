# LeetCode Problem: 2221. Find Triangular Sum of an Array
# Problem Link: https://leetcode.com/problems/find-triangular-sum-of-an-array
# Difficulty: Medium
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        new = []
        while n > 1:
            for i in range(n - 1):
                a = (nums[i] + nums[i + 1]) % 10
                new.append(a)
            nums = new[:]
            n = len(nums)
            new.clear()
        return nums[0]

