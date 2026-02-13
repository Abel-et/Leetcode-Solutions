class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        if len(nums) == len(set(nums)):
            return 0

        n = len(nums)
        count = 0

        for i in range(n-1):
            for j in range(i+1,n):
                index = j*i
                if nums[i] == nums[j] and index%k == 0 :
                    count +=1
        return count
        