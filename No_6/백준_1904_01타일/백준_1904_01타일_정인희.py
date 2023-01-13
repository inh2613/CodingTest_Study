n=int(input())
global dp
dp=[0]*1000001

# def re(i):
#     if i==0 or i==1:
#         return 1
#     elif dp[i]!=0:
#         return dp[i]
#     else:
#         dp[i]=(re(i-2)+re(i-1))%15746
#         return dp[i]
a, b = 0, 1
for i in range(n):
    a,b=b%15746,(a+b)%15746

print(b)

#https://blog.naver.com/occidere/220787441430



#print(re(n))
