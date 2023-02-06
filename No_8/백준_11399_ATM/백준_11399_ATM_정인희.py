from copy import deepcopy
n=int(input())

number=[]

number=list(map(int,input().split()))

number.sort()
sum=0
a=number.copy()

for i in range(1,n):
    number[i]+=number[i-1]
    sum+=number[i]

sum+=number[0]
print(sum)
