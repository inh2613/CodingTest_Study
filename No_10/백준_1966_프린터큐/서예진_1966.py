# 프린터 큐

from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    q = deque()
    for i in range(n):
        q.append((i, p[i]))

    cnt = 0
    check = True
    while check:
        priority = q[0][1]
        high = 0
        for i in range(len(q)):
            if priority < q[i][1]:
                q.append(q.popleft())
                break
            else:
                high += 1
        if len(q) == high:
            pop_idx, pop_p = q.popleft()
            cnt += 1
            if pop_idx == m:
                check = False
        if len(q) == 0:
            break
    print(cnt)
