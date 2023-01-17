import sys

N,M = list(map(int, sys.stdin.readline().split()))
ans = []

def bt():
    if len(ans) == M:
        print(*ans)
        return

    for i in range(1, N+1):
        if i in ans: continue
        ans.append(i)
        bt()
        ans.pop()

bt()