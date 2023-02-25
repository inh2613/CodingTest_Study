import sys
N = int(sys.stdin.readline())
ans = [[0 for _ in range(10)] for _ in range(N)]
ans[0] = [0,1,1,1,1,1,1,1,1,1]

for i in range(1,N):
    for j in range(10):
        if j == 0: ans[i][j] = ans[i-1][1]
        elif j == 9: ans[i][j] = ans[i-1][8]
        else: ans[i][j] = ans[i-1][j-1] + ans[i-1][j+1]

print(sum(ans[N-1])%1000000000)