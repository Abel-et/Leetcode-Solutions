# LeetCode Problem: Intersection of Two Array
# Problem Link: https://leetcode.com/problems/intersection-of-two-arrays/
# Difficulty: Easy


def intersection(self, nums1, nums2):
    unique = []
    n, m = len(nums1), len(nums2)
    if n == 0 or m == 0:
        return unique
    if n > m:
        for i in nums2:
            if i in nums1:
                unique.append(i)
    else:
        for i in nums1:
            if i in nums2:
                unique.append(i)
    result = list(set(unique))
    return result
