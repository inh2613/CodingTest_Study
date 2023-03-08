# 구간 합 구하기 5
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = []
for _ in range(n):
    num.append(list(map(int, input().split())))

prefix_sum = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] + num[i-1][j-1] - prefix_sum[i-1][j-1]

# 당연히 ~ 시간 초과!
'''
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    total = 0
    for x in range(x1-1, x2):
        total += prefix_sum[x][y2] - prefix_sum[x][y1-1]
    print(total)
'''
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(prefix_sum[x2][y2] - prefix_sum[x2][y1-1] - prefix_sum[x1-1][y2] + prefix_sum[x1-1][y1-1])