from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []

        for row in grid:
            for val in row:
                nums.append(val)

        # check possibility
        rem = nums[0] % x

        for num in nums:
            if num % x != rem:
                return -1

        nums.sort()

        median = nums[len(nums) // 2]

        ops = 0

        for num in nums:
            ops += abs(num - median) // x

        return ops