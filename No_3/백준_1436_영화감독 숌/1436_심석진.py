import sys

N = int(sys.stdin.readline())
cnt = 0
for n in range(666,100000000):
    if '666' in str(n): cnt += 1
    if cnt == N:
        print(n)
        break
