import sys

N,M = list(map(int, sys.stdin.readline().split()))
Nlist = set()
ans = 0
anslist = []

for _ in range(N):
    Nlist.add(sys.stdin.readline().rstrip())

for _ in range(M):
    m = sys.stdin.readline().rstrip()
    if m in Nlist:
        ans += 1
        anslist.append(m)


anslist.sort()
print(ans)
for s in anslist: print(s)