import sys
N = int(sys.stdin.readline())

ans = [1,2]
for i in range(2, N): ans.append((ans[i-2] + ans[i-1])%15746)

print(ans[N-1])