n,k=map(int,input().split())

arr=list(map(int,input().split()))

arr_k=[]

arr_k.append(sum(arr[:k]))
for i in range(n-k):
    arr_k.append(arr_k[i]+arr[i+k]-arr[i])
#print(arr_k)
print(max(arr_k))
