n,m=map(int,input().split())

n_set=set()
m_set=set()

for _ in range(n):
    input_=input()
    n_set.add(input_)

result=[]

for _ in range(m):
    input_=input()
    m_set.add(input_)

result=list(n_set.intersection(m_set))

result.sort()

print(len(result))
for r in result:
    print(r)