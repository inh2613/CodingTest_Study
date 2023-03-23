# 회전하는 큐
from collections import deque

n, m = map(int, input().split())
num = list(map(int, input().split()))
q = deque([i for i in range(1, n+1)])

cnt = 0
for pick in num:
    while True:
        if pick == q[0]:
            q.popleft()
            break
        else:
            if q.index(pick) <= len(q) // 2:
                while q[0] != pick:
                    q.append(q.popleft())
                    cnt += 1
            else:
                while q[0] != pick:
                    q.appendleft(q.pop())
                    cnt += 1

print(cnt)
