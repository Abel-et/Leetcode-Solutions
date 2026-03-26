
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        even = (n+1)//2
        odd = n//2

        first = pow(5 , even , mod)
        second = pow(4 , odd , mod)

        return (first*second) % mod