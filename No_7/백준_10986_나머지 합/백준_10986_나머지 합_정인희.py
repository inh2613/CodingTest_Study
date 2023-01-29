n,m=map(int,input().split())

arr=list(map(int,input().split()))
remainder=[arr[0]%m]
C=[0]*m # 같은 나머지의 인덱스를 카운트하는 리스트
answer=0

for i in range(1,n):
    arr[i]+=arr[i-1]
    remainder.append(arr[i]%m)
# 시간초과
# for i in range(n):
#     for j in range(i):
#         if abs(remainder[i]-remainder[j])==0:
#             # print('i j', i, j)
#             answer+=1
#     if remainder[i]==0:
#         answer+=1
print(remainder)
for r in remainder:
    if r==0:
        answer+=1
    C[r]+=1

for i in range(m):
    if C[i]>1:
        answer+=(C[i]*(C[i]-1))//2

print(answer)


