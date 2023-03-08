# 인간-컴퓨터 상호작용
import sys
input = sys.stdin.readline

s = input()
q = int(input())
d = {}
l = len(s)
for i in range(26):
    c = ord('a') + i
    d[chr(c)] = [0]
    cnt = 0
    for j in range(l):
        if s[j] == chr(c):
            cnt += 1
        d[chr(c)].append(cnt)

for _ in range(q):
    ch, left, right = input().split()
    left = int(left)
    right = int(right)
    print(d[ch][right+1] - d[ch][left])
