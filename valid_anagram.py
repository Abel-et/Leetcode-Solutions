# LeetCode valid anagram
# Problem Link:https://leetcode.com/problems/valid-anagram/
# Difficulty: easy
def isAnagram(self, s, t):
    d = {}
    if len(t) != len(s):
        return False
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for j in t:
        if j in d:
            if t.count(j) != d[j]:
                return False
        else:
            return False
    else:
        return True