n=int(input())
dp=[]
left=[0]*(n+1)
right=[0]*(n+1)

for i in range(n):
    dp.append(list(map(int,input().split())))

# left[0]=dp[0][0]
# right[0]=dp[0][0]

for i in range(1,n):
    for j in range(i+1):
        if j==0:
            dp[i][j]=dp[i][j]+dp[i-1][j]
        elif i==j:
            dp[i][j]=dp[i][j]+dp[i-1][j-1]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-1])+dp[i][j]

print(max(dp[n-1]))