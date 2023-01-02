n=int(input())

cnt1=0
# cnt2=0

f=[0]*n
def fib(n):
    global cnt1
    if n==1 or n==2:
        cnt1 += 1
        return 1
    else:
        n=fib(n-1)+fib(n-2)
        return cnt1

def fibonacci(n):
    #global cnt2
    cnt2=0
    f[0]=f[1]=1

    for i in range(2,n):
        cnt2+=1

        f[i]=f[i-1]+f[i-2]

    return cnt2


# print(fib(n))
# print(fibonacci(n))

print(fib(n),fibonacci(n))