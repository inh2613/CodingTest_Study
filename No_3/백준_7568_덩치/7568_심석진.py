import sys

N = int(sys.stdin.readline())
x,y = list(map(int, sys.stdin.readline().split()))
person = [[x,y]]
ans = [1]
for i in range(1, N):
    x,y = list(map(int, sys.stdin.readline().split()))
    rank = 1
    for j in range(0,i):
        if x < person[j][0] and y < person[j][1]: rank += 1
        elif x > person[j][0] and y > person[j][1]: ans[j] += 1

    ans.append(rank)
    person.append([x,y])

for i in range(len(ans)): print(ans[i], end=' ')