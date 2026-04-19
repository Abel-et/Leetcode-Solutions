class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        
        # using for-while combo approach
        ans = 0
        j = 0
        for i in range(len(nums1)):
            while  j < len(nums2) and nums1[i] <= nums2[j]:
                j +=1
            if i <= j:
                ans = max(ans, abs(i - j))
        return ans - 1 if ans > 1 else 0