# 덩치

n = int(input())
ar = []
for _ in range(n):
    w, h = map(int, input().split())
    ar.append((w, h))

for i in range(n):
    cnt = 0
    for j in range(n):
        if i == j:
            continue
        if ar[i][0] < ar[j][0] and ar[i][1] < ar[j][1]:
            cnt += 1
    print(cnt+1, end=" ")