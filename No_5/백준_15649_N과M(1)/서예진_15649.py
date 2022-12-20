# N과 M(1)
n, m = map(int, input().split())
ar = []
def backTracking():
    if len(ar) == m:
        # print('-------------------')
        print(' '.join(map(str, ar)))
        return

    for i in range(1, n+1):
        if i in ar:
            continue
        ar.append(i)
        # print('append', ar)
        backTracking()
        ar.pop()
        # print('pop', ar)


backTracking()

