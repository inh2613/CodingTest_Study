n,m=map(int,input().split())

arr=list(map(int,input().split()))
_sum=[0]*(n)
for i in range(len(arr)):
    if i==0:
        _sum[i]=arr[i]
    else:
        _sum[i]=_sum[i-1]+arr[i]
# print(_sum)
for _ in range(m):
    i,j=map(int,input().split())
    if i==1:
        print(_sum[j-1])
    else:
        print(_sum[j-1]-_sum[i-2])