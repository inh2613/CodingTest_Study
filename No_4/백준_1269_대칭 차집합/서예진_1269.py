# 대칭 차집합
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

res = A.symmetric_difference(B)
print(len(res))