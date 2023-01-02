# 알고리즘 수업 - 피보나치 수 1

n = int(input())
cnt_recursion = 0
cnt_dp = 0


def fibo(n):
    global cnt_recursion

    if n == 1 or n == 2:
        cnt_recursion += 1
        return 1
    return fibo(n-1) + fibo(n-2)


def fibo_dp(n):
    global cnt_dp
    d = [0] * (n+1)
    d[1] = 1
    d[2] = 1
    for i in range(3, n+1):
        cnt_dp += 1
        d[i] = d[i-1] + d[i-2]

fibo(n)
fibo_dp(n)
print(cnt_recursion, cnt_dp)
