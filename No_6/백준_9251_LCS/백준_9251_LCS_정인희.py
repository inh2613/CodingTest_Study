a=input()
b=input()

len_a=len(a)
len_b=len(b)

#dp=[0]*max(len_a,len_b)
dp=[[0]*(len_a+1) for _ in range(len_b+1)]
# for i in range(len_a):
#     _max=0
#     for j in range(len_b):
#         if _max<dp[j]:
#             _max=dp[j]
#             #print('1',_max)
#         elif a[i]==b[j]:
#             dp[j]=_max+1
#     print(dp)

for i in range(1,len_b+1):
    for j in range(1,len_a+1):
        if b[i-1]==a[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
_max=0
for i in range(len_b+1):
    _max=max(_max,max(dp[i]))
print(_max)
