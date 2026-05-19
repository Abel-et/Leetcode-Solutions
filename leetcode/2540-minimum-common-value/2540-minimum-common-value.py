class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        return -1 if sorted(set(nums2) & set(nums1))  == [] else sorted(set(nums2) & set(nums1))[0]