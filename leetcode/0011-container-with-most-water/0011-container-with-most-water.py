class Solution:
    def maxArea(self, height: List[int]) -> int:
        # using collinding two pointer apperoach
        left , right = 0 , len(height)-1
        max_area = 0

        def area(left , right , height):
            return (right-left)*height

        while left < right:
            if height[left] >= height[right]:
                max_area = max(area(left , right , height[right]), max_area)
                right -=1
            else:
                min_height = min(height[left], height[right])
                max_area = max(area(left, right, min_height), max_area)
                left += 1
        return max_area
