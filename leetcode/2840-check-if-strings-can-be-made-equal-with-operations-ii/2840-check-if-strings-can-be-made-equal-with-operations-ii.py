class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # Compare sorted even-indexed characters
        evens_match = sorted(s1[0::2]) == sorted(s2[0::2])
       
        # Compare sorted odd-indexed characters
        odds_match = sorted(s1[1::2]) == sorted(s2[1::2])
       
        
        return evens_match and odds_match
