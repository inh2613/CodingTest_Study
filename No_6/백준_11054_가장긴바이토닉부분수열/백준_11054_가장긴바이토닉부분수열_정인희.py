n=int(input())

a=list(map(int,input().split()))

dp_up=[1]*(n)
dp_down=[1]*(n)
dp=[0]*(n)

for i in range(1,n):
    for j in range(i):
        if a[i]>a[j]:
            dp_up[i]=max(dp_up[i],dp_up[j]+1)


for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):

        if a[i]>a[j]:
            dp_down[i]=max(dp_down[i],dp_down[j]+1)


# print(dp_up)
# print(dp_down)

for i in range(n):
    dp[i]=dp_up[i]+dp_down[i]-1
# print(dp)

print(max(dp))

