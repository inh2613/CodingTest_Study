# 연속합
n = int(input())
ar = list(map(int, input().split()))

for i in range(1, n):
    ar[i] = max(ar[i-1] + ar[i], ar[i])

print(max(ar))
