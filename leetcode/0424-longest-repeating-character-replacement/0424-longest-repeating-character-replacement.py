from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_freq ,res,left = 0,0,0

        for i in range(len(s)):
            count[s[i]] +=1
            max_freq = max(max_freq, count[s[i]])
            print(*count,"in if ")

            while ((i - left + 1) - max_freq) > k:
                count[s[left]] -=1
                left +=1
            res = max(res, i - left+1)
        return res