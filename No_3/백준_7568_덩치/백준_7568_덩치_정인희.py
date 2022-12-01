
n=int(input())

l=[]

for _ in range(n):
    x,y=map(int,input().split())
    l.append((x,y))

rank=[]

for i in range(n):
    count=0
    for j in range(n):
        if l[i][0]<l[j][0] and l[i][1]<l[j][1]:
            count+=1
    rank.append(count+1)

print(*rank)