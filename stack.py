

# LeetCode Problem:682. Baseball Game
# Problem Link:https://leetcode.com/problems/baseball-game/description/
# Difficulty: Easy
stack = []
operation = 0
for i in ops:
    if i.lstrip('-').isdigit():
        stack.append(int(i))
    elif i =="C":
        stack.pop()
    elif i =="D":
        last = stack[-1]
        stack.append(last*2)
    elif i =="+":
        operation = stack[-1] + stack[-2]
        stack.append(operation)
    print(stack)
print(sum(stack))

