# LeetCode Problem: Count_Hills_and_Valleys_in_an_Array
# Problem Link: https://leetcode.com/problems/count-hills-and-valleys-in-an-array/
# Difficulty: Easy

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        change = 0

        def check(left, m, right):
            print(left, m, right)
            if (left < m and right < m):
                return 1
            elif (left > m and right > m):
                return 1
            else:
                print("in else ", left, m, right)
                return 0

        for i in range(1, len(nums) - 1):
            index = i
            left = nums[i - 1]
            m = nums[i]
            right = nums[i + 1]
            if m == left and m == right:
                continue
            elif m == right:
                while index < len(nums) and right == m:
                    right = nums[index]
                    index += 1
                change += check(left, m, right)
            elif m == left:
                continue
            else:
                change += check(left, m, right)
        return change
