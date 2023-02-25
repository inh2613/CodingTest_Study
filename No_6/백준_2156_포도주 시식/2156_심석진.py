import sys
n = int(sys.stdin.readline())
wine = []
for _ in range(n): wine.append(int(sys.stdin.readline()))

if n < 3: print(sum(wine))
else:
    ans = [0] * n
    ans[0] = wine[0]
    ans[1] = wine[1] + wine[0]
    ans[2] = max(wine[2] + wine[1], wine[2] + wine[0], ans[1])

    for i in range(3,n):
        ans[i] = max(wine[i] + ans[i-2], wine[i] + wine[i-1] + ans[i-3], ans[i-1]) # 포도주를 2번 연속으로 안먹을 경우도 고려해야 함

    print(ans)
    print(max(ans))