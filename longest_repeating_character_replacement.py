# LeetCode Problem: Longest Repeating Character Replacement
# Problem Link:https://leetcode.com/problems/longest-repeating-character-replacement/
# Difficulty: medium
def characterReplacement(self, s, k):
    count = defaultdict(int)
    left = 0 # staring point of the window
    maxC = 0 # maximum value of element in the dictionary
    maxL = 0 # maximum length of the window which hold longest repeating char

    for rigth in range(len(s)): # traversing each element of s
        count[s[rigth]] += 1 #  add on the char which is in s or for new char
        maxC = max(count[s[rigth]],maxC) # knowing the maximum repeated char

        if (right - left + 1) - maxC >k: # if the window minus max counted char greater k
            count[s[left]] -=1 # shrink the window size
            left+=1
        maxL = max(maxL, riht - left + 1)
    return maxL