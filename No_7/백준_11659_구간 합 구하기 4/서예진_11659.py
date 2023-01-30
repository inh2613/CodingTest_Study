# 구간 합 구하기 4
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
prefix_sum = [0]

sum_value = 0
for i in range(n):
    sum_value += num[i]
    prefix_sum.append(sum_value)

for _ in range(m):
    start, end = map(int, input().split())
    print(prefix_sum[end] - prefix_sum[start-1])
