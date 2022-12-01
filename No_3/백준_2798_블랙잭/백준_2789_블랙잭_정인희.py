from itertools import combinations
n,m=map(int,input().split())

cards=list(map(int,input().split()))

global answer
answer=0
combi=combinations(cards,3)
for c in combi:
    sum_card=sum(c)
    if sum_card<=m:
        answer=max(answer,sum_card)
print(answer)



