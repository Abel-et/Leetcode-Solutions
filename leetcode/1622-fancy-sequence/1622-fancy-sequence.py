class Fancy:
    def __init__(self):
        self.nums = []
        self.mul = 1
        self.add = 0
        self.MOD = 10**9 + 7

    def append(self, val: int) -> None:
        # We store the value such that: (stored_val * current_mul + current_add) == val
        # So: stored_val = (val - current_add) * inv(current_mul)
        # pow(a, -1, mod) is available in Python 3.8+ for modular inverse
        inv_mul = pow(self.mul, -1, self.MOD)
        self.nums.append(((val - self.add) * inv_mul) % self.MOD)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.nums):
            return -1
        # Apply the current global transformation to the stored 'neutral' value
        return (self.nums[idx] * self.mul + self.add) % self.MOD