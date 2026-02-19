from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran = Counter(ransomNote)
        mag = Counter(magazine)

        for i in set(ransomNote):
            if ran[i] > mag.get(i, 0):
                return False
        else:
            return True
    
        