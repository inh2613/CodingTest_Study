

n=int(input())

arr=[]

if n==1:
    x=int(input())
    if x==0:
        print(0)
        exit()

for _ in range(n):
    x=int(input())

    if x!=0:
        arr.append(x)
    else:
        arr.pop()
print(sum(arr))