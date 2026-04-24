class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        rt = sorted(nums1 + nums2)
        if len(rt)<2:
            return rt[0]
        elif len(rt)%2 != 0:
            index = int(len(rt)/2)
            return float(rt[index])
        else:
            index1 = int(len(rt)/2)
            index2 = int(len(rt)/2 - 1)
            sum = rt[index1] + rt[index2]
            return float(sum/2)