n,m=map(int,input().split())

s_1=[]
s_2=[]

for i in range(n):
    s_1.append(input())

for i in range(m):
    s_2.append(input())

s_1=set(s_1)


cnt=0

for s in s_2:
    if s in s_1:
        cnt+=1

print(cnt)
