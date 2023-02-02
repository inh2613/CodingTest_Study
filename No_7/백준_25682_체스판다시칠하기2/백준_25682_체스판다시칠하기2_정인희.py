n,m,k=map(int,input().split())

board=[]

for _ in range(n):
    board.append(list(input()))
dp=[[0]*(m+1) for _ in range(n+1)]

answer=1e9
def solve(color):
    global answer
    for i in range(n):
        for j in range(m):
            if (i+j)%2==0:
                if board[i][j]!=color:
                    dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j] - dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j] - dp[i][j]
            else:
                if board[i][j]==color:
                    dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j] - dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j] - dp[i][j]
    # print(dp)
# 이 부분이 조금 어렵다...
    for i in range(1,n-k+2):
        for j in range(1,m-k+2):
            count=dp[i+k-1][j+k-1]-dp[i-1][j+k-1]-dp[i+k-1][j-1]+dp[i-1][j-1]
            answer=min(count,answer)


solve('B')
solve('W')

print(answer)