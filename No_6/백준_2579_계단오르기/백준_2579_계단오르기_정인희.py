n=int(input())
stairs=[0]
dp=[[0]*(2) for _ in range(n+1)]
#dp[i][0]: i번째 계단 올라가는데 직전에 한개 계단 올라온 경우
#dp[i][1]: i번째 계단 올라가는데 직전에 두개 계단 올라온 경우
for i in range(n):
    stairs.append(int(input()))
# print(stairs)

if n==1:
    print(max(stairs))
elif n==2:
    print(sum(stairs))
elif n==3:
    print(max(stairs[-1]+stairs[-2],stairs[-1]+stairs[-3]))

else:
    for i in range(1,n+1):
        if i==1:
            dp[i][0]=stairs[1]
            dp[i][1]=stairs[1]
            continue
        dp[i][0]=stairs[i]+dp[i-1][1]
        dp[i][1]=stairs[i]+max(dp[i-2][0],dp[i-2][1])


    print(max(dp[n]))