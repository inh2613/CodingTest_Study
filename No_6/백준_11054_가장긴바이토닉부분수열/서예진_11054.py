# 가장 긴 바이토닉 부분 수열
n = int(input())
num_list = list(map(int, input().split()))

up = [1] * n
down = [1] * n
dp = [0] * n

for i in range(1, n):
    for j in range(i - 1, -1, -1):
        if num_list[i] > num_list[j]:
            up[i] = max(up[i], up[j] + 1)

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if num_list[i] > num_list[j]:
            down[i] = max(down[i], down[j]+1)

for i in range(n):
    dp[i] = up[i] + down[i] - 1

print(max(dp))