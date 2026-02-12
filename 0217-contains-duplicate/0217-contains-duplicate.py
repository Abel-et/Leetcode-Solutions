class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for i in nums:
            if i in unique:
                return True
            else:
                unique.add(i)
        else:
            return False