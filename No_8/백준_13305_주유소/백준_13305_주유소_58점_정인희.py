n=int(input())

distance=list(map(int,input().split()))
price=list(map(int,input().split()))

answer=0
# answer=float(answer)
_min_price = min(price[:-1])
last=n-1

while True:
    start = price.index(_min_price)

    total_distance=sum(distance[start:last])

    answer+=total_distance*price[start]

    # print(answer)

    if start==0:
        break
    price=price[0:start]
    last=start
    _min_price=min(price)



print(answer)







