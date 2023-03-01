n=int(input())

for _ in range(n):
    query=input()
    stack=[]
    flag=0
    for i in query:
        if i=='(':
            stack.append(i)
        else:
            if stack:
                stack.pop()

            else:
                print('NO')
                flag=1
                break
    if stack and flag==0:
        print('NO')
    elif flag==0 and len(stack)==0:
        print('YES')