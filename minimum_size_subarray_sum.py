# LeetCode Problem: minimum Subarray Sum
# Problem Link:https://leetcode.com/problems/minimum-size-subarray-sum/
# Difficulty: medium
def minimumSubarraySum(self, nums):
    left = 0
    n = 0
    length = float('inf')
    for right in range(len(nums)):
        n += nums[right]
        while n >= target:
            length = min(length, right - left + 1)
            n -= nums[left]
            left += 1
    return 0 if length == float('inf') else length