# N과 M(4)
n, m = map(int, input().split())
ar = []


def BT():
    if len(ar) == m:
        print(' '.join(map(str, ar)))
        return

    for i in range(1, n+1):
        if len(ar) > 0 and i < ar[-1]:
            continue
        ar.append(i)
        BT()
        ar.pop()


BT()