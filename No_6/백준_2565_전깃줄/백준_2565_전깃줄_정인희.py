n=int(input())

line=[]
dp=[1]*n
for _ in range(n):
    line.append(list(map(int,input().split())))
answer=0
line.sort(key=lambda x:(x[0]))
# print(line)
for i in range(n):
    for j in range(i):
        if line[i][1]>line[j][1]:
            dp[i]=max(dp[i],dp[j]+1)

# print(dp)
print(n-max(dp))