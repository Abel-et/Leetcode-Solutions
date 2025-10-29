# LeetCode Problem: 2024. Maximize the Confusion of an Exam .
# Problem Link:https://leetcode.com/problems/contains-duplicate-ii/?envType=problem-list-v2&envId=sliding-windowhttps://leetcode.com/problems/contains-duplicate-ii/?envType=problem-list-v2&envId=sliding-window
# Difficulty: Medium

def maxConscutiveAnswer(ansewerKey , k):
    def maxConscuative(targe):
        left = count = length = 0
        for right in range(len(ansewerKey)):
            if ansewerKey[right] != targe:
                count +=1
            while count > k :
                if ansewerKey[left] != targe:
                    count -=1
                left += 1
            length = max(length, right - left + 1)
        return length
    return max(maxConscuative('T'),maxConscuative('F'))
