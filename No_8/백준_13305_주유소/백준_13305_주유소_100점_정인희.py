n=int(input())

distance=list(map(int,input().split()))
price=list(map(int,input().split()))

answer=0
cur_min=1e9
for i in range(n-1):

    cur_min=min(cur_min,price[i])

    answer+=distance[i]*cur_min



print(answer)







