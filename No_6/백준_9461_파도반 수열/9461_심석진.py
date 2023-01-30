import sys

T = int(sys.stdin.readline())
P = [0 for _ in range(100)]
P[0] = P[1] = P[2] = 1
for i in range(3,100): P[i] = P[i-3] + P[i-2]

for _ in range(T):
    N = int(sys.stdin.readline())
    print(P[N-1])