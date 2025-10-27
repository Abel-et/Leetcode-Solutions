# LeetCode Problem:max-consecutive-ones
# Problem Link:https://leetcode.com/problems/max-consecutive-ones/
# Difficulty: easy

def findMaxConsecutiveOnes(self, nums):
    l = 0
    left = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            left = right +1
        l = max(l, right - left +1)
    return l