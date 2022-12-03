import math

def is_prime(num):
    check=[True]*(num+1)
    res=[]
    check[0],check[1]=False,False
    for i in range(2,int(math.sqrt(n))+1):
        if check[i]==True:
            res.append(i)
            j=2
            while i*j<=n:
                check[i*j]=False
                j+=1
    res=[x for x in range(n+1) if check[x]==True]
    return res

m,n=map(int,input().split())

res=is_prime((n))

for i in res:
    if i>=m:
        print(i)