n=int(input())

init=666
cnt=1
while True:

    if cnt==n:
        break
    init+=1
    num=str(init)
    for i in range(len(num)-2):
        if num[i]=='6' and num[i+1]=='6' and num[i+2]=='6':
            cnt+=1
            break
    #print(cnt)
print(init)

