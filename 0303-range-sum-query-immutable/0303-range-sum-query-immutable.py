class NumArray:

    def __init__(self, nums: List[int]):
        self.nums  = nums
        self.prefix = []
        self.start = 0
        for i in range(len(nums)):
            self.start += nums[i]
            self.prefix.append(self.start)
        print(self.prefix)

    def sumRange(self, left: int, right: int) -> int:
        if left ==0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left-1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)