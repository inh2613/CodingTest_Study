n=int(input())

dp=[[0]*2 for _ in range(n+1)]

wine=[0]*(n+1)
for i in range(1,n+1):
    wine[i]=int(input())

for i in range(1,n+1):
    if i==1:
        dp[i][0]=wine[i]
        dp[i][1]=wine[i]
    elif i==2:
        dp[i][0] = dp[i - 1][1] + wine[i]
        dp[i][1]=wine[i]
    else:
        dp[i][0]=dp[i-1][1]+wine[i]
        _max=0
        for j in range(i-1):
            _max=max(_max,max(dp[j]))
        dp[i][1]=_max+wine[i]
result=0
for i in range(1,n+1):
    _max=max(dp[i])
    result=max(result,_max)

print(result)
# print(dp)