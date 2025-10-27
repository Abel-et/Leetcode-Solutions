# LeetCode Problem:max-consecutive-ones-iii
# Problem Link:https://leetcode.com/problems/max-consecutive-ones-iii/
# Difficulty: medium
zeros = 0
length = 0
n = len(nums)
left =0
for right in range(n):
    if nums[right] == 0:
        zeros += 1

    while zeros > k:
        if nums[left] == 0:
            zeros -= 1
        left +=1
    length = max(length,right - left+1)
    print(length)
print(length)