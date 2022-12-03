n=int(input())

num1=set(map(int,input().split()))

m=int(input())

num2=list(map(int,input().split()))

result=[]

for n2 in num2:
    if n2 in num1:
        result.append(1)
    else:
        result.append(0)

print(*result)