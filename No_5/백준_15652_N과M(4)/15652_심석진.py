import sys

N,M = list(map(int, sys.stdin.readline().split()))
ans = []


def bt(n):
    if len(ans) == M:
        print(*ans)
        return

    for i in range(n, N+1):
        ans.append(i)
        bt(i)
        ans.pop()

bt(1)