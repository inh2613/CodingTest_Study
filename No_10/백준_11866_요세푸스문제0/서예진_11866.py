# 요세푸스 문제 0
from collections import deque
N, K = map(int, input().split())
cq = deque()
num_q = N

for _ in range(N):
    cq.append(True)

s = '<'
pointer = 0
k_cnt = 0
while num_q > 0:

    if cq[pointer]:
        k_cnt += 1

    if k_cnt == K:
        cq[pointer] = False
        num_q -= 1
        s += str(pointer+1)
        s += ', '
        k_cnt = 0

    pointer += 1

    if pointer == N:
        pointer = 0

s = s[:-2]
s += '>'
print(s)
