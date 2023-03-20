# 카드2

from collections import deque
n = int(input())
q = deque([i for i in range(1, n+1)])

while len(q) > 1:
    q.popleft()
    if len(q) == 1:
        break
    top = q.popleft()
    q.append(top)

print(q[0])