import sys

N, M = list(map(int, sys.stdin.readline().split()))
S = set()
ans = 0

for _ in range(N):
    tmp = sys.stdin.readline().rstrip()
    S.add(tmp)

for _ in range(M):
    test = sys.stdin.readline().rstrip()
    if test in S: ans += 1

print(ans)