
# LeetCode Problem: length Of Longest Substring
# Problem Link:https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Difficulty: medium
def lengthOfLongestSubstring(self, s):
    l = 0
    longest = 0
    unique = set()
    n = len(s)
    for i in range(n):
        while s[i] in unique:
            unique.remove(s[l])
            l+=1
        window = (i-l)+1
        longest = max(longest,window)
        unique.add(s[i])
    return longest