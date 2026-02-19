class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for c in magazine:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        for c in ransomNote:
            if c not in count:
                return False
            elif count[c] == 1:
                del count[c]
            else:
                count[c] -=1
        return True
        