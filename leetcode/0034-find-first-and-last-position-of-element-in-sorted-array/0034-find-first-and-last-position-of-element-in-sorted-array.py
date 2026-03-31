class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def get_starging_positon(nums, target):
            left, right = 0 , len(nums)-1
            ans = -1
            mid = 0

            while left <= right:

                mid = (left + right)// 2

                if nums[mid] == target:
                    ans = mid
                    right = mid -1
                elif nums[mid] > target:
                    right = mid -1
                else:
                    left = mid + 1
            return ans 

        def get_end_position(nums, target):
            left, right = 0 , len(nums)-1
            ans = -1
            mid = 0

            while left <= right:

                mid = (left + right)// 2

                if nums[mid] == target:
                    ans = mid
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid -1
                else:
                    left = mid + 1
            return ans 
        return [get_starging_positon(nums, target),get_end_position(nums , target)]

        