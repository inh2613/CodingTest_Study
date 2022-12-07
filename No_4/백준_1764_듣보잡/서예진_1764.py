# 듣보잡
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
people = {}
for _ in range(n):
    people[input().rstrip()] = False

l = []
cnt = 0
for _ in range(m):
    no_see = input().rstrip()
    if no_see in people:
        people[no_see] = True
        l.append(no_see)
        cnt += 1

print(cnt)
l.sort()
for name in l:
    print(name)