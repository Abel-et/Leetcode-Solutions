from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # putting the arr into a counter to know the frequency of each element in the arr
        container = Counter(nums)

        # Travers through each container elements and check if the value == 1 element
        for num in container:
            if container[num] == 1:
                return num
        