import sys

N = int(sys.stdin.readline())
num = [0 for _ in range(N+1)]

for i in range(2, N+1):
    num[i] = num[i-1] + 1

    if i%3 == 0: num[i] = min(num[i], num[i//3]+1)
    if i%2 == 0: num[i] = min(num[i], num[i//2]+1)


    '''
    div3cnt = 0
    div2cnt = 0
    subcnt = 0

    if i%3 == 0:
        div3cnt += 1
        div3cnt += num[(i//3)]
        num[i] = div3cnt

    if i%2 == 0:
        div2cnt += 1
        div2cnt += num[(i//2)]
        if num[i] != 0: num[i] = min(num[i], div2cnt)
        else: num[i] = div2cnt

    if i > 1:
        subcnt += 1
        subcnt += num[i-1]
        if num[i] != 0: num[i] = min(num[i], subcnt)
        else: num[i] = subcnt
        '''


print(num[N])