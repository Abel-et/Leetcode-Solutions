# class Solution:
#     def maxDistance(self, colors: List[int]) -> int:
#         left, right = 0, len(colors) - 1
#         maxd = 0
        
#         # Original user logic (re-simulated)
#         # Part 1
#         temp_l, temp_r = left, right
#         while temp_l < temp_r:
#             if colors[temp_l] != colors[temp_r]:
#                 maxd = max(maxd, abs(temp_l - temp_r))
#                 temp_l += 1
#             temp_r -= 1
        
#         # Part 2
#         temp_l, temp_r = left, right
#         while temp_l < temp_r:
#             if colors[temp_l] != colors[temp_r]:
#                 maxd = max(maxd, abs(temp_l - temp_r))
#                 temp_r -= 1
#             temp_l += 1
            
#         return maxd

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        l ,r= 0 ,len(colors)-1

        maxd = 0
        left ,right = l, r
        while left < right:
            if colors[left] != colors[right]:
                maxd = max(maxd, abs(left - right))
                left += 1
            right -= 1

        left ,right = l, r
        while left < right:
            if colors[left] != colors[right]:
                maxd = max(maxd, abs(left - right))
                right -=1
            left +=1
        return maxd