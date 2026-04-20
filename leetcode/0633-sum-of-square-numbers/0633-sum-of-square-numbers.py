import math 

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # using binary search  [0 , sqrt(c)]
        for a in range(int(math.sqrt(c)) + 1):
            target = c - (a * a)
            low, high = 0, int(math.sqrt(c))

            while low <= high:
                mid = low + (high - low) // 2
                mid_sqr = mid * mid

                if mid_sqr == target:
                    return True 
                elif mid_sqr < target:
                    low = mid + 1
                else:
                    high = mid - 1
        return False
