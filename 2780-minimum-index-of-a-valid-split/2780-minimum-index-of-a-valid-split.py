from collections import Counter
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # if the length is equal to one should return it self
        if len(nums) == 1:
            return -1

        # if the length is equal to two have two chances 
        if len(nums) == 2:
            if len(nums) != len(set(nums)):
                return 0
            else:
                return -1
        
        # finding dominant element for the give arr
        dom_element = max(Counter(nums), key= Counter(nums).get)
        
        # creating a helper function which return boolean of if it is dominant in the give arr or not 
        def isdom(arr,dom):
            dom_element = arr.count(dom)
            if len(arr) == dom_element:
                return True
            return dom_element > (len(arr)//2)
        
        # creating mid point which split the given arr from the begining of the dominant element
        mid_point = nums.index(dom_element) + 1

        # Travers through each element usign for loop to split and get valid split
        for _ in range(len(nums)):
            if mid_point == 0 or mid_point > (len(nums)-1):
                return -1
            left = isdom(nums[:mid_point], dom_element)
            right = isdom(nums[mid_point:], dom_element)
            if left and right:
                return mid_point - 1
            elif not left:
                mid_point += 1
            else:
                mid_point -= 1
        else:
            return -1

        