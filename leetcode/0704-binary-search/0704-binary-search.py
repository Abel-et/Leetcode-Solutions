class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low , high , = 0 , len(nums)-1 
        mid = (low + high)//2

        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid -1
                
        if nums[mid] == target:
            return mid
        else :
            return -1     
        