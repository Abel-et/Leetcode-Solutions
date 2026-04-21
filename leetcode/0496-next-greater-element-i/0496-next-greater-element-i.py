class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        collect = []
        def check(arr,target,index):
            for i in range(index, len(arr)):
                if arr[i] > target:
                    return arr[i]
            return -1
            
        
        for i in nums1:
            index = nums2.index(i)
            collect.append(check(nums2,i,index))
        return collect

        