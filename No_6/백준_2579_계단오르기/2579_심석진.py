import sys

n = int(sys.stdin.readline())
score = [int(sys.stdin.readline()) for _ in range(n)]
ans = [0 for _ in range(n)]

if n <= 2:
    print(sum(score))

else:
    ans[0] = score[0]
    ans[1] = max(score[1], score[0]+score[1])
    ans[2] = max(score[0]+score[2], score[1]+score[2])

    for i in range(3,n):
        ans[i] = max(ans[i-2]+score[i], ans[i-3]+score[i-1]+score[i])

    print(ans[-1])