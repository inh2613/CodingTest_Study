n=int(input())

dp=[[0]*(10) for _ in range(n+1)]

# 이런 표를 통해 점화식을 세울 수 있음
# 맨 뒷자리 숫자: 0 1 2 3 4 5 6 7 8 9
# 자리수=1(n=1): 0 1 1 1 1 1 1 1 1 1
# 자리수=2(n=2): 1 1 2 2 2 2 2 2 2 2

for i in range(10):
    if i==0:
        dp[1][i]=0
    else:
        dp[1][i]=1

for i in range(2,n+1):
    for j in range(10):
        if j==0:
            dp[i][j]=dp[i-1][1]
        elif j==9:
            dp[i][j]=dp[i-1][8]
        else:
            dp[i][j]=dp[i-1][j-1]+dp[i-1][j+1]


print(sum(dp[n])%1000000000)
