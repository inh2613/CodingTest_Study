# 괄호
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    stack = []
    s = input()
    for ch in s:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if len(stack) == 0:
                stack.append(ch)
                break
            else:
                stack.pop()
    if len(stack) > 0:
        print("NO")
    else:
        print("YES")