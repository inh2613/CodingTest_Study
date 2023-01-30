# 수열
n, k = map(int, input().split())
tmp = list(map(int, input().split()))
prefix_sum = [0]

sum_value = 0
for i in range(n):
    sum_value += tmp[i]
    prefix_sum.append(sum_value)

max_temp = -100 * n
for i in range(n-k+1):
    sub = prefix_sum[i + k] - prefix_sum[i]
    if sub > max_temp:
        max_temp = sub

print(max_temp)
