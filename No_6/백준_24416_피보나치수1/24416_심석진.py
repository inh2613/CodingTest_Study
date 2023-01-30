import sys

def rec_fib(n):
    global recN
    if n == 1 or n == 2:
        recN += 1
        return 1
    else: return rec_fib(n-2) + rec_fib(n-1)


def DP_fib(n):
    global DPN
    arr[0] = arr[1] = 1
    for i in range(2,n):
        arr[i] = arr[i-2] + arr[i-1]
        DPN += 1


N = int(sys.stdin.readline())
arr = [0 for _ in range(N)]
recN = 0    # 마지막 값이 정답임.. 세상에!
DPN = 0
rec_fib(N)
DP_fib(N)
print(recN, DPN, end=' ')