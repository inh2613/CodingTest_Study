while True:
    query=input()
    if query=='.':
        exit()
    stack=[]

    flag=0
    for q in query:
        if q=='(' or q=='[':
            stack.append(q)
        elif q==')':
            if stack:
                x=stack[-1]
                if x!='(':
                    print('no')
                    flag=1
                    break

                else:
                    stack.pop()
            else:
                flag=1
                print('no')
                break
        elif q==']':
            if stack:
                x=stack[-1]
                if x!='[':
                    print('no')
                    flag=1
                    break
                else:
                    stack.pop()
            else:
                flag=1
                print('no')
                break



    if flag==0:
        if len(stack)==0:
            print('yes')
        else:
            print('no')