n=int(input())
card=list(map(int,input().split()))
card_s=dict()
for c in card:
    if c not in card_s.keys():
        card_s[c]=1
    else:
        card_s[c]+=1

m=int(input())

card_q=list(map(int,input().split()))

result=[]
for q in card_q:
    if q in card_s.keys():
        result.append(card_s[q])
    else:
        result.append(0)

print(*result)