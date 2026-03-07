class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        
        # Target alternating strings for the doubled string
        target1 = "01" * n
        target2 = "10" * n
        
        # Count flips for first window of size n
        flips1 = 0
        flips2 = 0
        for i in range(n):
            if s[i] != target1[i]:
                flips1 += 1
            if s[i] != target2[i]:
                flips2 += 1
                
        min_flips = min(flips1, flips2)
        
        # Slide the window
        for i in range(n, 2 * n):
            # Remove character leaving the window
            if s[i - n] != target1[i - n]:
                flips1 -= 1
            if s[i - n] != target2[i - n]:
                flips2 -= 1
                
            # Add character entering the window
            if s[i] != target1[i]:
                flips1 += 1
            if s[i] != target2[i]:
                flips2 += 1
                
            min_flips = min(min_flips, flips1, flips2)
            
        return min_flips