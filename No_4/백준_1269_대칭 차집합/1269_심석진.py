import sys

N,M = list(map(int, sys.stdin.readline().split()))
A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))

A_B = A - B
B_A = B - A

print(len(A_B) + len(B_A))