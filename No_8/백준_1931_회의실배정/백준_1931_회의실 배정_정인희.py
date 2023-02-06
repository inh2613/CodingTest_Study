n=int(input())

l=[]
for _ in range(n):
    start,end=map(int,input().split())
    l.append((start,end))

l.sort(key=lambda x:(x[1],x[0]))

answer=1

i=0
while True:
    for j in range(i+1,n):
        if l[i][1]<=l[j][0]:
            answer+=1
            # print(i,j)
            break
    i=j
    if i==n-1:
        break
print(answer)