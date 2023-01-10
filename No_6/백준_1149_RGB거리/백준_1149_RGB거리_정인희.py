n=int(input())

dp=[]

r=[0]*(n+1)
g=[0]*(n+1)
b=[0]*(n+1)

for _ in range(n):
    dp.append(list(map(int,input().split())))

for i in range(1,n+1):
    r[i]=min(g[i-1],b[i-1])+dp[i-1][0]
    g[i]=min(r[i-1],b[i-1])+dp[i-1][1]
    b[i]=min(r[i-1],g[i-1])+dp[i-1][2]

print(min(r[n],g[n],b[n]))
