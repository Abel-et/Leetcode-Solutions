class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)

        # left , right = 0 , len(nums) - 1

        # while left <= right:
        #     mid = (left + right)//2

        #     if  nums[mid + 1] < nums[mid] and nums[mid] > nums[mid-1]:
        #         if nums[mid + 1] > nums[mid -1]:
        #             right = mid -1
        #         else:
        #             left = mid + 1
        #     elif nums[mid + 1] > nums[mid]  and nums[mid-1] < nums[mid]:
        #         right = mid -1
        #     else:
        #         left = mid +1
        # return nums[left]