class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left , right = 0 , len(nums)-1

        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            if left == right:
                if nums[left] < target:
                    return left + 1
                else:
                    return left

            elif nums[mid] > target:
                if mid == 0 and nums[mid] > target:
                    return 0
                if nums[mid] + 1 == target:
                    return mid+ 1
                right = mid -1
                
            elif nums[mid] < target:
                if nums[mid] + 1 == target:
                    return mid +1
                left  = mid +1
       