import sys

n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
ans = [seq[0]]

for i in range(1, n):
    num = seq[i] + ans[i-1]
    if num < seq[i]: ans.append(seq[i])
    else: ans.append(num)

print(max(ans))