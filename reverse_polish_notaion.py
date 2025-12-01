# LeetCode Problem:150. Evaluate Reverse Polish Notation
# Problem Link:https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
# Difficulty: Medium
stack = []
for i in tokens:
    if i.lstrip('-').isdigit():
        stack.append(int(i))
    elif i == "+":
        add = stack.pop() + stack.pop()
        stack.append(add)
    elif i == "*":
        mul =stack.pop() * stack.pop()
        stack.append(mul)
    elif i == "/":
        div = int(stack[-2] / stack[-1])
        stack.pop()
        stack.pop()
        stack.append(div)
    elif i =='-':
        sub = stack[-2] - stack[-1]
        stack.pop()
        stack.pop()
        stack.append(sub)
print(stack)
print(stack[-1])