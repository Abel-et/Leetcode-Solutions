import math

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
        def can_reduce_in_time(T: int) -> bool:
            """Checks if all workers can reduce the mountain height by at least
            mountainHeight within T seconds."""
            total_height_removed = 0
            for w in workerTimes:
                # To find max height 'x' worker can remove in time T:
                # w * (x * (x + 1) / 2) <= T
                # Solving the quadratic: x^2 + x - (2T/w) <= 0
                # Using quadratic formula: x = (-1 + sqrt(1 + 8T/w)) / 2
                x = int((-1 + math.isqrt(1 + (8 * T) // w)) // 2)
                total_height_removed += x
                
                # Optimization: stop early if we've already reached the goal
                if total_height_removed >= mountainHeight:
                    return True
            return total_height_removed >= mountainHeight

        # Set the binary search range
        # Low: 1 second
        # High: Worst case (one slow worker reducing the whole mountain)
        low = 1
        high = 10**16 # Sufficiently large for constraints
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if can_reduce_in_time(mid):
                ans = mid
                high = mid - 1 # Try to find a smaller valid time
            else:
                low = mid + 1 # Need more time
        
        return ans
