from collections import Counter
class Solution:
    def findValidPair(self, s: str) -> str:
        # catching the elements with their frequency 
        digits = Counter(s)
       
        # checking if the num and it adject have a difference of one  and have same frequency
        for i in range(1,len(s)):
            num = int(s[i])
            if num == digits[str(num)]:
                next = int(s[i-1])
                if (next + 1) == num or (next - 1) == num:
                    if next == digits[str(next)]:
                        return f"{next}{num}" 
        else:
            return ""
