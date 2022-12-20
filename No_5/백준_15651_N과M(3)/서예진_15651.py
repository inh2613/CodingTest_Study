# N과 M(3)
n, m = map(int, input().split())
ar = []

def BT():
    if len(ar) == m:
        print(' '.join(map(str, ar)))
        return
    for i in range(1, n+1):
        ar.append(i)
        BT()
        ar.pop()


BT()