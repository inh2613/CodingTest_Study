x=input()

num=x.split('-')

result=[]
for n in num:
    p=map(int,n.split('+'))
    result.append(sum(p))

answer=result[0]

for i in range(1,len(result)):
    answer-=result[i]

print(answer)

