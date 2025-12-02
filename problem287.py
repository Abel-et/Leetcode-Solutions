# LeetCode Problem:  Find the Duplicate Number
# Problem Link: https://leetcode.com/problems/find-the-duplicate-number/description/?envType=problem-list-v2&envId=two-pointers
# Difficulty: Medium
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            j = i+1
            if nums[i] == nums[j]:
                return nums[i]