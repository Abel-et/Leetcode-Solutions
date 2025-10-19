# LeetCode Problem: Contain Duplicate 2 .
# Problem Link:https://leetcode.com/problems/contains-duplicate-ii/?envType=problem-list-v2&envId=sliding-windowhttps://leetcode.com/problems/contains-duplicate-ii/?envType=problem-list-v2&envId=sliding-window
# Difficulty: Easy

def containsNearbyDuplicate(self, nums, k):
    if k <= 0:
        return False
    window = set()
    n = len(nums)
    for i, x in enumerate(nums):
        if x in window:
            return True
        window.add(x)
        if len(window) > k:
            window.remove(nums[i - k])
    return False
