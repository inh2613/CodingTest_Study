x=int(input())

dp=[0]*(x+1)

if x==2 or x==3:
    print(1)
elif x==1:
    print(0)
else:
    dp[1], dp[2], dp[3] = 1, 1, 1
    for i in range(4,x+1):
        if i%3==0 and i%2==0:
            dp[i]=min(dp[i//3],dp[i//2],dp[i-1])+1
        elif i%3==0:
            dp[i]=min(dp[i//3],dp[i-1])+1
        elif i%2==0:
            dp[i]=min(dp[i//2],dp[i-1])+1
        else:
            dp[i]=dp[i-1]+1

    print(dp[x])

