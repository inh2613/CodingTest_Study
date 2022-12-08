n,m=map(int,input().split())

names=dict()
index_=dict()

for i in range(n):
    input_=input()
    names[input_]=i
    index_[i]=input_

for _ in range(m):
    query=input()
    if query.isdigit()==True:
        query=int(query)
        print(index_[query-1])

    else:
        print(names[query]+1)


