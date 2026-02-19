class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = 0  
        yx = 0 
    
        for a, b in zip(s1, s2):
            if a == 'x' and b == 'y':
                xy += 1
            elif a == 'y' and b == 'x':
                yx += 1
        
        # If total mismatches is odd, impossible
        if (xy + yx) % 2 != 0:
            return -1
        
        # Each pair of same mismatches takes 1 swap
        swaps = xy // 2 + yx // 2
        
        # If there's one leftover of each, it takes 2 swaps
        swaps += xy % 2 * 2
        
        return swaps
            