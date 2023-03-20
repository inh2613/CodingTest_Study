# 큐 2
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()
for _ in range(n):
    oper = list(input().split())
    o = oper[0]
    if o == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif o == 'size':
        print(len(q))
    elif o == 'empty':
        if len(q) == 0:
            print('1')
        else:
            print('0')
    elif o == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif o == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
    else:
        num = oper[1]
        q.append(num)

