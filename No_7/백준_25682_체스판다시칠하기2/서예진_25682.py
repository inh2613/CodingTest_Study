# 체스판 다시 칠하기 2
import sys
input = sys.stdin.readline


def solution(start):
    row_num = [0] * (n+1)
    col_num = [0] * (m+1)
    res = 1e9
    s = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if ((i+j) % 2 == 1 and chess[i-1][j-1] == start) or ((i+j) % 2 == 0 and chess[i-1][j-1] != start):
                row_num[i] += 1
                col_num[j] += 1
                s[i][j] = 1
            s[i][j] = s[i-1][j-1] + row_num[i] + col_num[j] - s[i][j]

    for i in range(k, n+1):
        for j in range(k, m+1):
            temp = s[i][j] - s[i-k][j] - s[i][j-k] + s[i-k][j-k]
            res = min(res, temp)
    return res


n, m, k = map(int, input().split())
chess = []
for _ in range(n):
    chess.append(list(input().strip('\n')))

print(min(solution('B'), solution('W')))

