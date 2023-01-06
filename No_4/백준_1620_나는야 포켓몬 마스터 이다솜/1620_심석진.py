import sys

N, M = list(map(int, sys.stdin.readline().split()))
poket = {}
poket_value_key = {}

for i in range(N):
    name = sys.stdin.readline().rstrip()
    poket[i] = name
    poket_value_key[name] = i

for _ in range(M):
    q = sys.stdin.readline().rstrip()
    if q[0] in ['1','2','3','4','5','6','7','8','9']:
        print(poket[int(q)-1])

    else:
        print(poket_value_key[q]+1)