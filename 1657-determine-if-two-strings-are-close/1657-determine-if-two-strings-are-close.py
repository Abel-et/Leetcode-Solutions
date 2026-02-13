from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        count_word1 = Counter(word1)
        count_word2 = Counter(word2)

        if count_word1.keys() != count_word2.keys():
            return False
        return sorted(count_word1.values()) == sorted(count_word2.values()) 
       