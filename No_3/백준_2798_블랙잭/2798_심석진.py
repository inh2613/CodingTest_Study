import sys

N, M = list(map(int, sys.stdin.readline().split()))
num = list(map(int, sys.stdin.readline().split()))

ans = 0

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1, N):
            tmp = num[i] + num[j] + num[k]
            if tmp <= M and tmp > ans: ans = tmp

print(ans)