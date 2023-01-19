n,k=map(int,input().split())

bag=[]
#dp=[[0]*(k+1) for _ in range(n+1)]
dp=[[0]*(n+1) for _ in range(k+1)]
#dp[i][j] : 가방에 담은 물건의 무게 합이 i 일 때, 처음 j 개의 물건 중 담을 수 있는 최대 가치

# i: 배낭의 용량

for x in range(1,n+1):
    w,v=map(int,input().split())
    for i in range(1,k+1):
        if i<w: # 현재 물건을 담을 수 없다
            dp[i][x]=dp[i][x-1]
        else:
            dp[i][x]=max(dp[i][x-1],dp[i-w][x-1]+v)
# print(dp)
# for i in range(k+1):
#     print(dp[i])
print(dp[k][n])