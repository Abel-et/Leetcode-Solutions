class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        result = 0
        
        for i in range(1, n + 1):
            # i.bit_length() tells us how many positions to shift
            length = i.bit_length()

            result = ((result << length) + i) % MOD
            
        return result