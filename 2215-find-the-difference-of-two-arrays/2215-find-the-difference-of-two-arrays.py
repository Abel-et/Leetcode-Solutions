class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1) - set(nums2)
        set2 = set(nums2) - set(nums1)
        return [list(set1),list(set2)]
     