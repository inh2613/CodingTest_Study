# 스택
import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    oper = list(input().split())
    what = oper[0]
    if what == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif what == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif what == 'size':
        print(len(stack))
    elif what == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        stack.append(oper[1])

