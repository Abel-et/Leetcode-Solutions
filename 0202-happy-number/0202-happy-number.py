class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()

        # check if n is not in the set and n not equal to 1
        while n != 1 and n not in s:
            s.add(n)
            n = sum((int(i) ** 2 for i in str(n)))
        return n == 1 