class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(capacity , weights):
            day = 1
            curr_sum = 0
            for weight in weights:
                if weight + curr_sum > capacity:
                    day +=1
                    curr_sum = weight 
                else:
                    curr_sum += weight
            return day <= days


        left , right = max(weights), sum(weights)
        ans = -1
        while left <= right :
            mid = (left + right) // 2
            if check(mid, weights):
                ans = mid
                right = mid -1
            else:
                left = mid + 1
        return ans

