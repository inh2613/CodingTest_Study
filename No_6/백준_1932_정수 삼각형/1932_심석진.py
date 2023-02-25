import sys

n = int(sys.stdin.readline())
tri = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans = [[0 for _ in range(n)] for _ in range(n)]
ans[0][0] = tri[0][0]

for i in range(n-1):
    for j in range(0, i+1):
        ans[i+1][j] = max(ans[i+1][j], ans[i][j] + tri[i+1][j])
        ans[i+1][j+1] = max(ans[i+1][j+1], ans[i][j] + tri[i+1][j+1])

print(max(ans[n-1]))