import sys

N = sys.stdin.readline()

for i in range(int(N)):
    ans = i
    for j in str(i):
        ans += + int(j)
    if ans == int(N):
        print(i)
        break

if i == int(N)-1: print(0)