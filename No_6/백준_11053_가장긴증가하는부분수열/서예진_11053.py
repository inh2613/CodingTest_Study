# 가장 긴 증가하는 부분 수열
n = int(input())
num_list = list(map(int, input().split()))

d = [0] * n
d[0] = 1
for i in range(1, n):
    if num_list[i] > num_list[i-1]:
        d[i] = d[i-1] + 1
    else:
        d[i] = 1
    for j in range(i - 1, -1, -1):
        if num_list[j] < num_list[i]:
            d[i] = max(d[i], d[j] + 1)

print(max(d))
