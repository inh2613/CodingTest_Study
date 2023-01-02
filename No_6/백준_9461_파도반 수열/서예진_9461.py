# 파도반 수열
t = int(input())
d = [0] * 101
d[1] = d[2] = d[3] = 1
d[4] = d[5] = 2
for _ in range(t):
    n = int(input())
    if d[n] > 0:
        print(d[n])
        continue
    else:
        for i in range(6, n+1):
            d[i] = d[i-1] + d[i-5]
        print(d[n])

