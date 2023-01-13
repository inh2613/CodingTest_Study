# n=int(input())
#
# num=list(map(int,input().split()))
#
# dp=[-1001]
# def _sum(num):
#
#     dp[0]=num[0]
#
#     for i in range(1,len(num)):
#
#         dp.append(dp[i-1]+num[i])
#
#         if dp[i]<dp[i-1]:
#             dp[i]=dp[i]-num[i]
#
n = int(input())
data = list(map(int, input().split()))

for i in range(1, n):
    data[i] = max(data[i], data[i] + data[i - 1])

print(max(data))