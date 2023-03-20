# 덱

from collections import deque
import sys
input = sys.stdin.readline


def check_empty():
    if len(d) == 0:
        return True
    else:
        return False


n = int(input())
d = deque()
for _ in range(n):
    funcs = list(input().split())
    func = funcs[0]
    if func == 'pop_front':
        if check_empty():
            print(-1)
        else:
            print(d.popleft())
    elif func == 'pop_back':
        if check_empty():
            print(-1)
        else:
            print(d.pop())
    elif func == 'size':
        print(len(d))
    elif func == 'empty':
        if check_empty():
            print(1)
        else:
            print(0)
    elif func == 'front':
        if check_empty():
            print(-1)
        else:
            print(d[0])
    elif func == 'back':
        if check_empty():
            print(-1)
        else:
            print(d[-1])
    elif func == 'push_front':
        num = funcs[1]
        d.appendleft(num)
    elif func == 'push_back':
        num = funcs[1]
        d.append(num)