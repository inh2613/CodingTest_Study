# 문자열 집합
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = set()

for _ in range(n):
    s.add(input())

total = 0
for _ in range(m):
    check_str = input()
    if check_str in s:
        total += 1

print(total)