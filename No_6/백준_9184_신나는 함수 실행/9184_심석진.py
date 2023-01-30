import sys
input = sys.stdin.readline

ans = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
for i in range(21):
    for j in range(21):
        for k in range(21):
            if i <= 0 or j <= 0 or k <= 0: ans[i][j][k] = 1
            elif i < j < k: ans[i][j][k] = ans[i][j][k-1] + ans[i][j-1][k-1] - ans[i][j-1][k]
            else: ans[i][j][k] = ans[i-1][j][k] + ans[i-1][j-1][k] + ans[i-1][j][k-1] - ans[i-1][j-1][k-1]

while True:
    a,b,c = list(map(int, input().split()))
    if a == -1 and b == -1 and c == -1: break
    print('w(' + str(a) + ', ' + str(b) + ', ' + str(c) + ') = ', end='')

    if a <= 0 or b <= 0 or c <= 0: print(ans[0][0][0])
    elif a > 20 or b > 20 or c > 20: print(ans[20][20][20])
    else: print(ans[a][b][c])