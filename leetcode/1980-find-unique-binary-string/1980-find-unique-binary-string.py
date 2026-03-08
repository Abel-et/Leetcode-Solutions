from collections import  defaultdict
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        counter = defaultdict(int)
        n = len(nums)
        for i in nums:
            int_rep = int(i,2)
            counter[int_rep] = i
        max_value = pow(2,n)

        for i in range(max_value):
            if i not in counter:

                return f'{i:0{str(n)}b}'
        