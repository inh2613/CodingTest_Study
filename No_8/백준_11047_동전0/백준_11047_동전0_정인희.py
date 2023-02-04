n,k=map(int,input().split())
values=[]

for i in range(n):
    value=int(input())
    values.append(value)
values=sorted(values,reverse=True)

result=0


for value in values:
    if k>=value:
        while k>0:
            k-=value
            result+=1
            if k<0:
                k+=value
                result-=1
                break
    else:
        pass

print(result)
