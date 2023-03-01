n=int(input())

t=[]
visited=[0]*(n)
answer=[]
for _ in range(n):
    x=int(input())
    t.append(x)
stack=[0]
j=1
for i in range(1,n+1):
    if 0 not in visited:
        if t[i-1]==stack[-1]:
            stack.pop()
            # print('-')
            answer.append('-')
        else:
            print('NO')
            exit()

    else:
        while stack[-1]!=t[i-1]:
            if visited[j-1]==0:
                visited[j-1]=1
                stack.append(j)
                j+=1
                answer.append('+')
            else:
                j+=1
            if j>n:
                break
        if stack:
            stack.pop()
            answer.append('-')


    # print(stack)

for a in answer:
    print(a)