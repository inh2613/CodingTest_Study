t=int(input())

def P(n):
    for i in range(n):
        if i==0 or i==1 or i==2:
            answer[i]=1
        elif i==3 or i==4:
            answer[i]=2
        elif i==5:
            answer[i]=answer[i-1]+answer[2]
        elif i==6:
            answer[i]=answer[i-1]+answer[1]
        elif i==7:
            answer[i]=answer[i-1]+answer[0]
        else:
            answer[i]=answer[i-1]+answer[i-5]
    #print(answer)

    return answer[n-1]



for _ in range(t):
    n=int(input())
    answer=[0]*n
    print(P(n))
