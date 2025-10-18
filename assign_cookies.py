# LeetCode Problem: Assign Cookies
# Problem Link: https://leetcode.com/problems/assign-cookies/
# Difficulty: Easy

def assignCookes(g,s):
    i =0# pointer of childern
    j = 0# pointer of cookie
    content = 0
    g.sort()
    s.sort()
    while i < len(g) and j< len(s):
        if s[j] >= g[i]:
            # if cookie j satified child i
            content+=1
            i+=1# move to next child
            #always j move to the next cookie
        j+=1
    return content


